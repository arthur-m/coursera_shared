from random import randint

nums = []

for val in range(1, 11):
    nums.append(randint(1, 11))

minimum = None
maximum = None

for val in nums:
    if minimum == None:
        minimum = val
    else:
        if val < minimum:
            minimum = val

for val in nums:
    if maximum == None:
        maximum = val
    else:
        if val > maximum:
            maximum = val

print(nums)
print(maximum)
print(minimum)