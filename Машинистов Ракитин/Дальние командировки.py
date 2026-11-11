n = int(input())
t = 0
m = 0

while t < n:
    m += 1
    t += len(str(m))

print(m)