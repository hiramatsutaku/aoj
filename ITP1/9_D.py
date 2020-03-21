str = input()
for i in range(int(input())):
    line = input().split()
    formula = line[0]
    left = int(line[1])
    right = int(line[2]) + 1
    if (formula == 'print'):
        print(str[left:right])
    elif (formula == 'reverse'):
        str = str[:left] + str[left:right][::-1] + str[right:]
    elif (formula == 'replace'):
        str = str[:left] + line[3] + str[right:]
