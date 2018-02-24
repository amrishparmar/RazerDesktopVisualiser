import logging
from threading import Thread
from time import sleep
import requests


class RazerApp:
    """Handle connections to the SDK server"""

    def __init__(self, payload):
        r = requests.post("http://localhost:54235/razer/chromasdk", json=payload)
        self.uri = r.json()['uri']  # assign the uri from the SDK server response
        self.alive = True
        self._start_heartbeat()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def disconnect(self):
        """End connection to the SDK server"""
        logging.getLogger('Terminating connection to SDK server')
        self.alive = False
        self._hb_thread.join()
        requests.delete(self.uri)

    def _heartbeat(self):
        """Send a heartbeat to the SDK every second"""
        while self.alive:
            requests.put(self.uri + '/heartbeat')
            sleep(1)

    def _start_heartbeat(self):
        """Start the heartbeat thread to keep the SDK server connection alive"""
        self._hb_thread = Thread(target=self._heartbeat)
        self._hb_thread.start()

    def set_colour(self, values):
        """Update the colours on the keyboard with new values

        :param values: A 6 x 22 list of lists of BGR integers
        """
        payload = {
            'effect': 'CHROMA_CUSTOM',
            'param': values,
        }

        requests.put(self.uri + '/keyboard', json=payload)
