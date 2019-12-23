import json

import vk_api
from vk_api.utils import get_random_id

TOKEN = json.loads(open('static/config.json').read())['token']

class SendMessageToVk():

    def send_message(self, inspection_list):
        vk_session = vk_api.VkApi(token=TOKEN)
        vk = vk_session.get_api()
        vk.messages.send(
            message=inspection_list,
            random_id=get_random_id(),
            peer_id=16483527
        )
        return 'ok'