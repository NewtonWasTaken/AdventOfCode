input = open("input.txt")
text = input.read().splitlines()
common = []
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet += alphabet.upper()
result = 0

for x in range(len(text)):
    first_half = ""
    second_half = ""
    common_cache = ""
    for y in range(len(text[x])):
        if y >= len(text[x])/2:
            if text[x][y] in first_half and text[x][y] not in common_cache:
                common.append(text[x][y])
                common_cache += text[x][y]
            second_half += text[x][y]

        else:
            first_half += text[x][y]

for i in common:
   result += alphabet.rfind(i) + 1
print(result)

common = []
result = 0
for x in range(len(text)):
    common_cache = ""
    if ((x + 1) % 3) == 0:
        for y in range(len(text[x])):
                if (text[x][y] in text[x-1]) and text[x][y] not in common_cache:
                    if text[x][y] in text[x-2]:
                        common.append(text[x][y])
                        common_cache += text[x][y]


for i in common:
   result += alphabet.rfind(i) + 1
print(result)