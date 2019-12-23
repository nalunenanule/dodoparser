import json
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

CONFIG_FILE = open('static/config.json').read()

class VKLogin():

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('headless')
        self.driver = webdriver.Chrome('static/chromedriver', chrome_options=self.options)

    def _get_login(self):
        return json.loads(CONFIG_FILE)['login']

    def _get_password(self):
        return json.loads(CONFIG_FILE)['password']

    def set_connection(self):
        self.driver.get('https://lk.dodocontrol.ru/login')

        login_elem = self.driver.find_element_by_class_name('login-form__btn')
        login_elem.send_keys(Keys.ENTER)

        email_field = self.driver.find_element_by_name('email')
        email_field.send_keys(self._get_login())

        password_field = self.driver.find_element_by_name('pass')
        password_field.send_keys(self._get_password())

        submit = self.driver.find_element_by_class_name('oauth_button')
        submit.click()

        return self.driver

        


        
        