#this isn't mine and not so amazing either
"""q1 penta numbers

pentaNumRange(n1,n2)
getpentaNum

bet ask for 2 inputes

print (a,b,c,end = '')
"""
print ('a','b','c',end = '')

def pentaNumRange(n1,n2):
    getpentaNum = lambda n : n*(3*n-1)/2
    #def getpentaNum(n):
    pentaNumsLst = []
    for i in range(n1,n2):
        pentaNumsLst.append(getpentaNum(i))

def pentaNumRange2(n1,n2):
    getpentaNum = lambda n : n*(3*n-1)/2
    return [getpentaNum(i) for i in range(n1,n2)]



def pentaNumRange3(n1,n2):
    getpentaNum = lambda n : n*(3*n-1)/2
    return map(getpentaNum, range(n1,n2))


def main():
    n1 = eval(input("enter the lower limet of the range:  "))
    n2 = eval(input("enter the upper limet of the range:  "))
    Lst = pentaNumRange(n1,n2)
    for i in range(0,len(Lst),10):
        print(Lst [i:i+10])


