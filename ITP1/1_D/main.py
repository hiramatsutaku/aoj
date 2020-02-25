def format(second):
    h = second // (60*60)
    t = (second // 60) % 60
    s = ((second % 60) % 60) % 60
    return('{}:{}:{}'.format(h, t, s))


if __name__ == "__main__":
    _second = int(input())
    print(format(_second))
