
import cv2
import time

cap = cv2.VideoCapture('3.mp4')
time.sleep(2)

fgbg = cv2.createBackgroundSubtractorMOG2()
j = 0
while(1):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fgmask = fgbg.apply(gray)
    contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        areas = []

        for contour in contours:
            ar = cv2.contourArea(contour)
            areas.append(ar)
        
        max_area = max(areas or [0])

        max_area_index = areas.index(max_area)

        cnt = contours[max_area_index]

        M = cv2.moments(cnt)
        
        x, y, w, h = cv2.boundingRect(cnt)

        cv2.drawContours(fgmask, [cnt], 0, (255,255,255), 3, maxLevel = 0)
        
        if h < w:
            j += 1
            
        if j > 5:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)



        cv2.imshow('video', frame)
    
        if cv2.waitKey(33) == 27:
         break
cv2.destroyAllWindows()
