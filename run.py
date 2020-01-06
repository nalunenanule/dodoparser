from app.getpizzaslist import GetPizzeriaList, AvailibleInspections
from app.vk_module import SendMessageToVk

def actions_with_insperction_list():
    GetPizzeriaList()
    all_inspections = AvailibleInspections()
    SendMessageToVk().send_message(all_inspections.inspections, all_inspections.user_vk_id)

if __name__ == '__main__':
    actions_with_insperction_list()

# Делать проверку по запросу и по времени 
# Сделать интеграцию с Discord (Возможно Docker)