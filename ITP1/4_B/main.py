import math


def calc(r):
    area = r*r*math.pi
    circumference = 2*math.pi*r
    return '{:.6f} {:.6f}'.format(area, circumference)


if __name__ == "__main__":
    r = float(input())
    print(calc(r))
