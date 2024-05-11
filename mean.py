import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Đọc ảnh đầu vào
input_image_path = '.\manh.png'
input_image = cv2.imread(input_image_path)
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

# Kiểm tra xem ảnh có tồn tại không
if input_image is None:
    print("Không thể đọc được ảnh. Hãy chắc chắn rằng đường dẫn đến ảnh là chính xác.")
else:
    # Thực hiện lọc trung bình với kernel 3x3
    filtered_image = cv2.medianBlur(gray_image, 5)

    # Hiển thị ảnh gốc, ảnh grayscale và ảnh đã lọc trên cùng một hình (figure)
    plt.figure(figsize=(15, 5))

    # Ảnh gốc
    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.axis('off')

    # Ảnh grayscale
    plt.subplot(1, 3, 2)
    plt.imshow(gray_image, cmap='gray')
    plt.title('Grayscale Image')
    plt.axis('off')
    
    # Ảnh đã lọc
    plt.subplot(1, 3, 3)
    plt.imshow(filtered_image, cmap='gray')
    plt.title('Filtered Image')
    plt.axis('off')

    plt.show()
