import json

import vk_api
from vk_api.utils import get_random_id

TOKEN = json.loads(open('static/config.json').read())['token']

class SendMessageToVk():
    '''Класс работающий с ВКонтакте'''
    def __init__(self):
        self.vk_session = vk_api.VkApi(token=TOKEN)
        self.vk = self.vk_session.get_api()

    def send_message(self, inspection_list, user_id):
        print(inspection_list)
        self.vk.messages.send(
            message=inspection_list,
            random_id=get_random_id(),
            peer_id=user_id
        )
        return 'ok'