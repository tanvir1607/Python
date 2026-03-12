test = int(input())
for _ in range(test):
    size = int(input())
    lst = list(map(int, input().split()))
    pair = lst.count(1) // 2
    print(size - pair)