num_roads = int(input())
best_road = 0
max_height = -1
for i in range(1, num_roads + 1):
    num_tunnels = int(input())
    min_height = float('inf')
    for _ in range(num_tunnels):
        h = int(input())
        if h < min_height:
            min_height = h
    if min_height > max_height:
        max_height = min_height
        best_road = i
print(best_road, max_height)