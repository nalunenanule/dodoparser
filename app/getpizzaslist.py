import json

from app.login import VKLogin
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

class GetPizzeriaList():

    def __init__(self):
        self.driver = VKLogin().set_connection()

    def get_available_inspection(self):
        WebDriverWait(self.driver, 15).until(ec.url_changes(self.driver.current_url))
        
        self.driver.get('https://lk.dodocontrol.ru/api/personalarea/checkRequests/GetCheckOptions')
        pizzerias_data_list = self.driver.find_element_by_tag_name('pre')

        if len(pizzerias_data_list.text) != 0:
            return pizzerias_data_list.text

        return 'Нет свободных проверок'

    def get_user_vk_id(self):
        WebDriverWait(self.driver, 15).until(ec.url_changes(self.driver.current_url))

        self.driver.get('https://lk.dodocontrol.ru/api/personalarea/profile/getSecretBuyer')
        user_vk_id = self.driver.find_element_by_tag_name('pre')

        return json.loads(user_vk_id.text)['secretBuyer']['socialNetworkId']



        