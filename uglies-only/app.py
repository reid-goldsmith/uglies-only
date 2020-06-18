from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/') #adding stuff dope dope dlk;asfjlk;adsfjslfdsakfma
def hello_world():
    return render_template("index.html") #this renders the template
