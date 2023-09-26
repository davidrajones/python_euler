square_sum = pow(sum(range(1, 101)), 2)

sum_square = sum([pow(i, 2) for i in range(1, 101)])

print(square_sum-sum_square)
