def calc(a, b):
    d = a // b
    r = a % b
    f = a / b
    return '{} {} {:.5f}'.format(d, r, f)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(calc(a, b))
