import os

class Config(object):
    SECRET_KEY = os.getenv("SECRET_KEY") or "is-this-really-secret?"