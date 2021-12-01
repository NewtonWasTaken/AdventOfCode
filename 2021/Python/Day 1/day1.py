with open('input.txt', 'r') as f:
    text = f.readlines()
input = [int(i) for i in text]
result = 0
input2 = []

for y in range(len(input)):
    if y < 3:
        continue
    else:
        #print(input[y - 3], input[y - 2], input[y - 1])
        input2.append(input[y - 3] + input[y - 2] + input[y - 1])

for x in range(len(input2)):
    if x == 0:
        continue
    elif input2[x] > input2[x - 1]:
        result += 1
print(result)