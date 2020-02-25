def convert(a, b):
    if a > b:
        return('a > b'.format(a, b))
    elif a < b:
        return('a < b')
    return('a == b')


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(convert(a, b))
