from time import sleep
import threading
from threading import Thread

from app.getpizzaslist import GetPizzeriaList

def do_work():
    return GetPizzeriaList()

threading.Timer(21600, do_work()).start()

if __name__ == '__main__':
    do_work()