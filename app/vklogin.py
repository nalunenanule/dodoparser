import json
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# LOGIN = ''
# PASSWORD = ''

class VKLogin():

    def __init__(self, config:json):
        self.config = config

    def get_login_and_password(self):
        self.login = json.loads(open(self.config))['login']
        self.password = json.loads(open(self.config))['password']

    def set_connection(self, login:str, password:str):
        # Добавить проверку на "Залогиненность"
        driver = webdriver.Chrome('static/chromedriver')
        driver.get('https://lk.dodocontrol.ru/login')

        login_elem = driver.find_elements_by_class_name('login-form__btn')
        login_elem.send_keys(Keys.ENTER)

        email_field = driver.find_element_by_name('email')
        email_field.send_keys(login)

        password_field = driver.find_element_by_name('password')
        password_field.send_keys(password)

        submit = driver.find_element_by_class_name('oauth_button')
        submit.click()
        time.sleep(10)




        

