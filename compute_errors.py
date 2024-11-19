import os.path

from utils.error_metrics import ErrorMetrics
from utils.image_processing import resize_to_match
from configuration import settings
from PIL import Image
import cv2
import numpy as np

cover_image = np.array(cv2.imread(settings.cover_path, cv2.IMREAD_UNCHANGED))
secret_image = np.array(cv2.imread(settings.secret_path, cv2.IMREAD_UNCHANGED))
recovered_image_1 = np.array(cv2.imread(settings.recovered_path_1, cv2.IMREAD_UNCHANGED))
recovered_image_2 = np.array(cv2.imread(settings.recovered_path_2, cv2.IMREAD_UNCHANGED))
recovered_image_3 = np.array(cv2.imread(settings.recovered_path_3, cv2.IMREAD_UNCHANGED))

to_evaluate = [recovered_image_1, recovered_image_2, recovered_image_3]
file_names = [os.path.basename(settings.recovered_path_1), os.path.basename(settings.recovered_path_2), os.path.basename(settings.recovered_path_3)]

print(f"COVER IMAGE SHAPE: {cover_image.shape}")
print(f"SECRET IMAGE SHAPE: {secret_image.shape}")
print(f"RECOVERED IMAGE 1 SHAPE: {recovered_image_1.shape}")
print(f"RECOVERED IMAGE 2 SHAPE: {recovered_image_2.shape}")
print(f"RECOVERED IMAGE 3 SHAPE: {recovered_image_3.shape}")

for i, el in enumerate(to_evaluate, start=0):
    aligned_secret_image = resize_to_match(secret_image, el)
    aligned_secret_image = aligned_secret_image
    evaluator = ErrorMetrics(aligned_secret_image, el)

    print(f"--- Metrics for Recovered Image {file_names[i]} ---")
    print(f"SSIM: {evaluator.compute_ssim()}")
    print(f"MSE: {evaluator.mse()}")
    print(f"PSNR: {evaluator.psnr()}")
