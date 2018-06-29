#ben marcus 305568867 and tuvya epstein
#return approximation of pi through function to Nth correctness
#6/26/18

def iList(n):
    return [(lambda x: (4*(-1)**(x+1)/(2*x - 1)))(num) for num in range (1,n+1)]
def m(n):
    return sum(iList(n))
def asknum():
    theI = int(input('enter a whole positive number for the function '))
    for i in range(1,theI+1):
        print('the number '+ str(i) + " is " + str(m(i)))  #i think we can do this another way....
    return

def main():
    asknum()
    #print('the value for i is '+ )
if __name__ == "__main__":
    main()