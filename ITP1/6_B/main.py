def main(inputs):
    outputs = ''
    dict = {}
    pics = ['S', 'H', 'C', 'D']
    for p in pics:
        dict[p] = list(map(int, range(1, 14)))
    for input in inputs:
        parsed = input.split()
        pic = str(parsed[0])
        num = int(parsed[1])
        dict[pic].remove(num)
    for p in pics:
        for n in dict[p]:
            outputs += '{} {}\n'.format(p, n)
    return outputs


if __name__ == "__main__":
    n = int(input())
    inputs = [input() for i in range(n)]
    print(main(inputs), end='')
