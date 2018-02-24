import logging
import signal
import sys
from config import AppConfig
from sdk_connection import RazerApp
from image_process import ImageProcessor


# set up the logger
logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO)


def quit_program(sig, frame):
    """Callback for when program is quit"""
    logger.warning('Quitting program')
    sys.exit()


def main():
    """Main function"""
    signal.signal(signal.SIGINT, quit_program)

    logging.info('Initialising connection to SDK server')
    config = AppConfig()
    with RazerApp(config.to_dict()) as app:
        logging.info('Connected to the the SDK server')
        logging.info('Beginning screen capture (Press Ctrl-C to quit)')

        while True:
            try:
                pixels = ImageProcessor.get_keyboard_pixels()
            except OSError as ose:
                logger.error(f'Error grabbing screenshot: {ose.strerror}')
                continue

            app.set_colour(pixels)


if __name__ == '__main__':
    main()
