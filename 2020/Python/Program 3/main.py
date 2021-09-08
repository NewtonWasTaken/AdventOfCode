with open('input.txt', 'r') as f:
    data = [x.strip() for x in f.readlines()]
def part1():
    x = 0
    trees = 0
    for y in range(len(data)):
        if data[y][x] == '#':
             trees += 1
        x = (x + 3) % len(data[0])
    print(trees)

def part2():
    slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]

    trees_list = []
    for i in slopes:
        trees = 0
        add_x = i[0]
        add_y = i[1]
        curr_x = 0
        for i in range(len(data)):
            if i % add_y != 0:
                continue
            if data[i][curr_x] == '#':
                trees += 1
            curr_x = (curr_x + add_x) % len(data[0])
        trees_list.append(trees)
    result = 1
    for m in trees_list:
        result = result * m
    print(result)
part1()
part2()