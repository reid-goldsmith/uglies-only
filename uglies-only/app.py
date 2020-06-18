from flask import Flask
from flask import render_template
from flask import request, redirect
import cv2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/upload-image", methods=["GET","POST"])
def upload_image():

    if request.files:
        image = request.files["image"]
        print(image)
        return redirect(request.url)

    return render_template("index.html")

@app.route('/results',methods=['POST'])
def results():
    return "faces.jpg"


def facial_recognition(img):
    image = cv2.imread(img)
    path = "haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(path)

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.10,minNeighbors=5,minSize=(40,40)) 
    for (x, y, w, h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(image,"Not Ugly",(x+50,y+50),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),2)



#gray = cv2.resize(gray, (0,0), fx=0.5, fy=0.5)

    cv2.imwrite("faces.jpg", image)