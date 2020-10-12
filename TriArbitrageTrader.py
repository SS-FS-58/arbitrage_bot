# from api import BinanceAPI
# import ccxt
from binance.client import Client
# from binance.enums import *
from api_key import API_KEY, SECRET_KEY
# binance = ccxt.binance()
client = Client(API_KEY, SECRET_KEY)
print(client)
import time
from datetime import datetime
import math
import pprint
import matplotlib.pyplot as plt
import json

def run():
    while 1:
        try:
            initialize_arb()
        except:
            print("Restarting\n\n")
    pass

def initialize_arb():

    bot_start_time = str(datetime.now())
    welcome_message = "\nBot Start Time: {}\n\n\n".format(bot_start_time)
    print(welcome_message)
    # info = client.get_exchange_info()
    # print(info)
    data_log_to_file(welcome_message)
    try:
        
        #Find Arbitrage Opportunities
        tickers = client.get_orderbook_tickers()
        # print('All Book Tickers : ', tickers)
        #Collect all Symbols for Exchange
        # list_of_symbols = list(sym['symbol'] for sym in tickers)
        # print('all Symbols for Exchange', list_of_symbols)

        list_of_arb_sym = []
        list_of_arb_sym.append(['BNBBTC', 'ADABNB', 'ADABTC'])
        list_of_arb_sym.append(['BNBBTC', 'ANTBNB', 'ANTBTC'])
        list_of_arb_sym.append(['BNBBTC', 'ATOMBNB', 'ATOMBTC'])
        list_of_arb_sym.append(['BNBBTC', 'AVABNB', 'AVABTC'])
        list_of_arb_sym.append(['BNBBTC', 'AVAXBNB', 'AVAXBTC'])

        # fees = client.get_trade_fee()

        while True:
            # Run Arbitrage Profit Functionality - To Determine Highest Profit Percentage - Cont Loop
            calc_profit_list =[]
            exp_profit = 0      #Expected Profit, Set to 0 initially
            m=0
            for i in range(0,2):
                if exp_profit>0:
                    break
                n = 0 #Market Position Market (m) & counter (n)
                for arb_market in list_of_arb_sym:
                    calc_profit_list.append(arbitrage_bin(arb_market, tickers, fees, 1, 1))
                #print(calc_profit_list)
                for exch_market in calc_profit_list:
                    if exch_market[4]>exp_profit:
                        exp_profit = exch_market[4]
                        m = n
                    n+=1
           
            print(m)
            exp_profitx = float("%0.3f" % (exp_profit))
            if m>4:
                m-=4
            profit_message = "\nMost Profitable Market: {} \nExpected Profit: {}%".format(list_of_arb_sym[m], exp_profitx)
            print(profit_message)
            data_log_to_file(profit_message)
    except Exception as e:
        print(e)
        print("\nFAILURE INITIALIZE\n")
        raise

def data_log_to_file(message):
    with open('CryptoTriArbBot_DataLog.txt', 'a+') as f:
        f.write(message)

def get_maker_fee(fees, sym):
    for fee in fees['tradeFee']:
        if fee['symbol'] == sym:
            return float(fee['maker'])
    return 0

def get_taker_fee(fees, sym):
    for fee in fees['tradeFee']:
        if fee['symbol'] == sym:
            return float(fee['taker'])
    return 0    
def arbitrage_bin(list_of_sym, tickers, fees, cycle_num=1, cycle_time=30):
    #Create Triangular Arbitrage Function
    arb_message = "Binance Arbitrage Function Data Collection - Running\n"
    print(arb_message)
    data_log_to_file(arb_message)
    for i in range(0,1):    #initialize Exchange
        print("List of Arbitrage Symbols:", list_of_sym)
        for k in range(0,cycle_num):
            i=0
            exch_rate_list = []
            data_collect_message1 = "Data Collection Cycle Number: "+str(k) +'\n'
            print(data_collect_message1)
            data_log_to_file(data_collect_message1)

            sym = list_of_sym[0]
            currency_pair = "Currency Pair: "+str(sym)+" "
            print(currency_pair)
            depth = client.get_order_book(symbol=sym)
            price1 = float(depth['bids'][0][0])
            print('---price1 : {}'.format(price1))
            # get taker fee.
            # fees = client.get_trade_fee(symbol=sym, recvWindow = 3000)
            taker_fee = get_taker_fee(fees, sym)
            print('---taker fee : {}'.format(taker_fee))
            price1 *= (1 - taker_fee)
            print('---price1 based on fee : {}'.format(price1))
            exch_rate_list.append(price1)
            

            sym = list_of_sym[1]
            currency_pair = "Currency Pair: "+str(sym)+" "
            print(currency_pair)
            try:
                depth = client.get_order_book(symbol=sym)
                price2 = float(depth['asks'][0][0])
                price2 = 1/price2
                print('---price2 : {}'.format(price2))
                taker_fee = get_taker_fee(fees, sym)
                print('---taker fee : {}'.format(taker_fee))
                price2 *= (1 - taker_fee)
                print('---price2 based on fee : {}'.format(price2))
                exch_rate_list.append(price2)
            except Exception as e:
                print(e)
                print('error order book: ', sym)
                price2 = 0.000000001
                print('---price2 based on fee : {}'.format(price2))
                exch_rate_list.append(price2)  

            sym = list_of_sym[2]
            currency_pair = "Currency Pair: "+str(sym)+" "
            print(currency_pair)
            depth = client.get_order_book(symbol=sym)
            price3 = float(depth['bids'][0][0])
            print('---price3 : {}'.format(price3))
            taker_fee = get_taker_fee(fees, sym)
            print('---taker fee : {}'.format(taker_fee))
            price3 *= (1 - taker_fee)
            print('---price3 based on fee : {}'.format(price3))
            exch_rate_list.append(price3)

            exch_rate_list.append(datetime.now())      #changed to Human Readable time
            print(exch_rate_list)
            data_log_to_file(str(exch_rate_list))
            rate1 = exch_rate_list[0]
            buy_price = "Buy: {}".format(rate1)
            print(buy_price)
            data_log_to_file(buy_price)
            rate2 = price3 * price2
            sell_price = "Sell: {}".format(rate2)
            print(sell_price)
            data_log_to_file(sell_price)

            if float(rate1)<float(rate2):
                print('Detecting the opportunities for triangular arbitrage trading.', list_of_sym)
                # arb_1_msg = "Arbitrage Possibility - "
                # #Calculate Profit, append to List
                # arb_profit = ((rate2-rate1)/rate2)*100

            else:
                arb_2_msg = "No Arbitrage Possibility"
                print(arb_2_msg)
                data_log_to_file(arb_2_msg)
                exch_rate_list.append(0)
            exch_msg = "Exchange Rate List: " +str(exch_rate_list)+'\n'
            data_log_to_file(exch_msg)
            
        print('\nARBITRAGE FUNCTIONALITY SUCCESSFUL - Data of Exchange Rates Collected\n')
    return exch_rate_list

if __name__ == "__main__":
    run()
