import os, cv2, imutils
import numpy as np
from tqdm import tqdm
class ImageAugmentation:
    def _reflect(self, image, path):
        flipHorizontal = cv2.flip(image, 1)
        outPath = path[:-4] + '-reflected.png'
        cv2.imwrite(outPath, flipHorizontal)
        return outPath
    def _adjust_gamma(self, image, gamma=1.0):
        invGamma = 1.0 / gamma
        table = np.array([((i / 255.0) ** invGamma) * 255 
        for i in np.arange(0, 256)]).astype("uint8")
        return cv2.LUT(image, table)
    def _changeLighting(self, image, path):
        gammas = [0.5, 0.7, 1.3, 1.5]
        for gamma in gammas:
            adjusted = self._adjust_gamma(image, gamma=gamma)
            cv2.imwrite(path[:-4]+'-augmented-' + str(gamma) + '.png', adjusted)
    def execute(self):
        people = os.listdir('dataset/')
        people.remove('unknown')
        for person in people:
            personPath = 'dataset/' + person + '/'
            print(person)
            for image in tqdm(os.listdir(personPath)):
                if 'augmented' not in image and '.DS_Store' not in image:
                    path = personPath + image
                    photo = cv2.imread(path)
                    reflectedPath = self._reflect(photo, path)
                    reflectedPhoto = cv2.imread(reflectedPath)
                    self._changeLighting(photo, path)
                    self._changeLighting(reflectedPhoto, reflectedPath)
ImageAugmentation().execute()