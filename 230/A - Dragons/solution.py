s, n = map(int, input().split())
arr = []
for i in range(0, n):
    x, y = list(map(int,input().split()))
    arr.append((x, y))
arr.sort()
success = True
for x , y in arr:
    if s > x:
        s += y
    else:
        success = False
        print("NO")
        break
if success:
    print("YES")        