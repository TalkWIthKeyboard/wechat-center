# coding=utf-8

WECHAT_TOKEN = 'sw77sw77sw77'


class Config(object):
    '''
    配置类
    '''
    MONGODB_SETTINGS = {
        'db': 'Gryffindor-test',
        'hosts': '127.0.0.1',
        'port': 27017
    }

    JOBS = [

        # 开启任务扫描(添加到任务列表)
        {
            'id': 'job1',
            'func': 'app.service.getToken:get_token',
            'args': (),
            'trigger': {
                'type': 'interval',
                'seconds': 7200
            }
        }
    ]
