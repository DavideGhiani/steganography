import numpy as np
from skimage.metrics import structural_similarity as ssim


class ErrorMetrics:
    def __init__(self, image_a, image_b):
        self.image_a = image_a
        self.image_b = image_b

    def mse(self):
        """ Calculate the average squared difference between corresponding pixels of the secret and revealed-secrets."""

        assert self.image_a.shape == self.image_b.shape, "Images must have the same dimensions"
        # Compute the MSE
        err = np.sum((self.image_a.astype("float") - self.image_b.astype("float")) ** 2)
        err /= float(self.image_a.shape[0] * self.image_a.shape[1])
        return err

    def psnr(self):
        """ Measure the ratio between the maximum possible pixel value and the power of the distortion (MSE). """

        mse_value = self.mse()
        if mse_value == 0:
            return float('inf')
        max_pixel = 255.0
        psnr_value = 20 * np.log10(max_pixel / np.sqrt(mse_value))
        return psnr_value

    def compute_ssim(self):
        # Ensure both images have the same dimensions
        if self.image_a.shape != self.image_b.shape:
            raise ValueError("Images must have the same dimensions for SSIM calculation.")

        # Compute the smallest valid win_size (odd number <= min_dim)
        min_dim = min(self.image_a.shape[0],self.image_a.shape[1])
        win_size = min(7,min_dim)  # Ensure win_size <= min_dim
        if win_size % 2 == 0:  # Ensure win_size is odd
            win_size -= 1

        # Handle edge case: min_dim < 3
        if win_size < 3:
            raise ValueError("Image dimensions are too small for SSIM calculation with a valid win_size.")

        # Compute SSIM
        ssim_value = ssim(self.image_a,self.image_b,win_size = win_size,multichannel = True,data_range = 1.0
            # Explicitly set the data range for normalized images
        )
        return ssim_value

    def compute_ssim_new(self):
        # Ensure both images have the same dimensions
        if self.image_a.shape != self.image_b.shape:
            raise ValueError("Images must have the same dimensions for SSIM calculation.")

        # Compute SSIM
        min_dim = min(self.image_a.shape[0],self.image_a.shape[1])
        win_size = min(7,min_dim) if min_dim >= 7 else min_dim  # Use the smallest odd size >= 3

        ssim_value = ssim(self.image_a,self.image_b,win_size = win_size,multichannel = True,
            # Use this if images have color channels
            channel_axis = -1  # For multichannel, typically the last axis
        )
        return ssim_value

