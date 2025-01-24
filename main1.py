import cv2
import numpy as np
import face_recognition

imgMaz = face_recognition.load_image_file('images/mazen.jpg')
imgMaz = cv2.cvtColor(imgMaz,cv2.COLOR_BGR2RGB)
imgMazt = face_recognition.load_image_file('images/mohamed.jpg')
imgMazt = cv2.cvtColor(imgMazt,cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgMaz)[0]
encode = face_recognition.face_encodings(imgMaz)[0]
cv2.rectangle(imgMaz,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)

faceLoct = face_recognition.face_locations(imgMazt)[0]
encodet = face_recognition.face_encodings(imgMazt)[0]
cv2.rectangle(imgMazt,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)

results = face_recognition.compare_faces([encode],encodet)
faceDis = face_recognition.face_distance([encode],encodet)
print(results,faceDis)
cv2.putText(imgMazt,f'{results}{round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

cv2.imshow('mazen.jpg',imgMaz)
cv2.imshow('mohamed.jpg',imgMazt)
cv2.waitKey(0)