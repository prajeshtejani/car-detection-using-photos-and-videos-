import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2
import imutils
from PIL import Image
#Import Image
img  = Image.open('Data/cars.png')
img = img.resize((450,250))
img_array = np.array(img)

#convert image into gray_scale for better output
gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)

#add Gausian Filter to reduce noice
blur = cv2.GaussianBlur(gray,(5,5),0)

#use dilate which is used to add boundry on object
dilate = cv2.dilate(blur, np.ones((3,3)))

#perform Morphological Transformation which is used to defined difference betweeen dilate and erosion
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2,2))
closing = cv2.morphologyEx(dilate, cv2.MORPH_CLOSE, kernel)

#using carcascade xml train model using Carcascade classifier

car_cascade_src = 'Required Files/cars.xml'
car_cascade = cv2.CascadeClassifier(car_cascade_src)
cars = car_cascade.detectMultiScale(closing,1.1,1)

cnt = 0
for(x,y,w,h) in cars:
    cv2.rectangle(img_array, (x,y),(x+w,y+h), (255,0,0),2)
    cnt += 1
print(cnt,'cars found')
Image.fromarray(img_array)


    
  
    
