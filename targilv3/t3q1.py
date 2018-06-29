#ben marcus 305568867 and tuvya epstein ID unknown (my freind from out of school
#penta number function

#is this function stateless??
def pentaNumRange(n1,n2):
    getPentaNum = lambda x : x*(3*x-1)/2
    return [getPentaNum(num) for num in range(n1,n2)]
def pentaNumRangev2(n1,n2):
    return [(lambda x: x*(3*x-1)/2)(num) for num in range(n1,n2)]

def mainq1():
    print('''hey there fella welcome top targil 3 question one
    what you will be dpoing here is entering 2 numbers and the function will return the Penta Nmber in that range
    please put a first number <  2nd number or else the program will return''')
    n1 = int(input("enter first number  "))
    n2 = int(input("enter 2nd number   "))
    if n1 > n2:
        return
    #print("here are the penta numbers of the range of ",n1," and ",n2," ",pentaNumRange(int(n1),int(n2)))
    for t in range(n1,n2,10):
        #print(t-n1)
        if t<=(n2-10):
            print(pentaNumRange(t,t+10))# + n2 % 10-1 )))
        else:
            print(pentaNumRange(t, (t+ n2 % 10-1 )))
    print('ok thanbk you for joining use for targil 3 question 1')

#commented out and changed name from main to mainq1
'''
if __name__ == "__main__":
    main()
'''

#ok making comment to commit to github