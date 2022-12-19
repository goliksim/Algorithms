import random


__bits = []  # список случайных 64-битных значений, для BitHash
__rnd = random.Random()
__rnd.seed("BitHash random numbers") # сид для генерации
for i in range(64 * 1024): #длина списка 65536
    #getrandbits(64) - возвращает рандомное число до 2^64
    __bits.append(__rnd.getrandbits(64))


def BitHash(s, h=0):
    for c in s:
        # << 1 сдвиг налево на  1 бит /  >> 63 свиг направо на 63 бита
        # ord(chr) -> int
        # ^ - бинарный xor
        h = (((h << 1) | (h >> 63)) ^ __bits[ord(c)])
        # &= - бинарное «И»   
        h &= 0xffffffffffffffff #2**64 -1 (все единички)
    return h


def badHashFunc(s, hashVal=5381):
    for c in s:
        hashVal = hashVal * 33 + ord(c)
    return hashVal


# сброс BitHash. Новая хеш-функция для Cuckoo Hashing.
def ResetBitHash():
    global __bits
    for i in range(64 * 1024):
        __bits[i] = __rnd.getrandbits(64)


def __main():
    # Для Cuckoo Hashing два значения можно получить следующим образом
    v1 = BitHash("foo");
    v2 = BitHash("foo", v1);
    print(v1,v2)
    # сделаем сброс хеш функции
    
    print("\nсброс BitHash на новую хэш-функцию\n")
    ResetBitHash()

    v1 = BitHash("foo");
    v2 = BitHash("foo", v1);
    print(v1,v2)
  

if __name__ == '__main__':
    __main()