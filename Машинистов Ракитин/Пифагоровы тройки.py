import math
n = int(input())
for m in range(2, int(n**0.5) + 2):
    for v in range(1, m):
        a = m * m - v * v
        b = 2 * m * v
        c = m * m + v * v
        if c > n:
            continue
        if math.gcd(math.gcd(a, b), c) == 1:
            triple = sorted([a, b, c])
            print(f"{triple[0]} {triple[1]} {triple[2]}")