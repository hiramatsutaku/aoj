def main(a, b):
    outputs = ''
    m = len(b)
    for row in a:
        result = 0
        for j in range(m):
            result += row[j]*b[j]
        outputs += '{}\n'.format(result)
    return outputs


if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(n)]
    b = [int(input()) for m in range(m)]
    print(main(a, b), end='')
