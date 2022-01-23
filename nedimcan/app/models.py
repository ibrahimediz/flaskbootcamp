from app import db
from datetime import Datetime

class Kullanici(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kullanici_adi = db.Column(db.String(64), index=True, unique=True)
    eposta = db.Column(db.String(120), index=True, unique=True)
    sifre_hash = db.Column(db.String(128))
    gonderiler = db.relationship('Gonderi', backref='yazar', lazy='dynamic')

    def __repr__(self):
        return '<Kullanici {}>'.format(self.kullanici_adi)

class Gonderi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    yazi = db.Column(db.String(140))
    tarih = db.Column(db.Datetime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('kullanici.id'))

    def __repr__(self):
        return '<Gonderi {}>'.format(self.yazi)