n = int(input())
total_sum = 0
for i in range(1, n+1):
    power = sum(x for x in range(1, i+ 1) if x % 2 == i % 2)
    total_sum += i **power
print(total_sum)