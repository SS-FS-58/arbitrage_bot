import asyncio
import itertools
from datetime import datetime
from typing import List

from bitcoin_arbitrage.monitor import settings
from bitcoin_arbitrage.monitor.exchange import Exchange
from bitcoin_arbitrage.monitor.log import setup_logger
from bitcoin_arbitrage.monitor.spread_detection.exchange import Spread, SpreadMissingPriceError, SpreadDifferentCurrenciesError
from bitcoin_arbitrage.monitor.spread_detection.triangular import Tri_Spread, Tri_SpreadDifferentCurrenciesError, Tri_SpreadMissingPriceError

from time import sleep

logger = setup_logger('Monitor')


class Monitor:
    def __init__(self) -> None:
        self._last_spreads: List[Spread] = []

    # async def update(self) -> None:
    def update(self) -> None:
        while True:
            logger.debug('Update...')

            print("updating start!")

            '''update prices of exchanges'''
            # for exchange in settings.EXCHANGES:
            #     exchange.update_prices()

            '''update prices of triexchanges'''
            for tri_exchange in settings.TRI_EXCHANGES:
                tri_exchange['exchange'].update_prices()

            '''calculation spreads using exchange arbitrage.'''
            # spreads = self._calculate_spreads()
            # print('spreads :  ', str(spreads))

            '''calculation tri_spreads using triangular arbitrage.'''
            tri_spreads = self._calculate_tri_spreads()
            print('tri_spreads :  ', str(tri_spreads))

            timestamp = datetime.now().timestamp()

            '''Action on exchange arbitrage'''
            # for action in settings.UPDATE_ACTIONS:
            #     action.run(spreads, settings.EXCHANGES, timestamp)  # ToDo: Run every action asynchronously?

            '''Action on triangular arbitrage'''
            for action in settings.UPDATE_ACTIONS:
                action.run_tri(tri_spreads, settings.TRI_EXCHANGES, timestamp)  # ToDo: Run every action asynchronously?

            # await asyncio.sleep(settings.UPDATE_INTERVAL)
            print('sleeping for update interval :  ', settings.UPDATE_INTERVAL)
            sleep(settings.UPDATE_INTERVAL)

    ''' Exchange arbitrage spreads.'''
    def _calculate_spreads(self) -> List[Spread]:
        combinations: List[(Exchange, Exchange)] = itertools.combinations(settings.EXCHANGES, 2)
        spreads: List[Spread] = []
        for pair in combinations:
            try:
                spread = Spread(exchange_one=pair[0], exchange_two=pair[1])
                if spread.spread > 0:
                    spreads.append(spread)
            except (SpreadMissingPriceError, SpreadDifferentCurrenciesError):
                pass
        return spreads

    ''' Triangular arbitrage spreads.'''
    def _calculate_tri_spreads(self) -> List[Tri_Spread]:
        tri_spreads: List[Tri_Spread] = []
        for tri_exchange in settings.TRI_EXCHANGES:
            for currenciesList in tri_exchange['currenciesList']:
                try:
                    print(currenciesList)
                    tri_spread = Tri_Spread(exchange=tri_exchange['exchange'], currenciesList=currenciesList)
                    if tri_spread.spread > 0:
                        tri_spreads.append(tri_spread)
                except (Tri_SpreadMissingPriceError, Tri_SpreadMissingPriceError):
                    pass
        return tri_spreads
