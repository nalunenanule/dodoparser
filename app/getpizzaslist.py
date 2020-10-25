import re
import json
import random
import logging
import pymongo
from pymongo import MongoClient
from time import sleep

from app.login import VKLogin
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

logger = logging.getLogger('PIZZA MODULE')

class DatabaseData():

    def __init__(self):
        self.cluster = MongoClient('mongodb+srv://nuzkij:a1b2c3d4@cluster0-xpotn.mongodb.net', port=27017)

    def get_collection(self):
        db = self.cluster['dodo']
        return db['inspection']

    def close_connection(self):
        self.cluster.close()
    

class GetPizzeriaList():
    '''Класс для получения доступных проверок'''
    def __init__(self):
        self.driver = VKLogin().set_connection()
        self.db = DatabaseData().get_collection()
        self._get_available_inspection()

    def _get_available_inspection(self):
        try:
            logger.info('inspection driver...')
            WebDriverWait(self.driver, 30).until(ec.url_changes(self.driver.current_url))
            logger.info('inspection driver ready')
        except:
            logger.info('inspection driver error')
            sleep(random.randint(60*15, 60*30))
            self._get_available_inspection()
        
        self.driver.get('https://lk.dodocontrol.ru/api/personalarea/checkRequests/GetCheckOptions')
        pizzerias_data_list = self.driver.find_element_by_tag_name('pre')

        availible_inspections = json.loads(pizzerias_data_list.text)['openDates']

        self.db.remove()
        logger.info('clear table')

        if (len(availible_inspections) == 0):
            logger.info('Нет доступных проверок')
            self.driver.quit()
            DatabaseData().close_connection()
            return

        self.db.insert_many({"city": inspection['unit']['name'],
                           "name": inspection['unit']['alias'],
                           "address": inspection['unit']['address'],
                           "check_type": self._get_check_type(inspection['checkType']),
                           "check_date": inspection['date']} for inspection in availible_inspections)

        logger.info(f'add inspections {len(availible_inspections)}')
        
        self.driver.quit()
        DatabaseData().close_connection()
        logger.info('close')

    def _get_check_type(self, type_code):
        if type_code == 0:
            return 'Доставка'
        else: return 'Ресторан'