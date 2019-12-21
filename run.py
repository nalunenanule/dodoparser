from app.getpizzaslist import GetPizzeriaList
from app.vk_module import SendMessageToVk

def actions_with_insperction_list():
    p_list = GetPizzeriaList().start()
    SendMessageToVk().send_message(p_list)

if __name__ == "__main__":
    actions_with_insperction_list()

# Делать проверку по запросу и по времени
# Распарсить list, оставить только доступные проверки 