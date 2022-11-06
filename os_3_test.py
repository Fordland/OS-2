import random
import time
import threading
from pynput import keyboard
stack = []
give = []
work = 1
working = True
def con(thread, calc):
    time.sleep(5)
    while True:
        if random.randrange(1, 5, 1) == 2:
            for i in range(random.randrange(0, len(stack) + 1)):
                if i not in give:
                    print("Потребитель",random.randrange(1, 3), "взял" ,stack[i])
                    give.append(i)
                    time.sleep(1)
                else:
                    time.sleep(0.1)

def on_press(key):

def prod(thread, calc):
    while working == True:
        for i in range(0, 201):
            stack.append(int(random.randrange(1, 101, 1)))
            print("Производитель",random.randrange(1, 4),"добавил", stack[i])
            time.sleep(1)

prodd = threading.Thread(target = prod, args=(1, 270)).start()
workk = threading.Thread(target = con, args=(1, 270)).start()
wait = threading.Thread(target = on_press, args=(1, 270)).start()
