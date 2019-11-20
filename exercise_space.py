score = input('Enter Score: ')

try:
    f_score = float(score)
except:
    print('You did not enter a numerical value.')
else:
    if f_score < 0.0 or f_score > 1.0:
        print('Error: input value not between 0.0 and 1.0')
    else:
        if f_score >= 0.9:
            print('A')
        elif f_score >= 0.8 and f_score < 0.9:
            print('B')
        elif f_score >= 0.7 and f_score < 0.8:
            print('C')
        elif f_sccore >= 0.6 and f_score < 0.8:
            print('D')
        elif f_score < 0.6:
            print('F')




def print_thing():
    return 'Thing'


print(print_thing())        # print_thing() evaluates to 'Thing' 
                    # so this line of code becomes: print('Thing') after the function call is complete.
                    # always think through: what does a function call *literally evaluate to* and then
                    # read the line of code that has the function call in it again, this time replacing
                    # the function call with whatever it evaluates to. RUN-TIME BRAIN.