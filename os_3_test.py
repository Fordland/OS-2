import random
import time
import threading
global queue_of_numbers
global fall_asleep
queue_of_numbers = []
checking_for_quantity = 0
verification_work = 0
fall_asleep = 0
#если элементов становится более 100, то остановить работу, а если меньше 80, то включить

def checking_the_output(trash, trash_2):
    print("--------------------------------")
    global verification_work
    global fall_asleep
    while True:
        if verification_work == 1:
            if len(queue_of_numbers) >= 15:
                fall_asleep == 1
            elif len(queue_of_numbers) <= 10:
                fall_asleep == 0

def prod(thread, calc):
    global queue_of_numbers
    global checking_for_quantity
    while True:
        if fall_asleep == 1:
            print("Производители уснули")
        elif fall_asleep == 0:
            time.sleep(calc)
            time.sleep(random.random())
            number = random.randint(1, 100)
            print("Производитель", thread, "добавил", number, len(queue_of_numbers))
            queue_of_numbers.append(number)
            time.sleep(1)

prodd = threading.Thread(target = prod, args=(1, 0)).start()
prodd_2 = threading.Thread(target = prod, args=(2, 0.001)).start()
prodd_3 = threading.Thread(target = prod, args=(3, 0.0002)).start()

while checking_for_quantity == 0:
    time.sleep(0.1)
    if len(queue_of_numbers) > 11:
        checking_for_quantity += 1
        verification_work += 1
        print(checking_for_quantity, verification_work)
        print("Проверка запущена")
        break
check_4 = threading.Thread(target = checking_the_output, args=(0, 0)).start()
