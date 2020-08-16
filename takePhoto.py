import numpy as np
import cv2, os
from datetime import datetime

personName = input('Person name (type "new" to make a new folder): ')
if personName == 'new':
    personName = input('name: ')
    os.mkdir('dataset/'+personName)
validNames = os.listdir('dataset/')
if personName not in os.listdir('dataset/'):
    raise NameError("No folder exists for this person. Valid folder names are: " + ', '.join(validNames))

cap = cv2.VideoCapture(0)

while(True):
    path = 'dataset/' + personName + '/'
    ret, frame = cap.read()
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(frame,'Press t to take photo and q to quit', (50,50), font,1, (255,0,0))
    cv2.putText(frame,'It is sometimes difficult for the key press to register. If it doesn\'t, keep trying', (50,100), font,0.8, (255,0,0))
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF==ord('t'):
        print('Photo taken')
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cv2.imwrite(path + str(datetime.now()) + '.jpg',frame)
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
print('Photos taken will be stored in dataset/' + personName)