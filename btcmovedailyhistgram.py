
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
largecount = 0

for elem in rdict['result']:
    close = elem['close']
    open = elem['open']
    high = elem['high']
    low = elem['low']
    
    # val = close-open # 1日の変動量、符号あり
    val = abs(close-open) # 1日の変動量、絶対値
    # val = max(abs(low-open), abs(high-open)) # 1日の最大変動量、絶対値
    val /= open # 相対値
    # if val > 3000:
    if val > 0.10: # 10%以上
        largecount += 1
    tmparr.append(val)
    count += 1

print(count) 

nparr = np.asarray(tmparr, dtype=np.float64)

# 正規分布に従うかどうかの検定 シャピロ・ウィルク
sw = stats.shapiro(nparr)
print('sw=', sw)

# print('3000以上動いた日数:', largecount)
print('10%以上動いた日数:', largecount)

plt.hist(nparr, bins=50)
plt.show()


