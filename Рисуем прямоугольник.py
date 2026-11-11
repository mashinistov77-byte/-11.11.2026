height = int(input())
width = int(input())
char = input().strip()
for i in range(height):
    if i == 0 or i == height - 1:
        print(char * width)
    else:
        print(char + ' ' * (width - 2) + char)