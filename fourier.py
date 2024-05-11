### INSTALL LIBRARY ###
### python -m pip install -U scipy matplotlib ###



### link: https://realpython.com/python-scipy-fft/ ###
### https://docs.scipy.org/doc/scipy/tutorial/fft.html ###


import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft2, fftshift
from PIL import Image

# Load image
image_path = 'D:\linh ta linh tinh\ảnh linh tinh\image.jpeg'
image = np.array(Image.open(image_path))
gray_image = np.array(Image.open(image_path).convert('L'))  # Convert to grayscale

# Perform Fourier transform
fft_image = fft2(gray_image)
fft_image_shifted = fftshift(fft_image)  # Shift the zero frequency component to the center

# Calculate the magnitude spectrum
magnitude_spectrum = np.abs(fft_image_shifted)

# Create a new figure with subplots
plt.figure(figsize=(10, 5))

# Subplot 1: Original Image
plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image', fontsize=10)
plt.axis('off')

# Subplot 2: Image with Fourier Spectrum
plt.subplot(1, 3, 2)
plt.imshow(gray_image, cmap='gray')
plt.title('Gray Image', fontsize=10)
plt.axis('off')

# Subplot 3: Fourier Spectrum
plt.subplot(1, 3, 3)
plt.imshow(np.log(1 + magnitude_spectrum), cmap='gray')
plt.title('Fourier Spectrum', fontsize=10)
plt.axis('off')

plt.show()






# SAMPLE_RATE = 44100  # Hertz
# DURATION = 5  # Seconds

# def generate_sine_wave(freq, sample_rate, duration):
#     x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
#     frequencies = x * freq
#     # 2pi because np.sin takes radians
#     y = np.sin((2 * np.pi) * frequencies)
#     return x, y

# # Generate a 2 hertz sine wave that lasts for 5 seconds
# x, y = generate_sine_wave(2, SAMPLE_RATE, DURATION)
# plt.plot(x, y)
# plt.show()


# # Number of sample points
# N = 600
# # sample spacing
# T = 1.0 / 800.0
# x = np.linspace(0.0, N*T, N, endpoint=False)
# y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
# yf = fft(y)
# xf = fftfreq(N, T)[:N//2]
# plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
# plt.grid()
# plt.show()