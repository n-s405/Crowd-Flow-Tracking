import cv2
import time
import os

person_cascade = cv2.CascadeClassifier(
    os.path.join('/Users/samarthnegi/Google Drive/2019 Engineer Sync/CS Projects/MAIT - Major - CV Activity Logger/private-data/Haar Cascades/haarcascade_fullbody.xml'))
cap = cv2.VideoCapture('/Users/samarthnegi/Google Drive/2019 Engineer Sync/CS Projects/MAIT - Major - CV Activity Logger/private-data/sexy.avi')
while True:
    r, frame = cap.read()
    if r:
        start_time = time.time()
        frame = cv2.resize(frame,(640,360)) # Downscale to improve frame rate
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY) # Haar-cascade classifier needs a grayscale image
        rects = person_cascade.detectMultiScale(gray_frame)
        
        end_time = time.time()
        print("Elapsed Time:",end_time-start_time)
            
        for (x, y, w, h) in rects:
            cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,0),2)
        cv2.imshow("preview", frame)
    k = cv2.waitKey(1)
    if k & 0xFF == ord("q"): # Exit condition
        break