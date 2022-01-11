value = input("Welcome to the menu.Options are listed below:\n\t 1.Roll \n\t 2.Sweep \n\t 3.Scroll \n\t Type the number of your choice and press Enter.")

def func1(val):
    return val**val
def func2(val):
    return val**val
def func3(val):
    return val**val

while True:
    if value.isdigit() == True: #.isdigit()
        value = int(value)
        if value > 3 or value < 1 :#if value is outside of our range :
            value = input ("Please input a number between 1 and 3 .")
            continue #skip rest of loop , start from isdigit() check again
        else:
             break #on correct value datatype:exit the loop
    else:
        value =input("Invalid input ! Please provide an integer.") #ask for a new value

#compare numeric value to choices available , perform associiated function or sequence
if value == 1:
    func1(value)
elif value == 2:
    func2(value)
elif value == 3:
    func3(value)
