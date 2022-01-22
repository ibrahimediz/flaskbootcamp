from app import app
from flask import render_template
from app.forms import LoginForm

@app.route('/')
@app.route('/index')

def index():
    authorInfo = [
        {
            'author': {'username': 'Baran'},
            'text': 'I believe i can fly'
        },
        {
            'author': {'username': 'Hasan'},
            'test': 'Allahim sil beni listeden :) Amin :)'
        }
    ]
    
    user = {'username': 'Baran'}

    return render_template('index.html', 
                           title = 'Web Projesi', 
                           user = user, 
                           authorInfo = authorInfo
                           )

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title="Login", form=form)

    # return f'''
    # <html>
    #     <head>
    #         <title>Homepage</title>
    #     </head>

    #     <body>
    #         <h1>Merhaba {user["username"]}</h1>
    #     </body>
    # </html>
    # '''