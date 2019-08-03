import itertools

def primes():
    count = 1
    while True:
        count += 1
        isSimple = True
        for i in range(1, count, 1):
            if (count % i == 0) and (i != 1) :
                #print(count, i)
                isSimple = False
                break
        if isSimple:
            yield count



print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]