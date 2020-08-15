import cv2
image = cv2.imread('dataset/vivek/0.jpg')
flipHorizontal = cv2.flip(image, 1)
cv2.imshow('original', image)
cv2.imshow('Flip horizontal', flipHorizontal)
cv2.waitKey(0)