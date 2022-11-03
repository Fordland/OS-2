import random
import time
import threading
import keyboard
import sys
stack = []
joj = []
work = 1
def con(thread, calc):
    time.sleep(5)
    while True:
        if random.randrange(1, 8, 1) == 1:
            for i in range(random.randrange(0, len(stack) + 1)):
                print("Потребитель",random.randrange(1, 3), "взял" ,stack[i])
                time.sleep(1)

def prod(thread, calc):
    for i in range(0, 201):
        stack.append(int(random.randrange(1, 101, 1)))
        print("Производитель",random.randrange(1, 4),"добавил", stack[i])
        time.sleep(1)

prodd = threading.Thread(target = prod, args=(1, 270)).start()
workk = threading.Thread(target = con, args=(1, 270)).start()
