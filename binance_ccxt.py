import ccxt
from datetime import datetime

# api_key = "Q4Mu8mTjZgXxry8YEZnNdxUwmHs9NEUioesjaxCErqMqK2zMZL3VmrFf9IKONFBI"
# api_secret = "sVoJtkq6Wr5sjnLKam5g58l4tRu0NtEYVWNWtJz9PkL2ZYkvSkBmhNnCAZMIj3eq"

api_secret = "6c3e1213f188986ea22606f0b8a7cd09b6e3db047eafe4003bdafa0ef393a530"
api_key = "079351a2e33673248f1c2e4b4a8f30b65819e4d3461eca0de8722c4105d56220"



# binance = ccxt.binance()
binance = ccxt.binance({
    'apiKey': api_key,
    'secret': api_secret,
})

markets = binance.fetch_tickers()
# print(markets.keys())
ticker = binance.fetch_ticker('ETH/BTC')
print(ticker['open'], ticker['high'], ticker['low'], ticker['close'])
ohlcvs = binance.fetch_ohlcv('ETH/BTC')
# for ohlc in ohlcvs:
#   print(datetime.fromtimestamp(ohlc[0]/1000).strftime('%Y-%m-%d %H:%M:%S'))

orderbook = binance.fetch_order_book('ETH/BTC')
# print(orderbook['bids'])
# print(orderbook['asks'])
# for ask in orderbook['asks']:
#   print(ask[0], ask[1])
try:
  balance = binance.fetch_balance()
  print(balance.keys())
except Exception as e:
  print('api error: ', e)


# print(ohlcvs)

