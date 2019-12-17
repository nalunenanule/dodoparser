from selenium.webdriver.support.wait import WebDriverWait

from app.login import VKLogin

class GetPizzeriaList():

    def __init__(self):
        self.driver = VKLogin().set_connection()
        self.date_list = []

    def get_pizzerias_list(self):
        WebDriverWait(self.driver, 100).until(
            lambda is_element_available: self.driver.find_element_by_class_name('pizzeria__list'))
        pizzerias__list = self.driver.find_elements_by_xpath('//div[@class="pizzeria__list"]/h2')
        self.get_available_inspection() # Вызов функции для тестирования

        return pizzerias__list

    def get_available_inspection(self):
        available_inspection = self.driver.find_elements_by_class_name('type__date')

        for value in available_inspection:
            if value.text != 'Нет свободных дат':
                self.date_list.append(value.text)
        
        if len(self.date_list) == 0:
            return False
        
        return self.date_list        
                
# Для каждой пицерии свои даты или общий список (парсить блоками и добавлять в рестораны), 
# либо создавать список [Название ресторана:даты проверок, ...] Посредством проверки каждого pizzeria__list =>
# Для каждой пиццери добавлять даты, даже если их нет если название пиццерии совпадает в названием в методе получения даты, то добавить
# этому ресторану полученные даты

# Проверка доступных проверок  
# TO DO Распарсить даты, придумать интеграцию с сервисами (?) (Vk, Mattermost, WhatsApp)
# Продумать периодичность запросов к сайту
# Продумать возможность автоматической записи на проверку