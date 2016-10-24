# coding=utf-8

from flask import request, make_response
import hashlib
import xml.etree.ElementTree as ET
from app import app
from config import WECHAT_TOKEN
from app.service.makeReply import reply_navigation

@app.route('/reply',methods=['GET','POST'])
def wechat_auth():
    '''
    GET 方法验证服务器的有效性
    POST 方法为用户发送的消息
    :return: 封装xml的response
    '''
    output = open('test.txt','w+')
    if request.method == 'GET':
        token = WECHAT_TOKEN
        query = request.args
        signature = query.get('signature', '')
        timestamp = query.get('timestamp', '')
        nonce = query.get('nonce', '')
        echostr = query.get('echostr', '')
        s = [timestamp,nonce,token]
        s.sort()
        s = ''.join(s)
        output.close()
        if (hashlib.sha1(s).hexdigest() == signature):
            return echostr
    else:
        xml_recv = ET.fromstring(request.data)
        # 现在默认所有消息都回复导航框
        content = reply_navigation(xml_recv,output)
        response = make_response(content)
        response.content_type = 'application/xml'
        output.close()
        return response




