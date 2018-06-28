# myboolfuncs module
#
#question 3 check that numbers then return middle 2 numbers in value (sort)
#else




#this checks if input is a number (comes as a string)


def isNumber(valStr):
    if valStr.count('.') > 1:
        return False
    L = [c for c in valStr if (c.isdigit() or c == '.')]
    return len(L) == len(valStr)


#
def getNumber(prompt):
    while True:
        val = input(prompt)
        if not isNumber(val):
            print("it must be a number!")
        else:
            return eval(val)