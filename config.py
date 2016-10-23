# coding=utf-8

TOKEN_URL = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx392c85aff8aaccd4&secret=d208004e64eee56ee940c18e5a0989c3'
WECHAT_TOKEN = 'sw77sw77sw77'

class Config(object):

    JOBS=[

        # 开启自动获取token的任务
        {
            'id' : 'job1',
            'func' : 'app.service.token:getToken',
            'args' : (),
            'trigger' : {
                'type' : 'interval',
                'minutes' : 30
            }
        }

    ]

    MONGODB_SETTINGS={
        'db':'wechat-center',
        'hosts':'127.0.0.1',
        'port':27017
    }

