from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	kullaniciadi = StringField("Kullanıcı Adı", validators=[DataRequired])
	sifre = PasswordField("Parola", validators=[DataRequired])
	benihatirla = BooleanField("Hatırla")	
	submit = SubmitField("Giris Yap")	
