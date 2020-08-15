import os, cv2
from tqdm import tqdm
class ImageAugmentation:
    def _reflect(self, image, path):
        flipHorizontal = cv2.flip(image, 1)
        cv2.imwrite(path[:-4] + '-augmented-r.png', flipHorizontal)
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