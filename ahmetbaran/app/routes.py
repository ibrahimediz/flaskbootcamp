from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

# flash ekrana bilgi basmak icin. nerden ne geldi 

@app.route('/')
@app.route('/home')
def index():
    authorInfo = [
        {
            'author': {'username': 'Baran'},
            'text': 'I believe i can fly'
        },
        {
            'author': {'username': 'Hasan'},
            'text': 'Allahim sil beni listeden :) Amin :)'
        }
    ]
    
    user = {'username': 'Baran'}

    return render_template('index.html', 
                           title = 'Web Projesi', 
                           user = user, 
                           authorInfo = authorInfo
                           )

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.rememberMe.data))        
        return redirect(url_for('index'))
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