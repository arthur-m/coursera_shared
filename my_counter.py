from random import randint

# make a list of random numbers

nums = []

for num in range(1, 11):
    rand_num = randint(1,11)
    nums.append(rand_num)

# build the counter, use get() in the loop.

counted_nums = {}

for val in nums:
    counted_nums[val] = counted_nums.get(val, 0) + 1   # this is the vital pattern right here!

    # the magic here is that this statement works BOTH as (either) creating of a key value pair OR 
    # modification of an existing key value pair. If the key is found, it takes the value for that key
    # and adds 1 to it. If the key is not found, it CREATES that key inside the dictionary and gives it the
    # provided default value, which is 0, and then adds 1 to it. So any 'not found' key then gets added
    # to the dict as key: 'new key name', value: 1. 
    # if it's there, we simply find its value and add 1 to it.

for key, val in counted_nums.items():
    print('Num:{}   Counted:{}'.format(key, val))

print(counted_nums)