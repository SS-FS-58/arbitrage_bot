"""
Bitcoin arbitrage mixins.
"""
import logging
import psutil

logger = logging.getLogger(__name__)


class MonitorMixin(object):
    
    def start_bitcoin_monitor(self):
        try:
            args = [sys.executable, 'manage.py', 'startmonitor', 'start']
            proc = psutil.Popen(args)
            with open("moni_pid.txt", "w") as ts:
                ts.write(str(proc.pid))
        except Exception as error:
            logger.exception(str(error))
            return False
        return True

    def stop_bitcoin_monitor(self):
        try:
            with open("moni_pid.txt") as ts:
                pid = ts.readlines()[0]
            proc = psutil.Process(pid=pid)
            proc.terminate()
        except Exception as error:
            logger.exception(str(error))
            return False
        return True 