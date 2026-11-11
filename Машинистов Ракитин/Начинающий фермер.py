m = int(input())
t = int(input())

for b in range(1, m // 20 + 1):
    for i in range(m // 10 + 1):
        c = t - b - i
        if c < 0:
            continue
        n = b * 20 + i * 10 + c * 5
        if n == m:
            print(b, i, c)