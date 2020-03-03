import re


def main(s, p):
    sequence = s + s
    if re.search(p, sequence):
        return 'Yes'
    else:
        return 'No'


if __name__ == "__main__":
    s = input()
    p = input()
    print(main(s, p))
