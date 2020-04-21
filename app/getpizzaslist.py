import re
import json
import pymongo
from datetime import datetime
from pymongo import MongoClient

from app.login import VKLogin
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

class DatabaseData():

    def __init__(self):
        self.cluster = MongoClient("mongodb+srv://nuzkij:a1b2c3d4@cluster0-xpotn.mongodb.net/test?retryWrites=true&w=majority")

    def get_collection(self):
        db = self.cluster['dodo']
        return db['inspection']
    

class GetPizzeriaList():
    '''Класс для получения доступных проверок'''
    def __init__(self):
        self.driver = VKLogin().set_connection()
        self.db = DatabaseData().get_collection()
        self._get_available_inspection()

    def _get_available_inspection(self):
        WebDriverWait(self.driver, 30).until(ec.url_changes(self.driver.current_url))
        
        self.driver.get('https://lk.dodocontrol.ru/api/personalarea/checkRequests/GetCheckOptions')
        pizzerias_data_list = self.driver.find_element_by_tag_name('pre')

        availible_inspections = json.loads(pizzerias_data_list.text)['openDates']

        if (len(availible_inspections) == 0):
            return 'Нет свободных проверок'

        self.db.remove()

        self.db.insert_many({"city": inspection['unit']['name'],
                           "name": inspection['unit']['alias'],
                           "address": inspection['unit']['address'],
                           "check_type": self._get_check_type(inspection['checkType']),
                           "check_date": inspection['date'],
                           "user_vk_id": self._get_user_vk_id()} for inspection in availible_inspections)

    def _get_check_type(self, type_code):
        if type_code == 0:
            return 'Доставка'
        else: return 'Ресторан'

    def _get_user_vk_id(self):
        self.driver.get('https://lk.dodocontrol.ru/api/personalarea/profile/getSecretBuyer')
        user_vk_id = self.driver.find_element_by_tag_name('pre')

        return json.loads(user_vk_id.text)['secretBuyer']['socialNetworkId'] 