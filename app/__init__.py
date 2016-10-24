# coding=utf-8

from flask import Flask
from flask_mongoengine import MongoEngine
from config import Config

app = Flask(__name__, static_url_path='')
app.config.from_object(Config())
app.secret_key = 'wechat-center'
db = MongoEngine(app)

# module
from app.module.Token import Token

# routes
from app.routes import wechatReply



