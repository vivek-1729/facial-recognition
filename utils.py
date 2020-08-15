import os, cv2
from tqdm import tqdm
class ImageAugmentation:
    def _reflect(self, image, path):
        flipHorizontal = cv2.flip(image, 1)
        cv2.imwrite(path[:-4] + '-augmented-r.png', flipHorizontal)
    def adjust_gamma(image, gamma=1.0):
        invGamma = 1.0 / gamma
        table = np.array([((i / 255.0) ** invGamma) * 255 
        for i in np.arange(0, 256)]).astype("uint8")
        return cv2.LUT(image, table)
    def execute(self):
        for person in os.listdir('dataset/'):
            personPath = 'dataset/' + person + '/'
            print(person)
            for image in tqdm(os.listdir(personPath)):
                if 'augmented' not in image and '.DS_Store' not in image:
                    path = personPath + image
                    photo = cv2.imread(path)
                    self._reflect(photo, path)
ImageAugmentation().execute()