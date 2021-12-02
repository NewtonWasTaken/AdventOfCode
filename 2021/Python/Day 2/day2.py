with open('input.txt', 'r') as f:
    text = f.readlines()
input = [i.split() for i in text]

def part1(input, horizontal, depth):
    for i in range(len(input)):
        for m in range(len(input[i])):
            if input[i][m] == 'forward':
                horizontal += int(input[i][m + 1])
            elif input[i][m] == 'down':
                depth += int(input[i][m + 1])
            elif input[i][m] == 'up':
                depth -= int(input[i][m + 1])
    print(horizontal * depth)
def part2(input, horizontal, depth, aim):
    for i in range(len(input)):
        for m in range(len(input[i])):
            if input[i][m] == 'forward':
                horizontal += int(input[i][m + 1])
                depth += aim * int(input[i][m + 1])
            elif input[i][m] == 'down':
                aim += int(input[i][m + 1])
            elif input[i][m] == 'up':
                aim -= int(input[i][m + 1])
    print(horizontal * depth)
part1(input, 0, 0)
part2(input, 0, 0, 0)

