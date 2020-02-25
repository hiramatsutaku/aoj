def is_in(W, H, x, y, r):
    x_min = r
    x_max = W - r
    y_min = r
    y_max = H - r
    if x_min <= x <= x_max and y_min <= y <= y_max:
        return 'Yes'
    return 'No'


if __name__ == "__main__":
    W, H, x, y, r = map(int, input().split())
    print(is_in(W, H, x, y, r))
