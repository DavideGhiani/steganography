from utils.image_processing import field_morphing
import csv
from utils.error_metrics import ErrorMetrics
from configuration import settings
import cv2
import numpy as np

cover_image = np.array(cv2.imread(settings.cover_path, cv2.IMREAD_UNCHANGED))
secret_image = np.array(cv2.imread(settings.secret_path, cv2.IMREAD_UNCHANGED))
encoded_image = np.array(cv2.imread(settings.encoded_path, cv2.IMREAD_UNCHANGED))
recovered_image = np.array(cv2.imread(settings.recovered_path, cv2.IMREAD_UNCHANGED))
post_morph_recovered_image = np.array(cv2.imread(settings.post_morph_recovered_path, cv2.IMREAD_UNCHANGED))

# Field morphing sull'immagine codificata:
encoded_morphed = field_morphing(encoded_image)

# Lista di confronti e relativi nomi dei file:
comparisons = [
    ("Cover vs Encoded", cover_image, encoded_image),
    ("Secret vs Recovered", secret_image, recovered_image),
    ("Encoded vs Encoded Morphed", encoded_image, encoded_morphed),
    ("Secret vs Post-Morph Recovered", secret_image, post_morph_recovered_image)
]

output_csv_path = "/Users/davideghiani/Git/steganography/data/metrics_results.csv"

with open(output_csv_path, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Comparison", "SSIM", "MSE", "PSNR"])

    for name, img1, img2 in comparisons:
        evaluator = ErrorMetrics(img1, img2)
        ssim = evaluator.compute_ssim()
        mse = evaluator.mse()
        psnr = evaluator.psnr()

        writer.writerow([name, ssim, mse, psnr])

print(f"Metrics saved to {output_csv_path}")
