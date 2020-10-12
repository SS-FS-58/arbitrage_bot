"""
Getting a traceback for now - 10/10/20
"""
import asyncio
import logging
import os
import sys
from threading import Thread

from django.core.management.base import BaseCommand, CommandError

from bitcoin_arbitrage.monitor.monitor import Monitor


logger = logging.getLogger(__name__)


class Command(BaseCommand):

    help = 'Starting monitor thread.'
    output_transaction = False

    def add_arguments(self, parser):
        parser.add_argument("action", type=str, help="start | stop monitor")

   
    def handle(self, *args, **options):
        if options.get("action") == "start":
            flag = self.start()
        elif options.get("action") == "stop":
            flag = self.stop()


    def start(self, monitor_loop=asyncio.get_event_loop()):        
        try:
            t = Thread(target=self.start_monitor_thread, args=(monitor_loop,))
            t.start()
        except Exception as error:
            self.stderr.write(self.style.ERROR(str(error))) 
        self.stdout.write(self.style.SUCCESS('Successfully start monitor!'))


    def stop(self):
        """
        Find the thread running with looping and the psutil module, or another way.

        for proc in psutil.process_iter():
            if proc.info["name"] == ...:
                proc.terminate()
        """
        
        raise NotImplementedError() from None        


    @staticmethod
    def start_monitor_thread(loop, monitor=Monitor()):
        logger.info("Starting monitor thread.")
        try:
            loop.run_until_complete(monitor.update())
        except Exception as error:
            logger.exception(str(error))
        return True         
