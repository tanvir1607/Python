test = int(input())
for _ in range(test):
    size = int(input())
    txt1 = input().replace("B", "G")
    txt2 = input().replace("B", "G")
    print("YES" if txt1 == txt2 else "NO")