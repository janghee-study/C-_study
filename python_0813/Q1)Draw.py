# 빨간지붕집그리기
import cv2
import numpy as np

img = np.zeros(shape=(512,512,3),dtype=np.uint8) + 255

#네모
x1,x2 = 100,400
y1,y2 = 100,400
cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,0))
#직선
cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2)
cv2.line(img,(x2,y1),(x1,y2),(0,0,0),2)
#원
cx = (img.shape[0] // 2)  #정중앙에 두기위해서
cy = (img.shape[1] // 2)
cv2.circle(img,(250,250),radius=150,color=(255,255,255),thickness=-1)
cv2.circle(img,(250,250),radius=150,color=(0,0,255))
#삼각형
pts1 = np.array([[100,100],[250,20],[400,100]])
cv2.polylines(img,[pts1],isClosed=True,color=(255,0,0))
cv2.fillPoly(img,[pts1],color=(0,0,255))

cv2.imshow('title',img)
cv2.waitKey()
cv2.destroyAllWindows()
