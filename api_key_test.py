from binance.client import Client

api_key = "8SqwIw1lYhaxQZa9LSCUx2wjN1GqguDDAuewtKUCKmUlO4uwXoQ3ylz0EfspuPQd"
api_secret = "5Phlc0ldADa6rQYJANguTIe1mSekiSTN2SiaowBPcs2gXi3wsgQ2TCQssmo4BwX7"

if __name__ == "__main__":

    # this would result in verify: False and timeout: 5 for the get_all_orders call
    client = Client(api_key, api_secret, {"verify": False, "timeout": 20})
    status = client.get_system_status()
    # info = client.get_exchange_info()
    info = client.get_symbol_info('BNBBTC')
    print(info)