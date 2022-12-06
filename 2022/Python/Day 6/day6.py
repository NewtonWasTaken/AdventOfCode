input = open("input.txt")
text = list(input.read())

for x in range(3, len(text)):
    test = set()
    for y in range(4):
        test.add(text[x-y])
    if len(test) == 4:
        print(x+1)
        break

for x in range(3, len(text)):
    test = set()
    for y in range(14):
        test.add(text[x-y])
    if len(test) == 14:
        print(x+1)
        break