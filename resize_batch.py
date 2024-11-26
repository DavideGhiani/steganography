import os
import cv2
from configuration import settings
from utils.image_processing import resize_to_optimal_square

os.makedirs(settings.processed_images_path, exist_ok = True)

for el in os.listdir(settings.to_resize):
    img = cv2.imread(os.path.join(settings.to_resize, el))

    if img is None:
        print(f"Immagine non valida o impossibile da leggere: {el}")
        continue

    resized_image = resize_to_optimal_square(img, 224)

    output_file = os.path.splitext(el)[0] + ".png"

    cv2.imwrite(os.path.join(settings.processed_images_path, output_file), resized_image)

