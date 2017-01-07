# coding=utf-8

import time
from config import PIC_TEXT_REPLY_ITEM, PIC_TEXT_REPLY_HEADER, REPLY, ARTICLES


def reply_navigation(xml, output):
    '''
    回复导航框
    :param xml:微信过来的xml
    :return: 返回给用户的xml
    '''
    try:
        ToUserName = xml.find('ToUserName').text
        FromUserName = xml.find('FromUserName').text
        Content = xml.find('Content').text

        output.writelines('ToUserName:' + str(ToUserName))
        output.writelines('FromUserName:' + str(FromUserName))

        header = PIC_TEXT_REPLY_HEADER % (FromUserName, ToUserName, str(int(time.time())), str(3))
        item = ""
        item += PIC_TEXT_REPLY_ITEM % ('MovieBox | 记录你一生观影历程', '',
                                       'http://p3.music.126.net/zUE3L4oIPmoyuhdIO_v54w==/3234763210233939.jpg', '')
        item += PIC_TEXT_REPLY_ITEM % ('电影日历', '', '', 'moviebox.sw77.live/calendar')
        item += PIC_TEXT_REPLY_ITEM % ('电影记录', '', '', 'moviebox.sw77.live/movies')
        item += PIC_TEXT_REPLY_ITEM % ('朋友圈', '', '', 'moviebox.sw77.live/timeline')
        content = REPLY.format(header + ARTICLES.format(item))

        output.writelines('content:' + str(content))
        return content

    except Exception, e:
        output.writelines('error: ' + str(e.message))
