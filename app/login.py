import json

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

CONFIG_FILE = open('static/config.json').read()

class VKLogin():
    '''Класс осуществляющий вход в личный кабинет через ВКонтакте'''
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('headless')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=self.options)

    def _get_login(self):
        return json.loads(CONFIG_FILE)['login']

    def _get_password(self):
        return json.loads(CONFIG_FILE)['password']

    def set_connection(self):
        self.driver.get('https://oauth.vk.com/authorize?client_id=6342119&display=page&redirect_uri=https://lk.dodocontrol.ru/login&response_type=code&v=5.71')

        email_field = self.driver.find_element_by_name('email')
        email_field.send_keys(self._get_login())

        password_field = self.driver.find_element_by_name('pass')
        password_field.send_keys(self._get_password())

        submit = self.driver.find_element_by_class_name('oauth_button')
        submit.click()

        return self.driver

        


        
        