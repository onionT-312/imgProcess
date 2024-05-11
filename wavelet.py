### INSTALL LIBRARY ###
### pip install PyWavelets ###
### pip install matplotlib ###

import matplotlib.pyplot as plt
import numpy as np

import pywt
import pywt.data

from PIL import Image


### link: https://pywavelets.readthedocs.io/en/latest/ ###

# Load image
# original = pywt.data.camera()
image_path = 'D:\linh ta linh tinh\ảnh linh tinh\image.jpeg'
original = plt.imread(image_path)

# Wavelet transform of image, and plot approximation and details
titles = ['Approximation', 'Horizontal detail', 'Vertical detail', 'Diagonal detail']
coeffs2 = pywt.dwt2(original, 'bior1.3')
LL, (LH, HL, HH) = coeffs2

# Create a new figure with appropriate size
plt.figure(figsize=(10, 5))

# Plot each coefficient
for i, coef in enumerate([LL, LH, HL, HH]):
    # Add a subplot for each coefficient
    plt.subplot(1, 4, i + 1)
    
    # Display the coefficient
    plt.imshow(coef, cmap=plt.cm.gray)
    
    # Set title for the subplot
    plt.title(titles[i], fontsize=10)
    
    # Remove ticks on x and y axes
    plt.xticks([])
    plt.yticks([])

# Adjust layout to make subplots fit nicely
plt.tight_layout()

# Show the plot
plt.show()



### link: https://www.scicoding.com/introduction-to-wavelet-transform-using-python/ ###

# # Generate the signal
# t = np.linspace(0, 1, 1000, endpoint=False)
# signal = np.cos(2.0 * np.pi * 7 * t) + np.sin(2.0 * np.pi * 13 * t)

# # Apply DWT
# coeffs = pywt.dwt(signal, 'db1')
# cA, cD = coeffs

# # Plotting
# plt.figure(figsize=(12, 4))
# plt.subplot(1, 3, 1)
# plt.plot(t, signal)
# plt.title("Original Signal")
# plt.subplot(1, 3, 2)
# plt.plot(cA)
# plt.title("Approximation Coefficients")
# plt.subplot(1, 3, 3)
# plt.plot(cD)
# plt.title("Detail Coefficients")
# plt.tight_layout()
# plt.show()


# # Generate a chirp signal
# t = np.linspace(0, 1, 1000, endpoint=False)
# signal = np.sin(2.0 * np.pi * 7 * t * t)

# # Apply CWT
# coefficients, frequencies = pywt.cwt(signal, scales=np.arange(1, 128), wavelet='cmor')

# # Plotting
# plt.figure(figsize=(10, 6))
# plt.imshow(np.abs(coefficients), aspect='auto', cmap='jet', extent=[0, 1, 1, 128])
# plt.colorbar(label="Magnitude")
# plt.ylabel("Scale")
# plt.xlabel("Time")
# plt.title("CWT of a Chirp Signal")
# plt.show()