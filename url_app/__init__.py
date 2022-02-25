from flask import Flask
from config import Config
import os

app1=Flask(__name__)
app1.config.from_object(Config)

from url_app import routes

