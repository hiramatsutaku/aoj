import re


def main(text):
    hash = {}
    keys = 'abcdefghijklmnopqrstuvwxyz'
    for k in keys:
        hash[k] = 0
    for char in re.findall('[a-zA-Z]', text):
        hash[char.lower()] += 1
    return list(map(lambda k: '{} : {}'.format(k, hash[k]), keys))


if __name__ == "__main__":
    text = ''
    while True:
        try:
            input_str = str(input())
        except EOFError:
            break
        text += input_str
    results = main(text)
    print('\n'.join(results))
