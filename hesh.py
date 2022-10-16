import time
from itertools import product # эта строка импортирует специальную функцию, для перебора всех вариантов
from hashlib import sha256 as hash_ # эта строка импротирует функцию, для создания хеша (для удобства можете поменять хеш, на один из доступных в этой библиотеке)
first_hash = input("Введите хэш: ")
len_hash = int(input("Введите длину закодированного хеша(если не знаете длину, напишите 0): "))
start_time = time.time()
if len_hash == 0:
    len_hash = 999

    for i2 in range(len_hash):
        for i in product("abcdefghijklmnopqrstuvwxyz1234567890", repeat=i2):
            if hash_("".join(i).encode("utf-8")).hexdigest() == first_hash:
                print("".join(i), (time.time() - start_time))
                quit()
else:

    for i in product("abcdefghijklmnopqrstuvwxyz1234567890", repeat=len_hash):
        if hash_("".join(i).encode("utf-8")).hexdigest() == first_hash:
            print("".join(i), (time.time() - start_time))
            quit()
