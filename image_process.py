from PIL import ImageGrab
from ctypes import windll


# enable DPI-aware behaviour for Pillow functions
user32 = windll.user32
user32.SetProcessDPIAware()


class ImageProcessor:
    """A collection of functions for turning images into Razer SDK keyboard-friendly representations"""

    @staticmethod
    def _get_resized_screen_pixels(columns=22, rows=6):
        """Grab a screenshot and resize to keyboard-friendly dimensions

        :param columns: An integer, the number of columns on the keyboard
        :param rows: An integer, the number of rows on the keyboard
        :return: An Image object, the resized image
        """
        img = ImageGrab.grab()
        img = img.resize((columns, rows))
        return img

    @staticmethod
    def get_keyboard_pixels():
        """Take a screenshot of the display, resize it and convert to a 6 x 22 list of BGR integers

        :return: A 6 x 22 list of lists of BGR integers
        """
        img = ImageProcessor._get_resized_screen_pixels()

        pixel_list = []

        for r in range(img.height):
            row = []
            for c in range(img.width):
                p = ImageProcessor._rgb_to_bgr_int(img.getpixel((c, r)))
                row.append(p)
            pixel_list.append(row)

        return pixel_list

    @staticmethod
    def _rgb_to_bgr_int(rgb):
        """Convert an rgb tuple into a corresponding BGR integer

        :param rgb: A tuple in the format (R, G, B) where R, G, B are 0 - 255
        :return: An integer, a BGR integer representation
        """
        return rgb[0] * pow(2, 0) + rgb[1] * pow(2, 8) + rgb[2] * pow(2, 16)
