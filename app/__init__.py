import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Caminho absoluto para o banco
basedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "storage.db")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:////{basedir}"
api = Api(app)
db = SQLAlchemy(app)
CORS(app)

