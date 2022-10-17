import time
from itertools import product
from hashlib import sha256 as hash_

print("В каком режиме работать")
print("Одним потокои или многопотоком(1/0):")
a = int(input())
first_hash = '74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f',\
                 '3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b',\
                 '1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad'
if a == 1:
    timee = time.time()
    for j in range(3):
        start_time = time.time()
        for i in product("abcdefghijklmnopqrstuvwxyz", repeat=5):
            if hash_("".join(i).encode("utf-8")).hexdigest() == first_hash[j]:
                print("".join(i), (time.time() - start_time))
                break
    print(time.time() - timee)
else:
    start_time = time.time()
    f = 0
    for i in product("abcdefghijklmnopqrstuvwxyz", repeat=5):
        x = hash_("".join(i).encode("utf-8")).hexdigest()
        if x == first_hash[0] or\
            x == first_hash[1] or\
            x == first_hash[2]:
            print("".join(i), (time.time() - start_time))
            f += 1
            if f == 3:
                print(time.time() - start_time)
                break
