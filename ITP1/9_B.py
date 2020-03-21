while True:
    text = input()
    if text == '-':
        break
    for i in range(int(input())):
        param = input()
        text = text[(int(param)):len(text)] + text[0:(int(param))]
    print(text)
