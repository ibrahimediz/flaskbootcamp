from app import app


from flask import render_template


@app.route('/')
@app.route('/index')

def index():
    user = {'kullaniciadi': 'Orkun'}

    return render_template('index.html', title='Web Projesi', user=user)
