from flask import Flask, request

from app.getpizzaslist import GetPizzeriaList, AvailibleInspections
from app.vk_module import SendMessageToVk

app = Flask(__name__)

@app.route('/', methods=['GET'])
def actions_with_insperction_list():
    data = request.get_json()
    if data['type'] == 'message_new':
        if data['object']['text'] == 'Доступные проверки':
            GetPizzeriaList()
            all_inspections = AvailibleInspections()
            SendMessageToVk().send_message(all_inspections.inspections, all_inspections.user_vk_id)
    return 'ok'
    
if __name__ == '__main__':
    app.run()

# Делать проверку по запросу и по времени 
# Сделать интеграцию с Discord (Возможно Docker)