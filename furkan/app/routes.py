from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Furkan'}

    return '''
    <html>
        <head>
            <title>Homepage</title>
        </head>

        <body>
            <p>Merhaba {user[]}</p>
        </body>
    '''