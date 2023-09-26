from math import factorial

for i in range(20, factorial(20), 20):
    not_bad = True
    for j in range(1, 20):
        if i % j != 0:
            not_bad = False
            break
    if not_bad:
        print(i)
        break
