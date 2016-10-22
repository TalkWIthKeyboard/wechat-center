# coding=utf-8

from flask import Flask
from flask_mongoengine import MongoEngine
from config import Config
from flask_apscheduler import APScheduler


app = Flask(__name__, static_url_path='')
app.config.from_object(Config())
app.secret_key = 'wechat-center'
db = MongoEngine(app)

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

# module
from app.module.Token import Token







