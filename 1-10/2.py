nos = [1, 2]
tot = 0
while 1:
    if min(nos) > 4000000:
        break
    if nos[0] % 2 == 0 and nos[0] <= 4000000:
        tot += nos[0]
    if nos[1] % 2 == 0 and nos[1] <= 4000000:
        tot += nos[1]

    nos[0] = sum(nos)
    nos[1] = sum(nos)
print(tot)
