import cv2
import numpy as np
import matplotlib.pyplot as plt

# Đọc ảnh đầu vào
image_path = 'manh.png'
input_image = cv2.imread(image_path)

# Kiểm tra xem ảnh có tồn tại không
if input_image is None:
    print("Không thể đọc được ảnh. Hãy chắc chắn rằng đường dẫn đến ảnh là chính xác.")
else:
    # Tăng độ sáng của ảnh
    brightness_factor = 1.5  # Điều chỉnh độ sáng theo nhu cầu
    brightened_image = cv2.convertScaleAbs(input_image, alpha=brightness_factor, beta=0)

    # Chắc chắn rằng giá trị pixel không vượt quá 255
    brightened_image = np.clip(brightened_image, 0, 255)

    # Hiển thị ảnh gốc và ảnh đã tăng độ sáng
    plt.figure(figsize=(10, 5))

    # Ảnh gốc
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.axis('off')

    # Ảnh đã tăng độ sáng
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(brightened_image, cv2.COLOR_BGR2RGB))
    plt.title('Brightened Image')
    plt.axis('off')

    plt.show()
