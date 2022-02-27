from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app1=Flask(__name__)
app1.config.from_object(Config)
db=SQLAlchemy(app1)
migrate=Migrate(app1,db)

from url_app import routes, models
