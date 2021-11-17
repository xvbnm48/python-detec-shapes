import cv2
import numpy as np

img = cv2.imread("shape.png", cv2.IMREAD_GRAYSCALE)
_, threshold = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)
font = cv2.FONT_HERSHEY_COMPLEX

# _, contours , _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours,hierachy=cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
	approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
	cv2.drawContours(img, [approx], 0 , (255),5)
	print(len(approx))
	x = approx.ravel()[0]
	y =  approx.ravel()[1]
	if len(approx) == 3:
		cv2.putText(img, "triangle", (x,y), font,1,(255))
	elif len(approx) == 4:
		cv2.putText(img, "rectangle", (x,y), font,1,(255))
	elif len(approx) == 5:
		cv2.putText(img, "pentagon", (x,y), font,1,(255))
	elif 6 < len(approx) < 15 :
		cv2.putText(img, "ellipse", (x,y), font,1,(255))	
	else:
		cv2.putText(img, "circle", (x,y), font,1,(255))	

cv2.imshow("shapes", img)
cv2.imshow("Threshold", threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()

