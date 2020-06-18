import cv2

img_path = cv2.imread(str(input("Enter a photo path: ")))


path = "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(path)

gray = cv2.cvtColor(img_path,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,scaleFactor=1.10,minNeighbors=5,minSize=(40,40)) 
for (x, y, w, h) in faces:
    cv2.rectangle(img_path,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.putText(img_path,"This is a face",(x+50,y+50),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),2)



#gray = cv2.resize(gray, (0,0), fx=0.5, fy=0.5)

cv2.imshow("faces", img_path)

cv2.waitKey(0)
cv2.destroyAllWindows()

