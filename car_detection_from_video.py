import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2
import imutils
from PIL import Image

car_cascade_src = 'Required Files/cars.xml'

video_src = 'Required Files/Cars.mp4'
cap = cv2.VideoCapture(video_src)
car_cascade = cv2.CascadeClassifier(car_cascade_src)
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
video = cv2.VideoWriter('Required Files/result.avi',cv2.VideoWriter_fourcc(*'XVID'),fps,(width,height))

while(cap.isOpened()):
    ret,img = cap.read()
    
    if(type(img) == type(None)):
        break
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2. imshow('frame',gray)
    cars = car_cascade.detectMultiScale(gray,1.1,2)
    
    for(x,y,w,h) in cars:
        cv2.rectangle(img, (x,y),(x+w,y+h), (255,0,0),2)
        
        
  
    video.write(img)
video.release()
    


    
