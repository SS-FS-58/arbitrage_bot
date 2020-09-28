from binance.client import Client
from pprint import pprint as p

api_key = "8SqwIw1lYhaxQZa9LSCUx2wjN1GqguDDAuewtKUCKmUlO4uwXoQ3ylz0EfspuPQd"
api_secret = "5Phlc0ldADa6rQYJANguTIe1mSekiSTN2SiaowBPcs2gXi3wsgQ2TCQssmo4BwX7"

if __name__ == "__main__":
    # this would result in verify: False and timeout: 5 for the get_all_orders call
    client = Client(api_key, api_secret, {"verify": False, "timeout": 20})
    status = client.get_system_status()
    # info = client.get_exchange_info()
    # info = client.get_symbol_info('BNBBTC')
    # # trades = client.get_historical_trades(symbol='BNBBTC')
    # trades = client.get_aggregate_trades(symbol='BNBBTC')
    # prices = client.get_all_tickers()
    klines = client.get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_1MINUTE, "10 minute ago UTC")
    # [
    #     [
    #         1499040000000,      // Open time
    #         "0.01634790",       // Open
    #         "0.80000000",       // High
    #         "0.01575800",       // Low
    #         "0.01577100",       // Close
    #         "148976.11427815",  // Volume
    #         1499644799999,      // Close time
    #         "2434.19055334",    // Quote asset volume
    #         308,                // Number of trades
    #         "1756.87402397",    // Taker buy base asset volume
    #         "28.46694368",      // Taker buy quote asset volume
    #         "17928899.62484339" // Ignore
    #     ]
    # ]


    p(klines)

    print(status)
    # print(client.ping())