''' exception.py - getpatho用の例外を記載する '''

class NetworkError(Exception):
    '''
    ネットワークエラー用の例外
    '''

    def __init__(self, message):
        super(NetworkError, self).__init__(message)
        return

class NotFoundError(Exception):
    '''
    pathoreportが見つからなかった時の例外
    '''

    def __init__(self, message):
        super(NotFoundError, self).__init__(message)
        return