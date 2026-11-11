cols = int(input())
rows = int(input())
for i in range(1, rows + 1):
    row = []
    for j in range(1, cols + 1):
        row.append(str(j / i))
    print(' '.join(row))