#!/usr/local/bin/python3
import cv2
import numpy as np

# data = np.arange(6).reshape(2, 3)
"""
[[0 1 2]
 [3 4 5]]
"""
# data = data[:, :, np.newaxis]
"""
[[[0]
  [1]
  [2]]

 [[3]
  [4]
  [5]]]
"""
# data = data[:, :] * [0, 1, 0]
"""
[[[0 0 0]
  [0 1 0]
  [0 2 0]]

 [[0 3 0]
  [0 4 0]
  [0 5 0]]]
"""
# data = np.where(np.sum(data, axis=2) > 2, 0, 255).astype(np.uint8)
"""
[[255 255 255]
 [  0   0   0]]
"""
# data = np.arange(6).reshape(2, 3, 1)
# data1 = np.where(data[:, :] > 2, 0, 255).astype(np.uint8)
"""
[[[255]
  [255]
  [255]]

 [[  0]
  [  0]
  [  0]]]
"""

# Load the aerial image and convert to HSV colourspace
img = cv2.imread("../images/bullet.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = np.array(img, np.uint8)

# Make a True/False mask of pixels. Set True is color bigger then black
# alpha = img[:, :] > 0
# Convert True/False to 255/0
# alpha = np.uint8(alpha * 255)
alpha = np.where(img[:, :] > 0, 255, 0).astype(np.uint8)

colorMaskNormalized = np.array((0, 1, 0), np.uint8)

# Add new axis
img = img[:, :, np.newaxis]
print(img.shape)
# Replace axis=2 to [n] * colorMaskNormalized
img = img[:, :] * colorMaskNormalized
print(img.shape)

# Stack alpha layer with existing image to go from BGR to BGRA (3 channels to 4)
img = np.dstack((img, alpha))
print(img.shape)

cv2.imshow("Result", img)
cv2.imwrite("../images/bullet_green.png", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
