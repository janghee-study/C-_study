# 0310 키보드 이벤트 처리방법
# 1.키 이벤트 받기
# 2.그림의 영역 처리
#-------------------------------
# Q)오각형을 그린 후 키보드 화살표키를 이용하여 이동이 가능하게 구현해주세요~~

import numpy as np
import cv2
import keyboard #Using module keyboard
import mouse

text = 'OpenCV program'
org = (50, 100)
width,height =512,512
x,y,R = 256,256,50
RB,LB = False,False
font = cv2.FONT_HERSHEY_SIMPLEX

direction = 0

event = 1

while True:
    key = cv2.waitKey(60)
    if key == 0x1B:  # if key 'q' is pressed
        break;
    elif key == 0x270000:
        direction = 0
    elif key == 0x280000:
        direction = 1
    elif key == 0x250000:
        direction = 2
    elif key == 0x260000:
        direction = 3
    elif mouse.is_pressed('LeftButton'): # 네모
        if LB == True:
            LB = False
        else :
            LB = True
    elif mouse.is_pressed(R):
        if RB == True:
            RB = False
        else :
            RB = True
    #방향으로 이동

    if direction == 0:
        x+=10
    elif direction == 1:
        y+=10
    elif direction == 2:
        x-=10
    elif direction == 3:
        y-=10

    if x<R:
        x=R
        direction=0
    if x > width - R:
        x = width - R
        direction = 2

    if y<R:
        y=R
        direction =1

    if y > height - R:
        y = height - R
        direction = 3

    img = np.zeros(shape=(512,512,3),dtype=np.uint8) + 255

    pts1 = np.array([[x-20, y-10], [x-10, y], [x,y], [x+10,y-10], [x-5,y-25]])

    cv2.polylines(img, [pts1], isClosed=True, color=(255, 0, 0))
    cv2.fillPoly(img, [pts1], color=(0, 0, 255))

    if LB == True:
        cv2.rectangle(img, (10,10), (50,50), (0, 0, 255))
    elif LB == False:
        pass

    if RB == True:
        cv2.putText(img, text, org, font, 1, (255, 0, 0), 2)
    elif RB == False:
        pass

    cv2.imshow('img', img)

cv2.destroyAllWindows()