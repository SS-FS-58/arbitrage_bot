import requests

from bitcoin_arbitrage.monitor.currency import CurrencyPair, FiatAmount
from bitcoin_arbitrage.monitor.exchange import Exchange, BTCAmount
from bitcoin_arbitrage.monitor.log import setup_logger
from bitcoin_arbitrage.monitor.order import Order, OrderState, OrderId

from binance.client import Client
from bitcoin_arbitrage.monitor.api_keys import BINANCE_API_KEY, BINANCE_SECRET_KEY

logger = setup_logger('Binance')


class Binance():
    def __init__(self, api_key: str=BINANCE_API_KEY, secret_key: str=BINANCE_SECRET_KEY, ):
        self.client = Client(api_key, secret_key)
        # self.fees = self.client.get_trade_fee()
    @property
    def name(self) -> str:
        return str(self.__class__.__name__)

    def update_prices(self) -> bool:
        print('updated prices of binance.')
        try:
            self.tickers = self.client.get_orderbook_tickers()
            # print('binance prices: ', self.tickers)
            return True
        except:
            return False
    def __str__(self):
        return f"{self.name}"
    
