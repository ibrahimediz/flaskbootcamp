from app import app
from flask import render_template

@app.route('/')
@app.route('/index')

def index():
    user = {"kullaniciadi": "Bilal"}
    return render_template('index.html', title="Web projesi", user=user)