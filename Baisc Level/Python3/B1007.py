'''
Tips:
for loop to find prime numbers:time exceeded
Composite number must be divisible by prime numbers
prime numbers = [2,3,5,7,11,13,17,19,......]
Therefore, a prime number can be judged  by whether the number can divide prime numbers smaller than it
In the for loop,the range must be stepped at 2,or it will time exceeded
'''
import math


def Is_prime(n, primes):
    upData = math.ceil(math.sqrt(n))
    for i in primes:
        if i > upData:
            break
        if n % i == 0:
            return False
    return True


n = eval(input())
primeNum = [2]
prime = 0
for i in range(3, n + 1, 2):
    if Is_prime(i, primeNum):
        primeNum.append(i)
        if len(primeNum) >= 2 and primeNum[len(primeNum) - 1] - primeNum[len(primeNum) - 2] == 2:
            prime += 1
print(prime, end='')
