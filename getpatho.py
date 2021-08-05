''' getpatho.py - UTHのpatho reportを取得するスクリプト '''

import requests

import logging
import json
import os.path
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

baseurl = 'BaseURL'
assert baseurl in constdict
baseurl = constdict[baseurl]

assert "BodyQueryKey" in constdict
bodyquerykey = constdict['BodyQueryKey']

logger.info('baseurl = ' + baseurl)

notfoundsentence = constdict['NotFoundSentence']

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
    bodyquerykey: pathocode
}

# requestsによる取得
response = requests.post(baseurl, data=body)

# HTTP return codeの確認
if not response.status_code == 200:
    logger.warning("HTTPステータスコードが正常ではありません。status = " + str(response.status_code))
    logger.warning(response.text)
    raise NetworkError()

# patho reportが存在するかしないかのチェック
if notfoundsentence in response.text:
    raise NotFoundError(pathocode + 'は見つかりませんでした。')

# 結果の出力
outfile  = os.path.join(configdict['resultpath'], pathocode + '.html')
with open(outfile, mode='w') as outfp:
    outfp.write(response.text)
    logger.info(pathocode + 'のレポート保存が正常に終了しました。')

# 終了
logger.info('getpathoを終了します。')
