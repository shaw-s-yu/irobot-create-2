import cv2
import numpy as np
from create2api import Create2


bot=Create2()
bot.start()
bot.safe()
cam=cv2.VideoCapture(0)
cv2.waitKey(1000)

while True:
    v=0
    ret,img=cam.read()
    
    blurred=cv2.GaussianBlur(img,(11,11),0)
    gray=cv2.cvtColor(blurred,cv2.COLOR_BGR2GRAY)
    
    circles=cv2.HoughCircles(gray,cv2.cv.CV_HOUGH_GRADIENT,1.2,100)
    if circles is not None:
        circles=np.round(circles[0,:]).astype('int')
        for (x,y,r) in circles:
            if r <110:
                v=30
            elif r <120:
                v=0
            else:
                v=-30
            cv2.circle(img,(x,y),r,(0,255,0),4)
    bot.drive_straight(v)
    cv2.imshow('image',img)
    if cv2.waitKey(1)==27:
        break

cam.release()
cv2.destroyAllWindows()

'''


    '''
