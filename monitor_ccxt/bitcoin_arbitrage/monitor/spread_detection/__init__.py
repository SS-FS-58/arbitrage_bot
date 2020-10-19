from bitcoin_arbitrage.monitor import settings
from bitcoin_arbitrage.monitor.exchange import Exchange
from bitcoin_arbitrage.monitor.log import setup_logger

from abc import ABC, abstractmethod


class SpreadABC(ABC):
    
    def __str__(self) -> str:
        return self.summary

    def __repr__(self) -> str:
        return self.__str__()

    @property
    @abstractmethod
    def summary(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def spread_with_currency(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def spread_percentage(self):
        raise NotImplementedError

    @abstractmethod
    def _calculate_spread(self) -> int:
        raise NotImplementedError
    @property
    def is_above_trading_thresehold(self) -> bool:
        return self.spread > settings.MINIMUM_SPREAD_TRADING
