def main(text):
    result = ''
    for t in text:
        if t.isupper():
            result += t.lower()
        elif t.islower():
            result += t.upper()
        else:
            result += t
    return result


if __name__ == "__main__":
    print(main(input()))
