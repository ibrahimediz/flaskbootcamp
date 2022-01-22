from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    kullaniciadi = StringField("Kullanici Adi", validators=[DataRequired()])
    sifre = PasswordField("Sifre", validators=[DataRequired()])
    benihatirla = BooleanField("Beni Hatirla")
    submit = SubmitField("Giris")