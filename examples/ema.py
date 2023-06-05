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

#Get latest price history
df = pd.DataFrame(get_price_history('BTCUSDT', '15', 24)['result'])

#Calc EMA
ema = indicators.ema(df['close'], 9)

#Print results of Calculations
print('--------------------------------------------')
print('EMA(9):', ema[-1])