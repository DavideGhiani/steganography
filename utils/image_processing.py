import cv2
import numpy as np


def resize_to_match(image_a, image_b):
    # Ensure both images are RGB (3 channels) before resizing
    if len(image_a.shape) == 2:  # Grayscale image
        image_a = cv2.cvtColor(image_a, cv2.COLOR_GRAY2RGB)
    if len(image_b.shape) == 2:
        image_b = cv2.cvtColor(image_b, cv2.COLOR_GRAY2RGB)

    if image_a.shape[2] == 4:  # Image with alpha channel
        image_a = cv2.cvtColor(image_a, cv2.COLOR_RGBA2RGB)
    if image_b.shape[2] == 4:
        image_b = cv2.cvtColor(image_b, cv2.COLOR_RGBA2RGB)

    # Resize image_a to match dimensions of image_b
    return cv2.resize(image_a,(image_b.shape[1], image_b.shape[0]))


