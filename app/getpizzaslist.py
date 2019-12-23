import re

from selenium.webdriver.support.wait import WebDriverWait
from app.login import VKLogin

class GetPizzeriaList():

    def __init__(self):
        self.driver = VKLogin().set_connection()
        self.main_list = []

    def start(self):
        return self._get_pizzeria_data()

    def _get_pizzeria_data(self):
        WebDriverWait(self.driver, 100).until(
            lambda is_element_available: self.driver.find_element_by_class_name('pizzeria__list'))
        
        pizzerias_data_list = self.driver.find_elements_by_class_name('pizzeria__list')
        return self._get_available_inspection(pizzerias_data_list)

    def _get_available_inspection(self, pizzerias_data_list):
        for elem in pizzerias_data_list:
            result = (elem.text).count('Нет свободных дат')
            if result != 3:
                self.main_list.append(elem.text)

        if len(self.main_list) != 0:
            return self.main_list
        
        return ['Нет свободных проверок']

        