# coding=utf-8

import time
from flask import request, make_response
import hashlib
import xml.etree.ElementTree as ET
from app import app
from config import WECHAT_TOKEN

REPLY = "<xml>{}</xml>"
Articles = "<Articles>{}</Articles>"

PIC_TEXT_REPLY_HEADER =  "<ToUserName><![CDATA[%s]]></ToUserName> "\
                            "<FromUserName><![CDATA[%s]]></FromUserName> " \
                            "<CreateTime>%s</CreateTime> " \
                            "<MsgType><![CDATA[news]]></MsgType>" \
                            "<ArticleCount>%s</ArticleCount>"

PIC_TEXT_REPLY_ITEM = "<item>" \
                        "<Title><![CDATA[%s]]></Title>" \
                        "<Description><![CDATA[%s]]></Description>" \
                        "<PicUrl><![CDATA[%s]]></PicUrl>" \
                        "<Url><![CDATA[%s]]></Url>" \
                        "</item>"

TEXT_REPLY =   "<ToUserName><![CDATA[%s]]></ToUserName>" \
                "<FromUserName><![CDATA[%s]]></FromUserName>" \
                "<CreateTime>%s</CreateTime>" \
                "<MsgType><![CDATA[text]]></MsgType>" \
                "<Content><![CDATA[%s]]></Content>" \
                "<FuncFlag>0</FuncFlag>" \


@app.route('/reply',methods=['GET','POST'])
def wechat_auth():
    '''
    GET 方法验证服务器的有效性
    POST 方法为用户发送的消息
    :return: 封装xml的response
    '''
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
        if (hashlib.sha1(s).hexdigest() == signature):
            return echostr
    else:
        xml_recv = ET.fromstring(request.data)
        content = replyUser(xml_recv)
        response = make_response(content)
        response.content_type = 'application/xml'
        return response


def replyUser(xml):
    '''
    解析xml文件,回复用户
    :param xml:微信过来的xml
    :return: 返回给用户的xml
    '''
    ToUserName = xml.find('ToUserName').text
    FromUserName = xml.find('FromUserName').text
    Content = xml.find('Content').text

    if Content == u'功能':
        header = PIC_TEXT_REPLY_HEADER % (FromUserName, ToUserName, int(time.time()) , 1)
        item = PIC_TEXT_REPLY_ITEM % ('山塘街',
                                      '山塘街东起阊门渡僧桥，西至苏州名胜虎丘山的望山桥，长约七里，所以苏州俗语说“七里山塘到虎丘”...',
                                      'http://thinkshare.duapp.com/images/suzhou.jpg',
                                      'http://mp.weixin.qq.com/mp/appmsg/show?__biz=MjM5NDM0NTEyMg==&appmsgid=10000046&itemidx=1&sign=9e7707d5615907d483df33ee449b378d#wechat_redirect')
        content = REPLY.format(header + Articles.format(item))

    print content
    return content


