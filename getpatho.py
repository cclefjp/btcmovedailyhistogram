''' getpatho.py - UTHのpatho reportを取得するスクリプト '''

import logging
import json
from time import sleep
from random import randint
from retrievehtml import RetrieveHTML
from exception import NetworkError, NotFoundError

__author__ = 'Takeyuki Watadani<watadat-tky@umin.ac.jp'
__date__ = '2021/8/5'
__version__ = '0.2'
__status__ = 'development'

# ロギングの設定
logger = logging.getLogger('getpatho')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())
logger.info('getpatho.pyを開始')

# constants.jsonを読み込む
constpath = './constants.json'
with open(constpath, mode='r') as constfp:
    constdict = json.load(constfp)

# config.jsonを読み込む
configpath = './config.json'
with open(configpath, mode='r') as configfp:
    configdict = json.load(configfp)

codekey = 'pathocode'
assert codekey in configdict
pathocode = configdict[codekey]

logger.info('pathocode = ' + str(pathocode))

# 取得関数オブジェクトを生成
retrievefunc = RetrieveHTML(constdict, configdict, logger)

# 実際の取得を行う
if isinstance(pathocode, str):
    retrievefunc(pathocode)
elif isinstance(pathocode, list):
    length = len(pathocode)
    for i, code in enumerate(pathocode):
        try:
            retrievefunc(code)
        except NetworkError:
            logger.warning(code + 'の取得中にNetworkErrorが発生しました。')
        except NotFoundError:
            logger.warning(code + 'は見つかりませんでした。')

        # logger.info('i = ' + str(i) + ', length=' + str(length))
        if i < length - 1:
            sleeptime = randint(25, 35)
            logger.info('サーバー負荷軽減のため' + str(sleeptime) + '秒スリープします。')
            sleep(sleeptime)
else:
    logger.warning('pathocodeがstrでもlistでもないので取得を行いません。')

# 終了
logger.info('getpathoを終了します。')
