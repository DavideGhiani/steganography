import cv2
import numpy as np


def resize_to_match(image_a, image_b):
    if len(image_a.shape) == 2:
        image_a = cv2.cvtColor(image_a, cv2.COLOR_GRAY2RGB)
    if len(image_b.shape) == 2:
        image_b = cv2.cvtColor(image_b, cv2.COLOR_GRAY2RGB)

    if image_a.shape[2] == 4:
        image_a = cv2.cvtColor(image_a, cv2.COLOR_RGBA2RGB)
    if image_b.shape[2] == 4:
        image_b = cv2.cvtColor(image_b, cv2.COLOR_RGBA2RGB)

    return cv2.resize(image_a,(image_b.shape[1], image_b.shape[0]))


def resize_to_optimal_square(image, scale):

    return cv2.resize(image, (scale, scale))


def field_morphing(img):
    rows, cols = img.shape[:2]

    center_x, center_y = cols // 2, rows // 2
    map_x = np.zeros_like(img[:, :, 0], dtype=np.float32)
    map_y = np.zeros_like(img[:, :, 0], dtype=np.float32)

    for i in range(rows):
        for j in range(cols):
            dx = j - center_x
            dy = i - center_y
            map_x[i, j] = center_x + dx * 0.9
            map_y[i, j] = center_y + dy * 0.9

    warped_img = cv2.remap(img, map_x, map_y, interpolation=cv2.INTER_LINEAR)

    cv2.imwrite("/Users/davideghiani/Git/steganography/data/to_measure/zoom_morph.png", warped_img)

    return warped_img

