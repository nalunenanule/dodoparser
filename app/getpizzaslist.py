from datetime import datetime
import json
import re

from app.login import VKLogin
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

class GetPizzeriaList():

    def __init__(self):
        self.driver = VKLogin().set_connection()
        self.p_list = []

    def get_available_inspection(self):
        WebDriverWait(self.driver, 15).until(ec.url_changes(self.driver.current_url))
        
        self.driver.get('https://lk.dodocontrol.ru/api/personalarea/checkRequests/GetCheckOptions')
        pizzerias_data_list = self.driver.find_element_by_tag_name('pre')

        availible_inspections = json.loads(pizzerias_data_list.text)['openDates']

        if (len(availible_inspections) == 0):
            return 'Нет свободных проверок'
        
        for inspection in availible_inspections:
            parsed_insperction_city = inspection['unit']['name']
            parsed_insperction_alias = inspection['unit']['alias']
            parsed_insperction_address = inspection['unit']['address']
            parsed_insperction_check_type = inspection['checkType']
            parsed_insperction_check_date = datetime.date(datetime.strptime(inspection['date'], '%Y-%m-%dT%H:%M:%S'))

            if (parsed_insperction_check_type == 0):
                parsed_insperction_check_type = 'Доставка'
            else: parsed_insperction_check_type = 'Ресторан'

            self.p_list.append(f'Город: {parsed_insperction_city}, Название: {parsed_insperction_alias}, Адрес: {parsed_insperction_address}, Тип: {parsed_insperction_check_type}, Дата: {parsed_insperction_check_date}\n\n')

        return (''.join(self.p_list))

    def get_user_vk_id(self):
        WebDriverWait(self.driver, 15).until(ec.url_changes(self.driver.current_url))

        self.driver.get('https://lk.dodocontrol.ru/api/personalarea/profile/getSecretBuyer')
        user_vk_id = self.driver.find_element_by_tag_name('pre')

        return json.loads(user_vk_id.text)['secretBuyer']['socialNetworkId']



        