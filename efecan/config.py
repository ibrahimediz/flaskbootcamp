import os
class Config(object):
    SECRET_KEY = os.getenv("SECRET_KEY") or  "Biri ne mi baktın baba yiğit"