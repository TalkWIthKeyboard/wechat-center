# coding=utf-8

REPLY = "<xml>{}</xml>"
ARTICLES = "<Articles>{}</Articles>"

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
                "<FuncFlag>0</FuncFlag>"