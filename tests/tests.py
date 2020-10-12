"""
Testing the endpoints with the BinanceAPI here - Charlie.
"""
import logging
import pdb
import sys
import unittest
sys.path.append("..")

import excepts
from api_key import API_KEY, API_SECRET
from api import BinanceAPI

logging.basicConfig(
    filename='tests.log', 
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s => : %(message)s"
)
logger = logging.getLogger(__file__)


class TestBinanceApiEndPoints(unittest.TestCase):

    def setUp(self):
        self.client = BinanceAPI(API_KEY,API_SECRET)

    def test_a_get_current_server_time(self):
        """ Test that we can get the current time. """
        time = self.client.time()
        self.assertTrue(time.get("serverTime", None) is not None)
        logger.info("Able to get current server time.")
    
    def test_b_get_all_prices(self):
        """ Test that we can get all prices """
        prices = self.client.allPrices()
        self.assertTrue(len(prices) > 0)
        logger.info("We got prices.")
        for each in prices: 
            # assert we have {"symbol" : "<symbol>", "price":<price>}.
            self.assertTrue("price" in each and "symbol" in each)
            # assert that each price can be of float type / for calculations.
            self.assertTrue(isinstance(float(each["price"]), float))
        logger.info("We can get all prices listed with this endpoint.")
    
    def test_c_get_all_orders(self):
        """ Test that the we get an exception if there are no orders for given <symbol> """
        with self.assertRaises(excepts.MalformedRequest):
            self.client.allOrders('ETHBTC')
        logger.info("We have no orders from ETHBTC so the API raises MalformedRequest.")
    
    def test_d_get_time_stats(self):
        pass

if __name__ == "__main__":
    unittest.main()