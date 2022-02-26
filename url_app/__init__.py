from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app1=Flask(__name__)
db=SQLAlchemy(app1)
migrate=Migrate(app1,db)
app1.config.from_object(Config)

from url_app import routes, models
