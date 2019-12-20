import re

from selenium.webdriver.support.wait import WebDriverWait

from app.login import VKLogin

class GetPizzeriaList():

    def __init__(self):
        self.driver = VKLogin().set_connection()
        self.main_list = []

    def get_pizzeria_data(self):
        WebDriverWait(self.driver, 100).until(
            lambda is_element_available: self.driver.find_element_by_class_name('pizzeria__list'))
        
        pizzerias_data_list = self.driver.find_elements_by_class_name('pizzeria__list')
        return self.get_available_inspection(pizzerias_data_list)

    def get_available_inspection(self, pizzerias_data_list):
        for elem in pizzerias_data_list:
            # result = re.findall('Нет свободных дат', elem.text) Вариант через регулярные выражения
            result = (elem.text).count('Нет свободных дат')
            if result != 3:
                self.main_list.append(elem.text)

        if len(self.main_list) != 0:
            return self.main_list
        
        return ['Свободных проверок нет']


               
                
# Придумать интеграцию с сервисами (?) (Vk, Mattermost, WhatsApp)
# Продумать периодичность запросов к сайту
# Продумать возможность автоматической записи на проверку