def sort(a, b, c):
    arr = [a, b, c]

    if arr[0] > arr[1]:
        arr[0], arr[1] = arr[1], arr[0]
    if arr[1] > arr[2]:
        arr[1], arr[2] = arr[2], arr[1]
    if arr[0] > arr[1]:
        arr[0], arr[1] = arr[1], arr[0]
    return ' '.join(map(str, arr))


if __name__ == "__main__":
    a, b, c = map(int, input().split())
    print(sort(a, b, c))
