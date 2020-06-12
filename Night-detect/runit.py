import cv2
capture = cv2.VideoCapture(0)

while(True):
    ret, frame = capture.read()
 
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cube = cv2.resize(grayFrame, (1, 1) )
    webcam = cv2.resize(grayFrame, (320, 240))
    cv2.imshow('video gray', webcam)
    cv2.imshow('light', cube)
    if cv2.waitKey(1) == 27:
        break

    if cube > 10:
        day = cv2.imread('Daytime.png')
        dayr = cv2.resize(day, (640, 480))
        cv2.imshow('daytime', dayr)
        cv2.destroyWindow('night')
    if cube < 10:
        night = cv2.imread('night.png')
        nightr = cv2.resize(night, (640, 480))
        cv2.imshow('night', nightr)
        cv2.destroyWindow('daytime')
         
capture.release()
cv2.destroyAllWindows()

