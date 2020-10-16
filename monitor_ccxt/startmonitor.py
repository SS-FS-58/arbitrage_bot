"""
Getting a traceback for now - 10/10/20
"""
import asyncio
import logging
import os
import sys
from threading import Thread

from bitcoin_arbitrage.monitor.monitor import Monitor

logger = logging.getLogger(__name__)


class Command():

    help = 'Starting monitor thread.'
    output_transaction = False

    def __init__(self)->None:
        self.monitor = Monitor()

    def start(self, monitor_loop=asyncio.get_event_loop()):        
        try:
            self.monitor.update()
            # t = Thread(target=self.start_monitor_thread, args=(monitor_loop,))
            # t = Thread(target=self.start_monitor_thread,)
            # t.start()
        except Exception as error:
            print(str(error)) 
        print('Successfully start monitor!')


    def stop(self):
        """
        Find the thread running with looping and the psutil module, or another way.

        for proc in psutil.process_iter():
            if proc.info["name"] == ...:
                proc.terminate()
        """
        
        raise NotImplementedError() from None        


    # @staticmethod
    # def start_monitor_thread(loop, monitor=Monitor()):
    def start_monitor_thread(self):
        logger.info("Starting monitor thread.")
        try:
            # loop.run_until_complete(monitor.update())
            self.monitor.update()
            print('Monitor updating ... in startmonitor.')
        except Exception as error:
            logger.exception(str(error))
        return True   

if __name__ == "__main__":
    command = Command()
    command.start()
