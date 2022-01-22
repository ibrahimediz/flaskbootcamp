from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    user = {"username" : "Efe Can"}
    return render_template("index.html",title="Birine mi baktın baba yiğit")