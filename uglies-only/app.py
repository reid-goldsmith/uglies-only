from flask import Flask
from flask import render_template
from flask import request, redirect, url_for, flash
import os
import cv2
#reid is super cool


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)
UPLOAD_FOLDER = '/Users/reidgoldsmith/Desktop/Computa/uglies-only/uglies-only/uploads'
#UPLOAD_FOLDER = 'uploads'
app.secret_key = "dafadfaad"

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/upload-image", methods=["GET","POST"])
def upload_image():
    if request.method == 'POST':
        if request.files:
            image = request.files["image"]
            print(image)
            filename = image.filename
            if image and allowed_file(filename):
                image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                return redirect(url_for("results"))
            else:
                flash("Unsupported file type", 'error')
                return render_template("index.html")
           
           
            #return redirect(url_for('uploaded_file',filename=filename))

    return render_template("index.html")

@app.route('/results',methods=["GET",'POST'])
def results():
    os.chdir("/Users/reidgoldsmith/Desktop/Computa/uglies-only/uglies-only/uploads")
    print(os.getcwd())##
    #os.chdir("uploads")
    print(os.getcwd())##

    images = os.listdir()
    image = images[1]
    print(image)
    try:
        facial_recognition(image)
        return render_template("good_results.html",path=image)
    except:
        return render_template("bad_results.html")


def facial_recognition(img):
    image = cv2.imread(img)
    path = "/Users/reidgoldsmith/Desktop/Computa/uglies-only/uglies-only/haarcascade_frontalface_default.xml"
    #path = "haarcascade_frontalface_default.xml"

    face_cascade = cv2.CascadeClassifier(path)

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.10,minNeighbors=5,minSize=(40,40)) 
    for (x, y, w, h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(image,"Not Ugly",(x+50,y+50),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),2)



#gray = cv2.resize(gray, (0,0), fx=0.5, fy=0.5)

    cv2.imwrite("/Users/reidgoldsmith/Desktop/Computa/uglies-only/uglies-only/static/faces.jpg", image)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    app.run(debug=True)
     