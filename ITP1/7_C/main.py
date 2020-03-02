def main(r, c, inputs):
    csum = [0]*(c+1)
    for input in inputs:
        input.append(sum(input))
        for i in range(len(input)):
            csum[i] += input[i]
    inputs.append(csum)
    row = [" ".join(map(str, i)) for i in inputs]
    return '\n'.join(map(str, row))


if __name__ == "__main__":
    r, c = map(int, input().split())
    inputs = [list(map(int, input().split())) for i in range(r)]
    print(main(r, c, inputs))
