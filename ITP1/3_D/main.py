def count_divisor(a, b, c):
    count = 0
    value = a
    while value <= b:
        if c % value == 0:
            count += 1
        value += 1
    return count


if __name__ == "__main__":
    a, b, c = map(int, input().split())
    print(count_divisor(a, b, c))
