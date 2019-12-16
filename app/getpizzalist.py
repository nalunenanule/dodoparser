import json
import time

from app.login import VKLogin

class GetPizzasList():

    def get_pizzas_list(self):
        login = VKLogin()
        connection = login.set_connection()
        
