import re
import json
from datetime import datetime

from app.login import VKLogin
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

class AvailibleInspections():
    '''Класс описывающий доступные проверки'''
    city = str
    name = str
    address = str
    check_type = str
    check_date = str
    user_vk_id = int
    inspections = []

    def __init__(self):
        self.inspections.append(f'Город: {self.city}, Название: {self.name}, Адрес: {self.address}, Тип: {self.check_type}, Дата: {self.check_date}\n\n')
        self.inspections = ''.join(self.inspections)
        self.inspections = self.inspections[:-1]

class GetPizzeriaList():
    '''Класс для получения доступных проверок'''
    def __init__(self):
        self.driver = VKLogin().set_connection()
        self._get_available_inspection()

    def _get_available_inspection(self):
        WebDriverWait(self.driver, 15).until(ec.url_changes(self.driver.current_url))
        
        self.driver.get('https://lk.dodocontrol.ru/api/personalarea/checkRequests/GetCheckOptions')
        pizzerias_data_list = self.driver.find_element_by_tag_name('pre')

        availible_inspections = json.loads(pizzerias_data_list.text)['openDates']

        if (len(availible_inspections) == 0):
            return 'Нет свободных проверок'
        
        for inspection in availible_inspections:
            AvailibleInspections.city = inspection['unit']['name']
            AvailibleInspections.name = inspection['unit']['alias']
            AvailibleInspections.address = inspection['unit']['address']
            AvailibleInspections.check_type = self._get_check_type(inspection['checkType'])
            AvailibleInspections.check_date = datetime.date(datetime.strptime(inspection['date'], '%Y-%m-%dT%H:%M:%S'))
            AvailibleInspections.user_vk_id = self._get_user_vk_id()
            AvailibleInspections()

    def _get_check_type(self, type_code):
        if type_code == 0:
            return 'Доставка'
        else: return 'Ресторан'

    def _get_user_vk_id(self):
        self.driver.get('https://lk.dodocontrol.ru/api/personalarea/profile/getSecretBuyer')
        user_vk_id = self.driver.find_element_by_tag_name('pre')

        return json.loads(user_vk_id.text)['secretBuyer']['socialNetworkId'] 