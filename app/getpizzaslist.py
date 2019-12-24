import time

from app.login import VKLogin
from selenium.webdriver.support import expected_conditions as ec

class GetPizzeriaList():

    def __init__(self):
        self.driver = VKLogin().set_connection()

    def get_available_inspection(self):
        # Костыль
        time.sleep(5)
        self.driver.get('https://lk.dodocontrol.ru/api/personalarea/checkRequests/GetCheckOptions')
        pizzerias_data_list = self.driver.find_element_by_tag_name('pre')

        if len(pizzerias_data_list.text) != 0:
            return pizzerias_data_list.text

        return 'Нет свободных проверок'

        