from math import sqrt, floor


def sieve(n: int):
    arr = [True] * (n + 1)
    arr[0] = arr[1] = False
    for i in range(2, floor(sqrt(n)+1)):
        if arr[i]:
            for j in range(i*i, n+1, i):
                arr[j] = False 
    return arr

total = 0
arr_res = sieve(2000000)
print(sum([i for i in range(0,len(arr_res)) if arr_res[i]]))
