#retyping from the slides

import math
def calculateDescrimint(a,b,c):
    return b**2 - 4*a*c

def calculateRoot(a,b,Descrimint):
    term = -b/(2*a)#can put this in to the elif to make stateless (i think)
    if Descrimint == 0:
        return -b/(2*a)
    elif Descrimint > 0:
        return (term + math.sqrt(Descrimint)/(2*a)) , (term - math.sqrt(Descrimint)/(2*a))
    else:
        return None

def printSolution(roots):
    if roots is None:
        print('no real solution (iow use imagination)')
    elif isinstance(roots , (int,float)):
        print('there is only one real solution it is ',)#what is this comma doing here??
        print(roots)
    else:
        print('the 2 real solutions are  ',roots)

def main():
    a = float(input("enter the value of a "))
    b = float(input("enter the value of b "))
    c = float(input("enter the value of c "))
    print('\n'*5)#this should print 5 lines
    Descrimint = calculateDescrimint(a,b,c)
    print('this is what you have  ',Descrimint)
    solution = calculateRoot(a,b,Descrimint)
    printSolution(solution)

if __name__ == "__main__":
    main()




