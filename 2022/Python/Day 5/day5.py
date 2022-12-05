input = open("input.txt")
text = input.read().split("\n")
table_raw = text[0:8]
table = [[] for i in range(9)]

for x in range(len(table_raw)):
    y = 1
    index = 0
    while y < len(table_raw[x]):
        if table_raw[x][y] != " ":
            table[index].append(table_raw[x][y])
        y += 4
        index += 1

instructions_raw = text[10:]

for i in range(len(instructions_raw)):
    instructions_raw[i] = instructions_raw[i].replace("move ", "")
    instructions_raw[i] = instructions_raw[i].replace(" from ", ",")
    instructions_raw[i] = instructions_raw[i].replace(" to ", ",")


instructions = [j.split(",") for j in instructions_raw]

for x in range(len(instructions)):
    move_cache = table[int(instructions[x][1]) - 1][:int(instructions[x][0])]
    table[int(instructions[x][1]) - 1] = table[int(instructions[x][1]) - 1][int(instructions[x][0]):]
    #move_cache.reverse() //add this to print part 2
    for i in move_cache:
        table[int(instructions[x][2]) - 1].insert(0, i)

for x in table:
    print(x[0], end ="")


