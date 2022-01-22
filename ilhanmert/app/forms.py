from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    kAdi=StringField("Kullanıcı Adı: ", validators=[DataRequired()])
    sifre=PasswordField("Sifre",validators=[DataRequired()])
    rememberMe=BooleanField("Remember Me")
    submit=SubmitField("Giriş")