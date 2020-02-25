def calc_area(a, b):
    return a*b


def calc_surrounding_length(a, b):
    return (a+b)*2


if __name__ == "__main__":
    a, b = map(int, input().split())
    print('{} {}'.format(calc_area(a, b), calc_surrounding_length(a, b)))
