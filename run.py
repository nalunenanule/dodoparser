from app.getpizzaslist import GetPizzeriaList
from app.vk_module import SendMessageToVk

def actions_with_insperction_list():
    inspections = GetPizzeriaList().get_available_inspection()
    user_id = GetPizzeriaList().get_user_vk_id()
    SendMessageToVk().send_message(inspections, user_id)

if __name__ == "__main__":
    actions_with_insperction_list()

# Реализовать добавление полученных данных в уже подготовленный list (Прим.: Город:...)
# Метод get_available_inspection ничего не возвращает, исправить!
# Добавить формирование строк с проверками    

# Делать проверку по запросу и по времени 
# Сделать интеграцию с Discord (Возможно Docker)
# Отпавлять сообщение текущему пользователю, передавать из Selenium
# Разобраться с токеном и использованием сообщений группы (Вопрос ! своя группа или отдельная для каждого пользователя)