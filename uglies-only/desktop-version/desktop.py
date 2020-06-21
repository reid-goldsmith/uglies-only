from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import cv2 


def facial_recognition(img):
    image = cv2.imread(img)
    path = "/Users/20goldsmithr/uglies-only/uglies-only/desktop-version/haarcascade_smile.xml"

    face_cascade = cv2.CascadeClassifier(path)

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.10,minNeighbors=5,minSize=(40,40)) 
    for (x, y, w, h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(image,"Not Ugly",(x+50,y+50),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),2)
    cv2.imwrite("/Users/20goldsmithr/uglies-only/uglies-only/desktop-version/output/faces.jpg", image)
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image', 600,600)
    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

root = Tk()

label = ttk.Label(root, text="uglies only")
label.pack()
def func1():
    filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file")#,filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    facial_recognition(filename)

'''
def func2():
    cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 
    ret,frame = cap.read() # return a single frame in variable `frame`

    while(True):
        cv2.imshow('img1',frame) #display the captured image
        if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y' 
            cv2.imwrite('images/c1.png',frame)
            cv2.destroyAllWindows()
            break

    cap.release()  
'''
button1 = ttk.Button(root, text="Select Image", command=func1)
#button2 = ttk.Button(root, text="Take Picture",command=func2)
button1.pack()
#button2.pack()


root.mainloop()





