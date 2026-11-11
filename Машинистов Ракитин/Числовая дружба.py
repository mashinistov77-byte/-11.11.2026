def sum_divisors(num):
    s = 0
    for d in range(1, num // 2 + 1):
        if num % d == 0:
            s += d
    return s

for a in range(2, 10000):
    b = sum_divisors(a)
    if a < b < 10000:
        if sum_divisors(b) == a:
            print(a, b)