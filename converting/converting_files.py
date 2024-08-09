import numpy as np
from PIL import Image
from typing import Union


def is_image_black_and_white(image_matrix: Union[list, np.ndarray, tuple]):
    pixels_set = set()
    for pixels in image_matrix:
        if isinstance(pixels, Union[list, tuple, np.ndarray]):
            for pixel in pixels:
                pixels_set.add(pixel)
        else:
            pixels_set.add(pixels)
    if len(pixels_set) == 2 and 0 in pixels_set and 1 in pixels_set:
        return True
    else:
        return False, 'image is not black and white, it is rgb image'


def matrix_to_image(image_matrix: Union[list, np.ndarray, tuple]) -> Image:
    if is_image_black_and_white(image_matrix):
        return Image.fromarray(image_matrix)
    else:
        return Image.fromarray(np.uint8(image_matrix))
