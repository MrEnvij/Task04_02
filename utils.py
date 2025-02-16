def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def convert_base(number, from_base, to_base):
    decimal = 0
    power = 0
    while number > 0:
        decimal += (number % 10) * (from_base ** power)
        number //= 10
        power += 1
    result = 0
    place = 1
    while decimal > 0:
        result += (decimal % to_base) * place
        decimal //= to_base
        place *= 10
    return result

A	B	C	F
0	0	0	1
0	0	1	0
0	1	0	1
0	1	1	0
1	0	0	1
1	0	1	0
1	1	0	1
1	1	1	1
/ if n < 2:\n return false
