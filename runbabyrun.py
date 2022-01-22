import subprocess
liste = ["ilhanmert","canersoy","efecan",
"mustafaismail","ayseberna","enes",
"hasan","ege","nedimcan","ahmetbaran",
"fahrettinorkun","celalbugra","onur","musa",
"alibaris","ardacem","irem","seyit","bilal",
"abdullah","ali","furkan","fatihcan"]
import random as rnd

print(rnd.choice(liste))
# # subprocess.run(komut,shell=True)
# # subprocess.run(f"flask run --port=500{rnd.randint(0,10)}",shell=True,check=True,)
# 5001

"""
host – the hostname to listen on.
port – the port of the web server.
debug – if given, enable or disable debug mode.
load_dotenv – load the nearest .env and .flaskenv files to set environment variables.
use_reloader – should the server automatically restart the python process if modules were changed?
use_debugger – should the werkzeug debugging system be used?
use_evalex – should the exception evaluation feature be enabled?
extra_files – a list of files the reloader should watch additionally to the modules.
reloader_interval – the interval for the reloader in seconds.
reloader_type – the type of reloader to use.
threaded – should the process handle each request in a separate thread?
processes – if greater than 1 then handle each request in a new process up to this maximum number of concurrent processes.
passthrough_errors – set this to True to disable the error catching.
ssl_context – an SSL context for the connection.
"""