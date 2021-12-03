with open('input.txt', 'r') as f:
    text = f.read()
input = text.split('\n')

def reverse(gamma_rate):
    epsilon = []
    for i in gamma_rate:
        if i == '1':
            epsilon.append('0')
        elif i == '0':
            epsilon.append('1')
    return (''.join(epsilon))

def part1():
    gamma_rate = []
    for y in range(len(input[0])):
        count_0 = 0
        count_1 = 0
        for x in range(len(input)):
            if input[x][y] == '1':
                count_1 += 1
            elif input[x][y] == '0':
                count_0 += 1
        if count_0 > count_1:
            gamma_rate.append('0')
        elif count_0 < count_1:
            gamma_rate.append('1')
    gamma_rate_str = ''.join(gamma_rate)
    epsilon_str = reverse(gamma_rate_str)
    gamma_rate_int = int(gamma_rate_str, 2)
    epsilon_int = int(epsilon_str, 2)
    print(gamma_rate_int * epsilon_int)



def more_numbers(input, y):
    send = []

    count_0 = 0
    count_1 = 0
    result = '1'
    for x in range(len(input)):
        if input[x][y] == '1':
            count_1 += 1
        elif input[x][y] == '0':
            count_0 += 1
    if count_0 > count_1:
        result = '0'
    elif count_0 < count_1:
        result = '1'
    for i in range(len(input)):
        if input[i][y] == result:
            send.append(input[i])
    return(send)




    print(send)
    return(send)

def less_numbers(input, y):
    send = []

    count_0 = 0
    count_1 = 0
    result = '0'
    for x in range(len(input)):
        if input[x][y] == '1':
            count_1 += 1
        elif input[x][y] == '0':
            count_0 += 1
    if count_0 < count_1:
        result = '0'
    elif count_0 > count_1:
        result = '1'
    for i in range(len(input)):
        if input[i][y] == result:
            send.append(input[i])
    return(send)




    print(send)
    return(send)



def part2():

    y = 0
    put_input = input
    run = True
    again = 0
    while run:
        put_input = more_numbers(put_input, y)

        if len(put_input) == 0:
            again += 1
            y = again
        elif len(put_input) == 1:
            oxygen = put_input[0]
            run = False
        y += 1

    run = True
    y = 0
    put_input = input
    again = 0
    while run:
        put_input = less_numbers(put_input, y)

        if len(put_input) == 0:
            again += 1
            y = again
        elif len(put_input) == 1:
            co2 = put_input[0]
            run = False
        y += 1
    oxygen_int = int(oxygen, 2)
    co2_int = int(co2, 2)
    print(oxygen_int * co2_int)

part1()
part2()




