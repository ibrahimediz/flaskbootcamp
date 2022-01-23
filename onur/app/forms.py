from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    kullaniciadi = StringField("Kullanıcı Adı", validators=[DataRequired()])
    sifre = PasswordField("Şifre", validators=[DataRequired()])
    benihatirla = BooleanField("Beni Hatırla")
    submit = SubmitField("Giriş")