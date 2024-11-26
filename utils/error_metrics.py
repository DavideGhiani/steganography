import numpy as np
from skimage.metrics import structural_similarity as ssim


class ErrorMetrics:
    def __init__(self, image_a, image_b):
        self.image_a = image_a
        self.image_b = image_b

    def mse(self):
        """ Calcola la differenza quadratica media tra i pixel corrispondenti di due immagini."""

        assert self.image_a.shape == self.image_b.shape, "Images must have the same dimensions"
        # Compute the MSE
        err = np.sum((self.image_a.astype("float") - self.image_b.astype("float")) ** 2)
        err /= float(self.image_a.shape[0] * self.image_a.shape[1])
        return err

    def psnr(self):
        """ Misura il rapporto tra il massimo valore possibile del pixel e la potenza della distorsione (MSE). """

        mse_value = self.mse()
        if mse_value == 0:
            return float('inf')
        max_pixel = 255.0
        psnr_value = 20 * np.log10(max_pixel / np.sqrt(mse_value))
        return psnr_value

    def compute_ssim(self):
        if self.image_a.shape != self.image_b.shape:
            raise ValueError("Images must have the same dimensions for SSIM calculation.")

        min_dim = min(self.image_a.shape[0],self.image_a.shape[1])
        win_size = min(7,min_dim) if min_dim >= 7 else min_dim

        ssim_value = ssim(self.image_a,self.image_b,win_size = win_size,multichannel = True,
            channel_axis = -1)
        return ssim_value

