import time
from itertools import product
from hashlib import sha256 as hash_
from threading import Thread
print("________________Выберите в каком потоке расшифровать:________________")
print("________________Однопоток                  Многопоток________________")
print("___________________[1]_________________________[2]___________________")
choise = int(input())
if choise == 1:
    first_hash = '74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f', '3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b', '1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad'
    for j in range(3):
        start_time = time.time()
        for i in product("abcdefghijklmnopqrstuvwxyz", repeat=5):
            if hash_("".join(i).encode("utf-8")).hexdigest() == first_hash[j]:
                print("".join(i), (time.time() - start_time), time.time())
                break
elif choise == 2:
    first_hash = '74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f'
    second_hash = '3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b'
    thirst_hash = '1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad'

    def ch1(thread, calc):
        abc = "abcdefghijklmnopqrstuvwxyz"
        first_hash = '1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad'
        for s in range(1, 27):
            a = slice(s)
            start_time = time.time()
            for i in product(abc[a], repeat=5):
                if hash_("".join(i).encode("utf-8")).hexdigest() == first_hash:
                    print("".join(i), (time.time() - start_time))
                    break
    def ch2(thread, calc):
        abc = "abcdefghijklmnopqrstuvwxyz"
        first_hash ='3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b'
        for s in range(1, 27):
            b = slice(s)
            start_time = time.time()
            for i in product(abc[b], repeat=5):
                if hash_("".join(i).encode("utf-8")).hexdigest() == first_hash:
                    print("".join(i), (time.time() - start_time))
                    break
    def ch3(thread, calc):
        abc = "abcdefghijklmnopqrstuvwxyz"
        first_hash = '74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f'
        for s in range(1, 27):
            c = slice(s)
            start_time = time.time()
            for i in product(abc[c], repeat=5):
                if hash_("".join(i).encode("utf-8")).hexdigest() == first_hash:
                    print("".join(i), (time.time() - start_time))
                    break

    thr1 = Thread(target = ch1, args=(1, 33)).start()
    thr2 = Thread(target=ch2, args=(1, 33)).start()
    thr3 = Thread(target=ch3, args=(1, 33)).start()

