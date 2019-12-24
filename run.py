from app.getpizzaslist import GetPizzeriaList
from app.vk_module import SendMessageToVk

def actions_with_insperction_list():
    inspections = GetPizzeriaList().get_available_inspection()
    SendMessageToVk().send_message(inspections)

if __name__ == "__main__":
    actions_with_insperction_list()

# Посмотреть возвожность получаения проверок через API

# Делать проверку по запросу и по времени
# Распарсить list, оставить только доступные проверки 
# Сделать интеграцию с Discord (Возможно Docker)
# Отпавлять сообщение текущему пользователю, передавать из Selenium
# Разобраться с токеном и использованием сообщений группы (Вопрос ! своя группа или отдельная для каждого пользователя)