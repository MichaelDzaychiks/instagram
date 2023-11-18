from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_session import Session
from flask_login import LoginManager
from flask_cors import CORS
from dotenv import load_dotenv
import os
from datetime import timedelta

load_dotenv()

app = Flask(__name__, template_folder = "views")
app.config["SECRET_KEY"] = "SECRET" #os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] ="sqlite:///data.db" #os.getenv("DB_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=30)
app.config['RECAPTCHA_PUBLIC_KEY'] = 'your_public_key'
app.config['RECAPTCHA_PRIVATE_KEY'] = 'your_private_key'


# Session(app)
db = SQLAlchemy(app) 
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"
cors = CORS(app)

class Config:
    SECRET_KEY = 'your_secret_key'
    RECAPTCHA_PUBLIC_KEY = os.getenv('RECAPTCHA_PUBLIC_KEY', '12345678')
    RECAPTCHA_PRIVATE_KEY = os.getenv('RECAPTCHA_PRIVATE_KEY', '123456789')

from application.routes import *
from application.models import *