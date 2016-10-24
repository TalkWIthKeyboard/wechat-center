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
        content = replyUser(xml_recv,output)
        response = make_response(content)
        response.content_type = 'application/xml'
        output.close()
        return response


def replyUser(xml,output):
    '''
    解析xml文件,回复用户
    :param xml:微信过来的xml
    :return: 返回给用户的xml
    '''
    try:
        ToUserName = xml.find('ToUserName').text
        FromUserName = xml.find('FromUserName').text
        Content = xml.find('Content').text

        output.writelines('ToUserName:' + str(ToUserName))
        output.writelines('FromUserName:' + str(FromUserName))

        header = PIC_TEXT_REPLY_HEADER % (FromUserName, ToUserName, str(int(time.time())) , str(3))
        item = ""
        item += PIC_TEXT_REPLY_ITEM % ('MovieBox | 一个记录你一生观影历程的APP','',
                                      'http://p3.music.126.net/zUE3L4oIPmoyuhdIO_v54w==/3234763210233939.jpg','')
        item += PIC_TEXT_REPLY_ITEM % ('电影日历','','','')
        item += PIC_TEXT_REPLY_ITEM % ('电影推荐','','','')
        content = REPLY.format(header + Articles.format(item))

        output.writelines('content:' + str(content))
        return content

    except Exception,e:
        output.writelines('error: ' + str(e.message))




