from hasan.app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    title='Namımızın büyüklüyü dostlarımızın büyüklüğündendir'
    name='Süleyman Çakır'
    return render_template('index.html',title=name,name=title)

