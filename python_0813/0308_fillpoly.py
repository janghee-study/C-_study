#다각형 채우기
import cv2
import numpy as np

img = np.zeros(shape=(512,512,3),dtype=np.uint8) + 255

#삼각형
pts1 = np.array([[100,100],[250,20],[400,10],[45,350]])
pts2 = np.array([[300,200],[500,500],[50,45]])

cv2.polylines(img,[pts1,pts2],isClosed=True,color=(255,0,0))
cv2.fillPoly(img,[pts1],color=(0,0,255))
cv2.fillPoly(img,[pts2],color=(255,0,0))

cv2.imshow('title',img)
cv2.waitKey()
cv2.destroyAllWindows()
