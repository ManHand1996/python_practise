import os.path
import logging
from logging import config
from logpack import api
import yaml


"""
由上以下 严重程度递增`
DEBUG: 开发调试信息 [正常]
INFO: 预期发生的信息 [正常]
WARNING: 不是经常发生的, 不是预期发生的， 若磁盘满了 [能运行]
ERROR: 程序某部分功能出错，不能正确返回预期结果 [部分功能有问题]
CIRTICAL: 最严重的级别 [程序不能运行]

注: level为NOTSET则不获取debug和info的信息 

日志记录机制:
logger(对象): 设置记录级别level
    多个handler(对象): 设置使用哪种handler(FileHandler StreamHanderl ect.), level
        每个handler有一个formatter(对象): 日志输出格式
        
三种形式创建logger
1.代码创建
2.配置文件logging.conf (无Filter功能), 一定要配置logger.root
3.字典dict, 
"""

# 1.代码创建
# logging.basicConfig(filename='./test.log', 
#                     level=logging.DEBUG,
#                     format='%(asctime)s %(name)s %(message)s')
# logger = logging.getLogger(name='mylogger')
# logger.setLevel(logging.DEBUG)
# fmt = logging.Formatter(fmt='%(asctime)s %(name)s %(levelname)s %(message)s')
# handler = logging.FileHandler(filename='./test.log')
# handler.setFormatter(fmt)
# handler.setLevel(logging.ERROR)
# console_handler = logging.StreamHandler()
# console_handler.setFormatter(fmt)
# console_handler.setLevel(logging.DEBUG)
# logger.addHandler(handler)
# logger.addHandler(console_handler)


# 2.fileConfig
# config.fileConfig("./logging.conf")


# 3.字典创建

def log_with_dict():
    
    dict_conf = {
        'version': 1,
        # 'root':{
        #     'level': logging.NOTSET,
        #     'handlers': ['streamhandler']
        # },
        'loggers':{
            'mylogger':{
                'level': logging.DEBUG,
                'handlers': ['streamhandler', 'filehandler'],
                'propagate': 0
            }  
        },
        'formatters':{
            'myfm': {
                'format': '%(asctime)s [%(levelname)s] %(name)s %(lineno)s %(message)s'
            }
        },
        'filters':{},
        'handlers':{
            'streamhandler':{
                # 类名和一些参数需要为字符串
                'class': 'logging.StreamHandler',
                'level': logging.DEBUG,
                'formatter': 'myfm'
                # 'stream': 'sys.stdout'
            },
            'filehandler':{
                'class': 'logging.FileHandler',
                'level': logging.ERROR,
                'formatter': 'myfm',
                'filename': './test.log',
                'mode': 'a'
            }
        }
    }

    config.dictConfig(dict_conf)
    print(yaml.dump(dict_conf,sort_keys=False))

    logger = logging.getLogger('mylogger')
    logger.debug('debug ...all')
    logger.info('info ...all')
    logger.warning('warning ...all')
    logger.error('error ...all')
    logger.critical('critical ...all')
# api.api_log()
# logging.info('hello fork')