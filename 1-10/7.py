prime_list = [2]

num = 1

while len(prime_list) < 10001:
    num += 2
    for p in prime_list:
        if num % p == 0:
            break
    else:
        prime_list.append(num)

print(prime_list[-1])
