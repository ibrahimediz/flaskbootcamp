from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginFrom(FlaskForm):
    kullaniciAdi = StringField("Kullanıcı Adı", validators=[DataRequired()])
    sifre = PasswordField("Şifre", validators=[DataRequired()])
    beniHatirla = BooleanField("Beni Hatırla")        
    submit = SubmitField("Giriş")