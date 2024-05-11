import numpy as np
import cv2 as cv
 
filename = 'shape.jpg'
img = cv.imread(filename)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
 
gray = np.float32(gray)
dst = cv.cornerHarris(gray,5,3,0.01)
 
# Đánh dấu góc trên ảnh gốc
img[dst > 0.01 * dst.max()] = [0, 0, 255]
 
# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]
 
cv.imshow('HARIS CORNER',img)
if cv.waitKey(0) & 0xff == 27:
 cv.destroyAllWindows()