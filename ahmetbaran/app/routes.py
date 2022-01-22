from app import app
from flask import render_template


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
            'test': 'Yakarsa dunyayi garipler yakar'
        }
    ]
    user = {'username': 'Baran'}

    return render_template('index.html', 
                           title = 'Web Projesi', 
                           user = user, 
                           authorInfo = authorInfo
                           )

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