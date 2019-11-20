# my answer, done pre-video


# total and average do not need to be None type, you're not checking against largest / smallest,
# you're just summing and getting an average

total = None
count = 0
average = None

print('Enter numbers, then type \'done\' when finished.')

while True:                                                           # start while loop
    
    user_choice = input('> ')                                         # get user input

    if user_choice == 'done':                                         # check if user wants to exit loop
        break
    else:                                                 # user doesn't want to quit, do main loop task
        try:                                                
            user_choice = int(user_choice)                  # try to convert input to int
        except:
            print('You did not enter a digit, try again.')  # didn't work, so restart the while loop
            continue
        else:
            if total == None:                           # if total is None, this is first pass, and we 
                total = user_choice                     # assign first input value to empty total
            else:
                total = total + user_choice             # if total is not None, we do this: 
                                                        # add new input to previous total,
                                                        

    count += 1                              # counter needs to update once per loop
                                            # it will not update if 'continue' was hit, will not update
                                            # on break (duh); does update after either option in the final
                                            # else (total is None, total is not None; counter needs to
                                            # update in either scenario.)

print('Total of all numbers: {}'.format(total))         # print out results
print('# of numbers entered: {}'.format(count))
print('Average of all numbers: {}'.format(int(total / count)))


# coursera video 'worked' answer


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