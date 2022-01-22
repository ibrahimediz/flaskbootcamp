import os
class Config(objecct):
    SECRET_KEY = os.getenv("SECRET_KEY") or "çipetpet"
    