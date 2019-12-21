import vk_api
from vk_api.utils import get_random_id

TOKEN = '192639fb972139b5b58d6b1bbdc19e25c5290466defb155694ff1d0bf83c339d36ace50e9decdb9f6b577'

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