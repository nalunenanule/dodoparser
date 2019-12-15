import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

CONFIG_FILE = open('static/config.json').read()
login = json.loads(CONFIG_FILE)['login']
password = json.loads(CONFIG_FILE)['password']


driver = webdriver.Chrome('static/chromedriver')
driver.get('https://lk.dodocontrol.ru/login')
elem = driver.find_element_by_class_name('login-form__btn')
elem.send_keys(Keys.ENTER)

email_field = driver.find_element_by_name('email')
email_field.send_keys(login)

password_field = driver.find_element_by_name('pass')
password_field.send_keys(password)

submit = driver.find_element_by_class_name('oauth_button').click()
time.sleep(10)
driver.quit()

