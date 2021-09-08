input = open('input2.txt')
program = [int(number) for number in input.readline().split(',')]
o = 0
z = 0
y = 0
def calculate(num1, num2, nums):
    nums[1] = num1
    nums[2] = num2
    idx = 0
    while nums[idx] != 99:
        num = nums[idx]
        val1 = nums[nums[idx + 1]]
        val2 = nums[nums[idx + 2]]
        idx3 = nums[idx + 3]
        if num == 1:
            nums[idx3] = val1 + val2
        elif num == 2:
            nums[idx3] = val1 * val2
        idx += 4
    return nums[0]

for y in range(100):
    for z in range(100):
       if calculate(y, z, program[:]) == 19690720:
           print(100 * y + z)
