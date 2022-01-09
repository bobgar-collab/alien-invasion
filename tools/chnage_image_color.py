#!/usr/local/bin/python3
import cv2
import numpy as np

# data = np.arange(6).reshape(2, 3)
# """
# [[0 1 2]
#  [3 4 5]]
# """
#
# data = data[:, :, np.newaxis]
# # print(data)
# """
# [[[0]
#   [1]
#   [2]]
#
#  [[3]
#   [4]
#   [5]]]
# """
# print(data[:, :]*[1, 1, 1])

# Load the aerial image and convert to HSV colourspace
image = cv2.imread("../images/bullet.png")
print(image.shape)

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = np.array(image, np.uint8)

# Make a True/False mask of pixels. Set True is color bigger then black
alpha = image[:, :] > 0
# Convert True/False to 0/255
alpha = np.uint8(alpha * 255)
print(alpha)

# alpha = np.where((image == 0).all(axis=2), 0, 255).astype(np.uint8)
# print(alpha)

colorMaskNormalized = np.array((0, 1, 0), np.uint8)

# Add new axis
image = image[:, :, np.newaxis]
print(image.shape)
# Replace axis=2 to [n] * colorMaskNormalized
image = image[:, :] * colorMaskNormalized
print(image.shape)

# Stack alpha layer with existing image to go from BGR to BGRA (3 channels to 4)
image = np.dstack((image, alpha))
print(image.shape)

cv2.imshow("Result", image)
cv2.imwrite("../images/bullet_green.png", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
