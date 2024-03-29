import json
import random
import logging
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

CONFIG_FILE = open('static/config.json').read()
logger = logging.getLogger('VK LOGIN MODULE')

class VKLogin():
    '''Класс осуществляющий вход в личный кабинет через ВКонтакте'''
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=self.options)

    def _get_login(self):
        return json.loads(CONFIG_FILE)['login']

    def _get_password(self):
        return json.loads(CONFIG_FILE)['password']

    def set_connection(self):
        try:
            logger.info('vk auth...')
            self.driver.get('https://oauth.vk.com/authorize?client_id=6342119&display=page&redirect_uri=https://lk.dodocontrol.ru/login&response_type=code&v=5.71')
            logger.info('vk auth driver ready')
        except:
            logger.info('vk auth driver error')
            sleep(random.randint(60*15, 60*30))
            self.set_connection()
        
        email_field = self.driver.find_element_by_name('email')
        email_field.send_keys(self._get_login())

        password_field = self.driver.find_element_by_name('pass')
        password_field.send_keys(self._get_password())

        submit = self.driver.find_element_by_class_name('oauth_button')
        submit.click()

        logger.info('vk auth ready')

        return self.driver

        


        
        