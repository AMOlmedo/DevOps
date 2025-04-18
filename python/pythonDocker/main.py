#save this as app.py. Es un simple servidor que inicia el server web
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World DataCloud!!!  v2"

app.run(host="0.0.0.0") #este puerrto default de la instancia en docker