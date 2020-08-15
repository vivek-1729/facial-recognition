import numpy as np
import cv2
from datetime import datetime

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(frame,'Press t to take photo and q to quit', (50,50), font,1, (255,0,0))
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF==ord('t'):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cv2.imwrite('dataset/vivek/' + str(datetime.now()) + '.jpg',frame)
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()