# refactoring of my version to remove unnecessary 'else' sections, remove use of None for the
# variables (not needed for a summing / average function), and resulting code is nearly identical
# to shorter 

total = 0
count = 0

while True:                                                              
    user_choice = input('> ')                                         
    if user_choice == 'done':                                        
        break
    try:                                                
        user_choice = int(user_choice)                  
    except:
        print('You did not enter a digit, try again.')  
        continue
             
    total = total + user_choice             
    count += 1           

print('Total of all numbers: {}'.format(total))         # print out results
print('# of numbers entered: {}'.format(count))
print('Average of all numbers: {}'.format(int(total / count)))



# class version

num = 0             # running count
tot = 0.0           # running total

while True:
   string_val = input('Enter a number: ')
   if string_val == 'done':
       break
   try:
       fval = float(string_val)
   except:
       print('You did not enter valid input, try again.')
       continue

   num = num + 1           # counter pattern
   tot = tot + fval        # accumulator pattern

print(tot, num, tot/num)