''' getpatho.py - UTHのpatho reportを取得するスクリプト '''

import requests

import logging
import json

__author__ = 'Takeyuki Watadani<watadat-tky@umin.ac.jp'
__date__ = '2021/8/5'
__version__ = '0.1'
__status__ = 'development'

# ロギングの設定
logger = logging.getLogger('getpatho')
logger.setLevel(logging.DEBUG)
logger.info('getpatho.pyを開始')

# constants.jsonを読み込む
constpath = './constants.json'
with open(constpath, mode='r') as constfp:
    constdict = json.load(constfp)

baseurl = 'BaseURL'
assert baseurl in constdict
baseurl = constdict[baseurl]

logger.info('baseurl = ' + baseurl)

# config.jsonを読み込む
configpath = './config.json'
with open(configpath, mode='r') as configfp:
    configdict = json.load(configfp)

codekey = 'pathocode'
assert codekey in configdict
pathocode = configdict[codekey]

logger.info('pathocode = ' + pathocode)

# POSTデータの構築
body = {
    "sid": pathocode
}

# requestsによる取得
response = requests.post(baseurl, data=body)

# 結果の出力
print(response.text)

