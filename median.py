import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import median_filter
from PIL import Image

# Load image
image_path = 'D:\linh ta linh tinh\ảnh linh tinh\manh.png'
original_image = np.array(Image.open(image_path))

# Convert image to grayscale
gray_image = np.array(Image.open(image_path).convert('L'))

# Add Gaussian noise to the grayscale image
noise = np.random.normal(0, 20, size=gray_image.shape)
noisy_image = gray_image + noise

# Apply median filter to the noisy image
filtered_image = median_filter(noisy_image, size=3)

# Plot original and filtered images
plt.figure(figsize=(12, 6))

# Original Image
plt.subplot(1, 3, 1)
plt.imshow(original_image)
plt.title('Original Image')
plt.axis('off')

# Noisy Image
plt.subplot(1, 3, 2)
plt.imshow(noisy_image, cmap='gray')
plt.title('Noisy Image')
plt.axis('off')

# Filtered Image
plt.subplot(1, 3, 3)
plt.imshow(filtered_image, cmap='gray')
plt.title('Filtered Image (Median Filter)')
plt.axis('off')

plt.tight_layout()
plt.show()