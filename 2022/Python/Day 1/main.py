input = open("input.txt")
text = input.read().split("\n\n")
final_list = [i.split("\n") for i in text]
order = []
for x in final_list:
    result = 0
    for y in x:
        result += int(y)
    order.append(result)

order.sort(reverse=True)
print(order[0] + order[1] + order[2])
