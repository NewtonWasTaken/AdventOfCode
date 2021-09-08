input = open('input1.txt')
numbers = input.read().splitlines()
mass = [int(i) for i in numbers]
fuel = []
o = 0
total = 0
for x in mass:
 result2 = x
 while result2 >= 0:
  result = result2 // 3
  result2 = result - 2
  if result2 < 0:
      continue
  else:
      fuel.append(result2)
for y in fuel:
    total = total + fuel[o]
    o = o + 1
print(total)













