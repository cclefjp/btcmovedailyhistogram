
# from internal
from unixtime import currentunixtime, agounixtime

# from the standard library
import json

# from external libraries
import requests
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats

# URL
URL = 'https://ftx.com/api/futures/BTC-PERP/mark_candles'

##### ここからメイン処理

# FTXから日足のBTC-PERP価格を取得する

t0 = agounixtime(days=365*3)
t1 = currentunixtime()

getparam = {
    'index_name': 'BTC-PERP',
    'resolution': 86400, # 日足なので60 x 60 x 24 = 14400秒
    'start_time': t0,
    'end_time': t1
}

response = requests.get(url=URL, params=getparam)

assert response.status_code == 200

rdict = json.loads(response.text)

# print(rdict)

count = 0
tmparr = []
for elem in rdict['result']:
    close = elem['close']
    open = elem['open']
    val = close-open
    tmparr.append(val)
    count += 1

print(count) 

nparr = np.asarray(tmparr, dtype=np.float64)

# 正規分布に従うかどうかの検定 シャピロ・ウィルク
sw = stats.shapiro(nparr)
print('sw=', sw)

plt.hist(nparr, bins=50)
plt.show()


