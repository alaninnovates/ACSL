numsIn = input('Please input an list of numbers: ')
target = input('Please input a target: ')

nums = numsIn.split()

for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        if int(nums[i]) + int(nums[j]) == int(target):
            print(i, j)
