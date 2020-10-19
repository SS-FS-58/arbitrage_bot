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
    # monitor = Monitor()
    help = 'Starting monitor thread.'
    output_transaction = False
    stop_threads = False

    def add_arguments(self, parser):
        parser.add_argument("action", type=str, help="start | stop monitor")
        self.monitor = Monitor()

   
    def handle(self, *args, **options):
        if options.get("action") == "start":
            flag = self.start()
        elif options.get("action") == "stop":
            flag = self.stop()


    def start(self, monitor_loop=asyncio.get_event_loop()):        
        try:
            # t = Thread(target=self.start_monitor_thread, args=(monitor_loop,))
            # stop_threads = False
            # t = Thread(target=self.start_monitor_thread)
            # # t.daemon = True
            # t.start()
            self.monitor.update()
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
        try:
            self.monitor.stop_update()            
        except Exception as error:
            self.stderr.write(self.style.ERROR(str(error))) 
        self.stdout.write(self.style.SUCCESS('Successfully stop monitor!'))


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
