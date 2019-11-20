# in an if, elif, else structure, only ONE of them will execute, and something will always
# execute (with else as the catch-all).

# if there's no 'else', it's possible that nothing will execute.

rawstr = input('Enter a number:')
try:
    ival = int(rawstr)
except:
    ival = -1           # -1 value used as flag to show an error occured

if ival > 0:                # less than zero means error...
    print('Nice Work')
else:
    print('Not a number')   # so show that an error occurred 


    

