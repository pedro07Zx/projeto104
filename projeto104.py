import cv2
img = cv2.imread("/home/pdhqferreira/Python/solar-system.jpg")

cv2.putText(img,"Sol",(100,80),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255))
cv2.putText(img,"Mercurio",(165,60),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255))
cv2.putText(img,"Venus",(122,265),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255))
cv2.putText(img,"Terra",(276,340),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255))
cv2.putText(img,"Marte",(346,257),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255))
cv2.putText(img,"Jupiter",(568,31),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255))
cv2.putText(img,"Saturno",(823,338),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255))
cv2.putText(img,"Urano",(920,113),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255))
cv2.putText(img,"Netuno",(1086,389),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255))




cv2.imshow("resultado",img)
cv2.waitKey(0)