import pandas as pd
from datetime import datetime, timedelta
import ccxt

mex = ccxt.bitmex()

start_date = datetime(year=2018,month=1,day=1)
end_date = datetime(year=2018,month=12,day=31)

data = []
while start_date < end_date:
    candles = mex.fetch_ohlcv('BTC/USD', '1h', since=start_date.timestamp()*1000, limit=500)
    data += candles
    start_date += timedelta(hours=len(candles))

df = pd.DataFrame(data=data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
df['timestamp'] /= 1000
df.set_index('timestamp', drop=True, inplace=True)
df.to_csv('data/historical_candles.csv')
