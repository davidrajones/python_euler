from math import sqrt
from collections import Counter
from functools import reduce


def get_prime_factors(n) -> Counter:
    primes = Counter()
    while n % 2 == 0:
        primes.update([2])
        n = int(n / 2)
    for i in range(3, int(sqrt(n))+1, 2):
        while n % i == 0:
            primes.update([i])
            n = int(n / i)

    if n > 2:
        primes.update([n])
    return primes


def get_product(input: list) -> int:
    return reduce((lambda x, y: (int)(x) * (int)(y)), input)


i = 1
num = 1
while 1:
    i += 1
    num += i
    prime_count = get_prime_factors(num)
    print(prime_count)
    primes = [i+1 for j, i in prime_count.items()]
    divisor_count = get_product(primes)
    if divisor_count > 500:
        print(num)
        exit(0)
