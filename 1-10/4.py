def is_palindrome(n) -> bool:
    str_no = f"{n}"
    return str_no == str_no[::-1]


max_no = 0

for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        no = i * j
        if is_palindrome(no) and no > max_no:
            max_no = no
        if no < 999:
            break
print(max_no)
