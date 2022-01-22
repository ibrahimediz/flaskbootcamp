from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    user = {"username" : "Çay var simit var neye bakıyon"}
    return render_template("index.html",title="Birine mi baktın baba yiğit")