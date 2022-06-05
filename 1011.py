t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    distance = y - x
    n=0
    while True:
        if distance <= n * (n + 1):
            break
        else:
            n += 1
    if distance <= n * n:
        print(2 * n - 1)
    else:
        print(2 * n)