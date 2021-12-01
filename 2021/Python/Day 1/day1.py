with open('input.txt', 'r') as f:
    text = f.readlines()
input = [int(i) for i in text]

def part1(input, result):
    for x in range(len(input)):
        if x == 0:
            continue
        elif input[x] > input[x - 1]:
            result += 1
    print(result)
def part2(input, result):
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
part1(input, 1)
part2(input, 1)