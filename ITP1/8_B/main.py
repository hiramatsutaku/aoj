def main(text):
    sum = 0
    for char in text:
        sum += int(char)
    return sum


if __name__ == "__main__":
    while True:
        text = str(input())
        if text == '0':
            break
        print(main(text))
