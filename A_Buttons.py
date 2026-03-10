a, b = map(int, input().split())
ans = max(a, b) + max(max(a, b) - 1, min(a, b))
print(ans)