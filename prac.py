nums = [0,1,12,3,0,4]
zeroes = []

for i in nums:
    if i == 0:
        nums.remove(i)
        zeroes.append(i)
print(nums+zeroes)