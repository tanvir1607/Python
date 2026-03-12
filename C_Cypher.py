test = int(input())
for _ in range(test):
    size = int(input())
    lst = list(map(int, input().split()))
    for i in range(size):
        _, txt = input().split()
        for char in txt:
            lst[i] = (lst[i] + (1 if char ==  "D" else - 1)) % 10
    print(*lst)
