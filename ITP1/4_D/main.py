def calc(n, arr):
    min = arr[0]
    max = arr[0]
    sum = arr[0]
    for i in range(n - 1):
        target = arr[i + 1]
        if target < min:
            min = target
        if target > max:
            max = target
        sum += target

    return '{} {} {}'.format(min, max, sum)


if __name__ == "__main__":
    n = input()
    arr = list(map(int, input().split()))
    print(calc(int(n), arr))
