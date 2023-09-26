val = 1000

# a + b + c = 1000
# a < b < c

# ar = range(1, 999)
# br = range(2, 1000)
# cr = range(3, 1001)

# The Pythagorean triples formula can be given as,

# a = m2- n2
# b = 2mn
# c = m2+ n2

# a, b = Base, and perpendicular of a right-angled triangle
# c = Hypotenuse of a right-angled triangle
# m, n are any two positive integers; m > n
# m and n are coprime and both should not be odd numbers

for a in range(1, 999):
    b = a + 1
    c = b + 1
    while c <= 1000:
        while (c * c) < ((a * a) +(b * b)):
            c += 1
        if (c * c) == ((a * a) +(b * b)) and c < 1000 and a+b+c == 1000:
            print(a * b * c)
            exit(0)
        b += 1
