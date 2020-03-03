while True:
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break
    count = 0
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            c = x - a - b
            if b < c <= n:
                count += 1
    print(count)
