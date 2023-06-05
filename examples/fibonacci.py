from tradingindicators import indicators
from datetime import datetime
import calendar
import pandas as pd
import requests

#Get latest prices
def get_price_history(symbol, tick_interval, timeframe_in_h):
    now = datetime.utcnow()
    unixtime = calendar.timegm(now.utctimetuple())
    since = unixtime
    start=str(since-60*60*timeframe_in_h)    
    
    url = 'https://api.bybit.com/public/linear/kline?symbol='+symbol+'&interval='+tick_interval+'&from='+str(start)
    
    data = requests.get(url).json()
    return data

#Get latest candle high and low
df = pd.DataFrame(get_price_history('BTCUSDT', '15', 24)['result'])
high = df['high'][len(df['high'])-1]
low = df['low'][len(df['low'])-1]

retracement_levels = [0, 0.236, 0.382, 0.5, 0.618, 0.764, 1, 1.382]
extension_levels = [2.618, 2, 1.618, 1.382, 1, 0.618]

uptrend = True

fibonacci_retracement = indicators.fibonacci_retracement(high, low, retracement_levels, uptrend)
fibonacci_extension = indicators.fibonacci_extension(high, low, extension_levels, uptrend)

#Print results of Calculations
print("--------------Retracement Levels--------------")
for i in range(len(fibonacci_retracement)):
    print(retracement_levels[i], ": ", fibonacci_retracement[i])

print("--------------Extension Levels--------------")
for i in range(len(fibonacci_extension)):
    print(extension_levels[i], ": ", fibonacci_extension[i])