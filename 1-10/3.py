from math import sqrt


def max_prime_factors(n: int) -> int:
    maxPrime = -1
    while n % 2 == 0:
        maxPrime = 2
        n >>= 1

    while n % 3 == 0:
        maxPrime = 3
        n = (int)(n / 3)

    for i in range(5, int(sqrt(n)) + 1, 6):
        while n % i == 0:
            maxPrime = i
            n = (int)(n / i)
        while n % (i+2) == 0:
            maxPrime = i+2
            n = (int)(n / (i+2))

    if n > 4:
        maxPrime = n

    return maxPrime


print(max_prime_factors(600851475143))
