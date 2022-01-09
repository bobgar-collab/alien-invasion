#!/usr/local/bin/python3
import cv2

img = cv2.imread("../images/bullet.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, alpha = cv2.threshold(imgGray, 0, 255, cv2.THRESH_BINARY)
b, g, r = cv2.split(img)

# rgba = [b, g, r, alpha] to Green
rgba = [b * 0, g, r * 0, alpha]
dst = cv2.merge(rgba, 4)

cv2.imshow("Result", dst)
cv2.imwrite("../images/bullet_green.png", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
