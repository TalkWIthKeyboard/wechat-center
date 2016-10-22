# coding=utf-8

import requests
import json
from config import TOKEN_URL
from datetime import datetime
from app.module.Token import Token


def getToken():
    '''
        获取token
    '''
    try:
        r = requests.get(TOKEN_URL)
        text = json.loads(str(r.text))

        dict = {}
        dict['token'] = str(text[u'access_token'])
        dict['expires_in'] = text[u'expires_in']
        dict['createTime'] = datetime.now()
        print dict
        Token(**dict).save()
    except Exception,e:
        print e.message

