hrs = input("Enter hours:")
rate = input("Enter rate:")

try:
    h = float(hrs)
    r = float(rate)

# note, no error type is given here; it will simply run the except block
# if the try fails -- it's not required to specify error type.    
except:
    print("Error, please enter numeric input")

else:
    if h <= 40:
        print(h * r)
    elif h > 40:
        extra_hours = h - 40
        new_rate = r * 1.5

        total = (40 * r) + (extra_hours * new_rate)
        print(total)


