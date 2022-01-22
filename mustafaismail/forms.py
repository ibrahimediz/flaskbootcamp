from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    kullaniciadi = StringField("Kullanıcı ADı", validators=[DataRequired()])
    sifre = PasswordField("Şifre", validators=[DataRequired()])
    beniHatirla = BooleanField("Beni Hatırla")
    submit = SubmitField("Giriş")

