# collection - a variable that holds multiple values

# use dir() on an object to see available methods for that Object Type

total = 0
count = 0
while True:
    i = input('Enter a number: ')
    if i == 'done':
        break

    value = float(i)
    total = total + value
    count = count + 1

average = total / count
print('Average: ', average)


# same as above, but using list and append, note that it has to create a giant list though!
# an argument for the version above is that it only stores one value in memory, the running total.
# i keeps getting assigned new values, the old values become disconnected from a name and ready for
# garbage collection.

nums = []

while True:
    i = input('Enter a number: ')
    if i == 'done':
        break

    nums.append(float(i))

average = sum(nums) / len(nums)

print('Average: ', average)

