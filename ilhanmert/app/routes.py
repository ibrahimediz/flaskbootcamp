from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    user ={"kullaniciadi":"ilhan"}
    return render_template("index.html",title="Web sitesi", user=username)