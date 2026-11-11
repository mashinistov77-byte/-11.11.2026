n = int(input())
curr = 1
row_len = 1
while curr <= n:
    row = []
    for _ in range(row_len):
        if curr <= n:
            row.append(str(curr))
            curr += 1
    print(' '.join(row))
    row_len += 1