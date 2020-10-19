from typing import List, Optional

# from bitcoin_arbitrage.app import db
from bitcoin_arbitrage.models import Spread, Exchange, Tri_Spread
from bitcoin_arbitrage.monitor.update import UpdateAction


class SpreadHistoryToDB(UpdateAction):
    from bitcoin_arbitrage.monitor.spread_detection.exchange import Spread

    def run(self, spreads: List[Spread], exchanges: List[Exchange], timestamp: float) -> None:
        db_spreads: List[Spread] = []
        for spread in spreads:
            exchange_buy = Exchange(name=spread.exchange_buy.name,
                                    currency_pair=spread.exchange_buy.currency_pair,
                                    last_ask_price=spread.exchange_buy.last_ask_price,
                                    last_bid_price=spread.exchange_buy.last_bid_price)
            # db.session.add(exchange_buy)
            exchange_buy.save()
            exchange_sell = Exchange(name=spread.exchange_sell.name,
                                     currency_pair=spread.exchange_sell.currency_pair,
                                     last_ask_price=spread.exchange_sell.last_ask_price,
                                     last_bid_price=spread.exchange_sell.last_bid_price)
            # db.session.add(exchange_sell)
            exchange_sell.save()

            s = Spread(spread=spread.spread,
                       xchange_buy=exchange_buy,
                       xchange_sell=exchange_sell)
            # db_spreads.append(s)
            s.save()

        # db.session.add_all(db_spreads)
        # db.session.commit()

    ''' Run triangular actions.'''
    def run_tri(self, tri_spreads: List[Tri_Spread], tri_exchanges: List[Exchange], timestamp: float) -> None:
        db_spreads: List[Tri_Spread] = []
        print('tri_spreads', str(tri_spreads))
        for spread in tri_spreads:
            exchange_buy = Exchange(name=spread.exchange_buy.name,
                                    currency_pair=spread.exchange_buy.currency_pair,
                                    last_ask_price=spread.exchange_buy.last_ask_price,
                                    last_bid_price=spread.exchange_buy.last_bid_price)
            # db.session.add(exchange_buy)
            exchange_buy.save()
            exchange_sell = Exchange(name=spread.exchange_sell.name,
                                     currency_pair=spread.exchange_sell.currency_pair,
                                     last_ask_price=spread.exchange_sell.last_ask_price,
                                     last_bid_price=spread.exchange_sell.last_bid_price)
            # db.session.add(exchange_sell)
            exchange_sell.save()

            s = Spread(spread=spread.spread,
                       xchange_buy=exchange_buy,
                       xchange_sell=exchange_sell)
            # db_spreads.append(s)
            s.save()
