from app import app
from app.models import Kullanici, Gonderi

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Kullanici': Kullanici, 'Gonderi': Gonderi}