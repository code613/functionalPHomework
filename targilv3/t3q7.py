#ben marcus 305568867 and tuvya epstein
#returns a dictionary prime numbers that are different only by 2
#wow this problem too wayyyy too long  but finished finally thank the lord above
#6/26/18
def napa(n):
    #make 'prime' to be an array of True values for prime numbers
    prime = [True]*n
    prime[0] = False
    for i in range(2,n):
        if prime[i]:
            for multiple in range(i*2,n,i):#example i = 3 so from 6 to N by 3 (6,9,12...)
                prime[multiple] = False
    result = []
    for i,item in enumerate(prime):
        if item:
            result.append(i)
    return result

#this also worked but for some reason it prints 11: 13 first
def napav2(n):
    #make 'prime' to be an array of True values for prime numbers
    prime = [True]*n
    prime[0] = False
    for i in range(2,n):
        if prime[i]:
            for multiple in range(i*2,n,i):#example i = 3 so from 6 to N by 3 (6,9,12...)
                prime[multiple] = False
    return prime #return ann array of true and false
def twinpv2(n):
    theList = napav2(n)
    result = {}
    for i in range(1,n):
        if theList[i-2] and theList[i]:
            result[i-2] = i
#            result[i+2] = i took this line off as i realized it doesn't really make sence as example 3 can't call 5 and 1 it can only call one number as it is a dictionary
    return result

#ok look WHAT WE JUST FOUND OUT THAT 'X IN S' IS TRUE IF THE VALUE OF X IS IN THE ITEM OF S
#ALSO CAN USE L.INDEX[I] WHICH WOULD HAVE JUST GIVEN ME THE NUMBER OF THE INDEX THAT WAS THE WAY TO GET THE NUMBER
#



def preTwin(n):
    return [num for num in napa(n) (napa(n) == (napa(n+1)-2) or napa(n) == (napa(n-1)+2))]

def twinp(n): # reads dictionary of napa(i,i+1) and opposite if they have a value of 2 apart
    #return dict([[(napa(i),napa(i + 1)),(napa(i),napa(i + 1))] for i in napa(n) if napa[i] is napa[i+1] -2])
    theList = napa(n)
    #return [(theList[i+ 1], theList[i]) for i in range(1,n+1) if theList[i] == (theList[i + 1] + 2)]
    #return [(i,i+2) for i in theList if isinstance(i+2, theList)]
    #return [(theList[int(i+ 1)], theList[int(i)]) for i in range(theList) if i == (theList[int(i) + 1] + 2)]
    return [(i,i+2) for i in theList if theList.count(i+2)>0]

def twinp5(n):
    theList = napa(n)
    return dict([(i,i+2) for i in theList if theList.count(i+2)>0])

'''
def twinp2(n): # reads dictionary of napa(i,i+1) and opposite if they have a value of 2 apart
    theList = []
    theList = napa(n)
    return [((theList[i], theList[i + 1]) for i in range(1,n) if theList[i] is theList[i + 1] - 2)] #range(1, n) not theList
def twinp3(n): # reads dictionary of napa(i,i+1) and opposite if they have a value of 2 apart
    theList = napa(n)
    return [((theList[i], theList[i + 1]) for i in theList if i is (theList[i + 1] - 2))] #range(1, n) not theList

'''

def main():
    theNumber = int(input("enter the positive whole number  "))
    #for i in range(1,theNumber):
    print(twinpv2(theNumber))
'''
    print(twinp(theNumber))
    print(twinp5(theNumber))
'''

if __name__ == "__main__":
    main()
