from flask import Flask

app = Flask(__name__)

app.secret_key = "Asparkitrighthere"
DATABASE = "dojos_ninjas_db"