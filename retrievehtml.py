''' retrievehtml.py - pathoreportのHTMLを取得する関数を記述 '''

import requests
import os.path
from exception import NetworkError, NotFoundError

class RetrieveHTML:
    '''
    pathoreportのHTMLを取得する関数型オブジェクト
    '''

    # class variables
    _baseurl = 'BaseURL'
    _bodyquerykey = 'BodyQueryKey'
    _notfoundkey = 'NotFoundSentence'

    def __init__(self, constantdict: dict, configdict: dict, logger):
        self.__constantdict = constantdict
        self.__configdict = configdict
        self.__logger = logger

    def __call__(self, pathocode: str):
        '''
        pathocodeで指定されるpathoreportのHTMLを取得する
        '''
        assert RetrieveHTML._baseurl in self.__constantdict
        baseurl = self.__constantdict[RetrieveHTML._baseurl]

        # self.__logger.info('baseurl = ' + baseurl)

        assert RetrieveHTML._bodyquerykey in self.__constantdict
        bodyquerykey = self.__constantdict[RetrieveHTML._bodyquerykey]

        # POSTデータの構築
        body = {
            bodyquerykey: pathocode
        }

        # requestsによる取得
        response = requests.post(baseurl, data=body)

        # HTTP return codeの確認
        if not response.status_code == 200:
            self.__logger.warning("HTTPステータスコードが正常ではありません。status = " + str(response.status_code))
            self.__logger.warning(response.text)
            raise NetworkError()

        # patho reportが存在するかしないかのチェック
        assert RetrieveHTML._notfoundkey in self.__constantdict
        notfoundsentence = self.__constantdict[RetrieveHTML._notfoundkey]
        if notfoundsentence in response.text:
            raise NotFoundError(pathocode + 'は見つかりませんでした。')

        # 結果の出力
        outfile  = os.path.join(self.__configdict['resultpath'], pathocode + '.html')
        with open(outfile, mode='w') as outfp:
            outfp.write(response.text)
            self.__logger.info(pathocode + 'のレポート保存が正常に終了しました。')

        return



