from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    authorData = [
        {
            'author': {'username': 'Furkan',},
            'text': 'i was here'
        },
        {
            'author': {'username': 'Hasan'},
            'test': 'Yakarsa dunyayi garipler yakar'
        }
    ]
    user = {'username': 'Baran'}

    return render_template('index.html', 
                           title = 'Web Projesi', 
                           user = user, 
                           authorData = authorData)