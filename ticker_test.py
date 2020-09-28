from binance.client import Client
# import binance_api_key as bak 
import time
import json
api_key = "8SqwIw1lYhaxQZa9LSCUx2wjN1GqguDDAuewtKUCKmUlO4uwXoQ3ylz0EfspuPQd"
api_secret = "5Phlc0ldADa6rQYJANguTIe1mSekiSTN2SiaowBPcs2gXi3wsgQ2TCQssmo4BwX7"

from binance.websockets import BinanceSocketManager
 
def process_message(msg):
    msg_= msg['E'], msg['t'],msg['p'],msg["q"],msg["T"],msg["m"] #pre-processing
    msg_=json.dumps(msg_)
    with open("ticker.json", "a") as data:
        data.write(msg_)#,msg_['t'],msg_['p'],msg_["q"],msg_["T"],msg_["m"])
        data.close()
 
if __name__ == "__main__":
    BTC = 'BTCUSDT'
    start_time = time.time()
    client = Client(api_key, api_secret)
    bm = BinanceSocketManager(client)
    conn_key = bm.start_trade_socket(BTC, process_message)
    bm.start()
