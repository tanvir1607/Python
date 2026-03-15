txt = input()
ans = "None"

for ch in "abcdefghijklmnopqrstuvwxyz":
    if ch not in txt:
        ans = ch
        break
print(ans)





txt = input()
ans = "None"

for ch in range(ord("a"), ord("z") + 1):
    if chr(ch) not in txt:
        ans = chr(ch)
        break
print(ans)




import string

txt = input()
ans = "None"

for ch in string.ascii_lowercase:
    if ch not in txt:
        ans = ch
        break
print(ans)