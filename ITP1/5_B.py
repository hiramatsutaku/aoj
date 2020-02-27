while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    print("#"*w)
    for j in range(h-2):
        print("#{}#".format("."*(w-2)))
    print("#"*w)
    print()
