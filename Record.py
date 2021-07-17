import time
import cv2
import requests
from tempfile import NamedTemporaryFile
from PIL import Image
import sys
import numpy as np
import glob

#after each record change exportfilename in (out=cv2.Videowriter(...)), otherwise it will be overwritten
framerate = 2

#in sekunden
aufnahmezeit = 10

camera_IP = '169.254.7.82'
        
starttime = time.process_time()

print("Before URL")

#ans = requests.get('http://admin:asdf@169.254.18.4:8099/frame.jpg?id=147647551')
# print(ans.status_code, ans.content)
#with open('D:/asdf.jpg', 'wb+') as f:
#f.write(ans.content)
#image = Image.open('D:/asdf.jpg')
#image.show()

    
cap = cv2.VideoCapture('http://test1234:Test1234@{}/cgi-bin/mjpeg?stream=[1]'.format(camera_IP))
#cap = cv2.VideoCapture('D:\Graubeamer_files\Test1234_rec_000003.avi')

if not cap:
    print("!!! Failed VideoCapture: invalid parameter!")
    
#set framecounter to 0
frameNr = 0

print("After URL")
start = time.time()

img_array = []

while True:    
    time.sleep(1/framerate)
    print('About to start the Read command')
    red, frame = cap.read()
    
    if red:
        cv2.imshow("Frame",frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
        status = cv2.imwrite(f'D:/Graubeamer_files/frame_{frameNr}.jpg', frame)
    frameNr = frameNr+1
     
    print("Image written to file-system : ",status)
    
    height, width, layers = frame.shape
    size = (width,height)
    img_array.append(frame)
    print("Image appended to array")

    if time.time() > start + aufnahmezeit:
        print("I will break")
        break

print("writing done")

#save frames as video
out = cv2.VideoWriter(f'D:/Graubeamer_files/video_out_of_frames6.mp4',cv2.VideoWriter_fourcc(*'DIVX'), framerate, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()

print("video safing done")

cap.release()
cv2.destroyAllWindows()


    
#http://test1234:Test1234@169.254.7.82/Medialnput    
#http://test1234:Test1234@169.254.7.82/live'
#http://test1234:Test1234@169.254.7.82/Medialnput/IE/stream_1
#http://test1234:Test1234@169.254.7.82/image/bt_inf.gif'
#http://test1234:Test1234@169.254.7.82