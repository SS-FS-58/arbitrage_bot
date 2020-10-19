from bitcoin_arbitrage.monitor import settings
from bitcoin_arbitrage.monitor.exchange import Exchange
from bitcoin_arbitrage.monitor.log import setup_logger
from bitcoin_arbitrage.monitor.spread_detection import SpreadABC

logger = setup_logger('Spread')


class Tri_SpreadDifferentCurrenciesError(Exception):
    pass


class Tri_SpreadMissingPriceError(Exception):
    pass


class Tri_Spread(SpreadABC):
    def __init__(self, exchange: Exchange, currenciesList: list) -> None:
        self.exchange = exchange
        self.currenciesList = currenciesList
        self.spread = self._calculate_spread()
        

    # def __str__(self) -> str:
    #     return self.summary

    # def __repr__(self) -> str:
    #     return self.__str__()

    @property
    def summary(self) -> str:
        return f'Tri_Spread: {self.spread_with_currency}'

    @property
    def spread_with_currency(self) -> str:
        return f'{self.spread}'

    @property
    def spread_percentage(self):
        return self.spread

    def _calculate_spread(self) -> int:
        exch_rate_list = []
        client = self.exchange.client
        sym = self.currenciesList[0]
        currency_pair = "Currency Pair: "+str(sym)+" "
        print(currency_pair)
        depth = client.get_order_book(symbol=sym)
        price1 = float(depth['bids'][0][0])
        print('---price1 : {}'.format(price1))
        exch_rate_list.append(price1)

        sym = self.currenciesList[1]
        currency_pair = "Currency Pair: "+str(sym)+" "
        print(currency_pair)
        try:
            depth = client.get_order_book(symbol=sym)
            price2 = float(depth['asks'][0][0])
            price2 = 1/price2
            print('---price2 : {}'.format(price2))
            print('---price2 based on fee : {}'.format(price2))
            exch_rate_list.append(price2)
        except Exception as e:
            print(e)
            print('error order book: ', sym)
            price2 = 0.000000001
            print('---price2 based on fee : {}'.format(price2))
            exch_rate_list.append(price2)  

        sym = self.currenciesList[2]
        currency_pair = "Currency Pair: "+str(sym)+" "
        print(currency_pair)
        depth = client.get_order_book(symbol=sym)
        price3 = float(depth['bids'][0][0])
        print('---price3 based on fee : {}'.format(price3))
        exch_rate_list.append(price3)

        rate1 = exch_rate_list[0]
        buy_price = "Buy: {}".format(rate1)
        print(buy_price)
        rate2 = price3 * price2
        sell_price = "Sell: {}".format(rate2)
        print(sell_price)
        if float(rate1)<float(rate2):
            print('Detecting the opportunities for triangular arbitrage trading.', self.currenciesList)
        else:
            print("No Arbitrage Possibility")

        return float(rate1) - float(rate2)

    # def is_above_trading_thresehold(self) -> bool:
    #     return self.spread > settings.MINIMUM_SPREAD_TRADING
