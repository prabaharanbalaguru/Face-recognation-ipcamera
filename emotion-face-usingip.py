# -*- coding: utf-8 -*-
"""
Created on Sat June 29 21:19:12 2024

@author: Prabaharan Balaguru
"""
from facial_emotion_recognition import EmotionRecognition
import urllib.request
import numpy as np
import imutils
import cv2

er = EmotionRecognition(device='cpu')
url='http://192.168.1.2:8080/shot.jpg'

while True:
    imgpath=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgpath.read()),dtype=np.uint8)
    frame=cv2.imdecode(imgNp,-1)
    frame=er.recognise_emotion(frame,return_type='BGR')
    print(frame)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:  # Press ESC to exit
        break
cam.release()
cv2.destroyAllWindows()
