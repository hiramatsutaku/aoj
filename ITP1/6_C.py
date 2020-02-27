def main(inputs):
    outputs = ''
    table = [[[0]*10 for i in range(3)] for i in range(4)]
    for input in inputs:
        b, f, r, v = map(int, input.split())
        table[b-1][f-1][r-1] += v
    for i in range(len(table)):
        if i != 0:
            outputs += '#'*20 + '\n'
        for j in range(len(table[i])):
            for r in range(len(table[i][j])):
                outputs += ' {}'.format(str(table[i][j][r]))
            outputs += '\n'
    return outputs


if __name__ == "__main__":
    n = int(input())
    inputs = [input() for i in range(n)]
    print(main(inputs), end='')
