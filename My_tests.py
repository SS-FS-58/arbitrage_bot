"""
Testing binance and other apis : by mariya
"""
import logging
import pdb
import sys
import unittest
from binance.client import Client
import excepts
import json
import hmac
import hashlib
import requests
from urllib.parse import urljoin, urlencode
from api_key import API_KEY, SECRET_KEY

logging.basicConfig(
    filename='My_tests.log', 
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s => : %(message)s"
)
logger = logging.getLogger(__file__)


class TestBinanceApiEndPoints(unittest.TestCase):

    def setUp(self):
        self.client = Client(API_KEY, SECRET_KEY)
        self.assertIsNotNone(self.client)
        logger.info('Setted the api client.')
    def test_1_get_system_status(self):
        """ Test that we can get the system status. """
        status = self.client.get_system_status()
        self.assertIsNotNone(status)
        logger.info('we can get system status now.')
    def test_2_get_historycal_klines(self):
        """ Test that we can get the historical klines. """
        klines = self.client.get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_1MINUTE, "10 minute ago UTC")
        self.assertIsNotNone(klines)
        logger.info("we can get historical klines.")

class TestBitfinexApiEndPoints(unittest.TestCase):

    def setUp(self):
        self.base_url = "https://api.bitfinex.com/v1"
        
    def test_1_get_ticker(self):
        """ Test that we can get the ticker url. """
        url= f"{self.base_url}/pubticker/BTCUSD"
        response = requests.get(url, None)
        print(response.json())
        self.assertIsNotNone(response.json())
        logger.info('we can get system status now.')

class TestBitstampApiEndPoints(unittest.TestCase):

    def setUp(self):
        self.base_url = "https://www.bitstamp.net/api/v2"
        
    def test_1_get_ticker(self):
        """ Test that we can get the ticker url. """
        url= f"{self.base_url}/ticker/btcusd"
        response = requests.get(url, None)
        print(response.json())
        self.assertIsNotNone(response.json())
        logger.info('we can get system status now.')

if __name__ == "__main__":
    unittest.main()