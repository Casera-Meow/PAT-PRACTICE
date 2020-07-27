import math


def Is_prime(n, primes):
    upData = math.ceil(math.sqrt(n))
    for i in primes:
        if i > upData:
            break
        if n % i == 0:
            return False
    return True


primeList = [2, 3]
m, n = input().split()
m = int(m)
n = int(n)
for x in range(5, 1000000, 2):
    upperBound = math.ceil(math.sqrt(x))
    if Is_prime(x, primeList):
        primeList.append(x)
    if len(primeList) > n:
        break
primeList = primeList[m - 1:n]
for outputNum in range(1, 1001):
    if outputNum == len(primeList):
        print(primeList[outputNum - 1], end='')
        break
    if outputNum % 10 != 0 and outputNum < len(primeList):
        print(primeList[outputNum - 1], end=' ')
    if outputNum % 10 == 0 and outputNum < len(primeList):
        print(primeList[outputNum - 1], end='\n')
