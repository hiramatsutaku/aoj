taro = 0
hanako = 0
for i in range(int(input())):
    line = str(input()).split()
    t = line[0]
    h = line[1]
    if (t == h):
        taro += 1
        hanako += 1
    elif (t < h):
        hanako += 3
    elif (t > h):
        taro += 3

print('{} {}'.format(taro, hanako))
