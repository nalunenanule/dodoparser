import logging
import random
from time import sleep
from datetime import datetime, timedelta

from app.getpizzaslist import GetPizzeriaList

logging.basicConfig(filename='status.log', level=logging.INFO, format='%(asctime)s %(name)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger('MAIN')
TIME_INTERVAL = 60*60*2

for n in range(0, TIME_INTERVAL):
    logger.info(f'attempt number {n}')
    sleep_interval = TIME_INTERVAL + random.randint(1*60, 60*15)
    str_date = str(timedelta(seconds=sleep_interval))
    logger.info(f'next attempt in {str_date}')
    GetPizzeriaList()
    sleep(sleep_interval)
    