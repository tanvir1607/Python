test = int(input())
for _ in range(test):
    a, b, c = map(int, input().split())
    print("+" if a + b == c else "-")