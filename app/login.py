import json
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# LOGIN = ''
# PASSWORD = ''
CONFIG_FILE = open('static/config.json').read()

class VKLogin():

    def _get_login(self):
        return json.loads(CONFIG_FILE)['login']

    def _get_password(self):
        return json.loads(CONFIG_FILE)['password']

    def set_connection(self):
        # Добавить проверку на "Залогиненность"
        driver = webdriver.Chrome('static/chromedriver')
        driver.get('https://lk.dodocontrol.ru/login')

        login_elem = driver.find_element_by_class_name('login-form__btn')
        login_elem.send_keys(Keys.ENTER)

        email_field = driver.find_element_by_name('email')
        email_field.send_keys(self._get_login())

        password_field = driver.find_element_by_name('pass')
        password_field.send_keys(self._get_password())

        submit = driver.find_element_by_class_name('oauth_button')
        submit.click()
        time.sleep(10)