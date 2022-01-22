from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, Submitfield
from wtforms.validators import DataRequired

class Loginform(FlaskFrom):
    kullaniciadi = StringField("Kullanıcı adı",validators=[DataRequired()])
    sifre = PasswordField()("Şifre",validators=[DataRequired()])
    benihatirla = BooleanField("Beni hatırla")
    submit = Submitfield("Giriş")