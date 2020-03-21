target = input()
count = 0

while True:
    line = input()
    if line == 'END_OF_TEXT':
        break
    words = line.lower().split()
    count += words.count(target.lower())

print(count)
