def main(N, M, L, a, b):
    results = [[0]*L for i in range(N)]
    for n in range(N):
        for l in range(L):
            for m in range(M):
                results[n][l] += a[n][m]*b[m][l]
    results = [" ".join(map(str, i)) for i in results]
    return '\n'.join(map(str, results))


if __name__ == "__main__":
    N, M, L = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(N)]
    b = [list(map(int, input().split())) for j in range(M)]
    print(main(N, M, L, a, b))
