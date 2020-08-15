import cv2
import numpy as np

def adjust_gamma(image, gamma=1.0):
   invGamma = 1.0 / gamma
   table = np.array([((i / 255.0) ** invGamma) * 255 
   for i in np.arange(0, 256)]).astype("uint8")
   return cv2.LUT(image, table)

x = 'dataset/vivek/1.jpg'  #location of the image
original = cv2.imread(x)
cv2.imshow('original',original)

gammas = [0.5, 0.7, 1.3, 1.5]                                   # change the value here to get different result

def changeLighting(image, path):
    for gamma in gammas:
        adjusted = adjust_gamma(image, gamma=gamma)
        cv2.imwrite()
cv2.destroyAllWindows()