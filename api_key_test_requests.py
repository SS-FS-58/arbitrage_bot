import requests
import pprint
 
ep='https://api.binance.com'
ping='/api/v1/ping'
ticker24h='/api/v1/ticker/24hr'
params = {'symbol': 'BTCUSDT'}
 
r1=requests.get(ep+ping)
r2 = requests.get(ep+ticker24h, params=params) #use parameter
pprint.pprint(r1.json())
pprint.pprint(r2.json())
