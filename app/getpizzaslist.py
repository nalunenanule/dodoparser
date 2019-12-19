from selenium.webdriver.support.wait import WebDriverWait

from app.login import VKLogin

class GetPizzeriaList():

    def __init__(self):
        self.driver = VKLogin().set_connection()
        self.main_dict = {}

    def get_pizzerias_data(self):
        WebDriverWait(self.driver, 100).until(
            lambda is_element_available: self.driver.find_element_by_class_name('pizzeria__list'))
        pizzerias__list = self.driver.find_elements_by_class_name('pizzeria__list')
        return self.get_available_inspection(pizzerias__list)

    def get_available_inspection(self, pizzerias__list):

        for pizzeria_element in pizzerias__list:
            self.main_dict.update(pizzeria_element.text)
        
        return self.main_dict        
                
# Для каждой пицерии свои даты или общий список (парсить блоками и добавлять в рестораны), 
# либо создавать список [Название ресторана:даты проверок, ...] Посредством проверки каждого pizzeria__list =>
# Для каждой пиццери добавлять даты, даже если их нет если название пиццерии совпадает в названием в методе получения даты, то добавить
# этому ресторану полученные даты

# Проверка доступных проверок  
# TO DO Распарсить даты, придумать интеграцию с сервисами (?) (Vk, Mattermost, WhatsApp)
# Продумать периодичность запросов к сайту
# Продумать возможность автоматической записи на проверку