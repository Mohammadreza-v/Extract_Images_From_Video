import cv2  
import numpy as np
import os

path = input("Enter Path Video : ")
cam = cv2.VideoCapture(path)

try: 
      
    if not os.path.exists('data'): 
        os.makedirs('data') 
  
except OSError: 
    print ('Error: Creating directory of data') 
  
currentframe = 0
  
while(True): 
      
    ret,frame = cam.read() 
  
    if ret: 
        name = './data/frame' + str(currentframe) + '.jpg'
        print ('Creating...' + name) 
  
        cv2.imwrite(name, frame) 
  
        currentframe += 1
    else: 
        break
  
cam.release() 
cv2.destroyAllWindows()
