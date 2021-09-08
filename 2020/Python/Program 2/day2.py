with open("input2.txt", "r") as f:
    strings = f.readlines()

eachline = [i.split("\n")[0] for i in strings]
# print(eachline)
passwords = []
indexes = []
value1 = []
value2 = []
o = 0
v = 0
result = 0
finalresult = 0
result1 = 0
finalresult1 = 0
for i in eachline:
    key, value = i.split(': ')
    values, index = key.split(' ')
    num1, num2 = values.split('-')
    passwords.append(value)
    indexes.append(index)
    value1.append(num1)
    value2.append(num2)

for l in range(0, len(value1)):
    value1[l] = int(value1[l])
for j in range(0, len(value2)):
    value2[j] = int(value2[j])

for z in passwords:
    for x in z:
        if indexes[o] == x:
            result = result + 1
        else:
            continue

    if value1[o] <= result <= value2[o]:
        finalresult = finalresult + 1
    o = o + 1
    result = 0
for y in passwords:
   if indexes[v] == y[value1[v] - 1]:
       result1 = result1 + 1
   if indexes[v] == y[value2[v] - 1]:
       result1 = result1 + 1
   if result1 == 1:
       finalresult1 = finalresult1 + 1
   v = v + 1
   result1 = 0

print(f'Part 1: {finalresult}')
print(f'Part 2: {finalresult1}')
