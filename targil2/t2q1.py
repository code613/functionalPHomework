def flatList(lst,type):
    for elem in lst:
        if isinstance(elem,type):
            yield elem

def isInListOrTuple(elem,lst,tup):
    return elem in lst or elem in tup

def makeListOfTuples(lst):
    return list(elem for tup in flatList(lst,tuple) for elem in tup)
#put's an elem in the list that is found in tup wich itself is found in flatlist()

def makeTupleOfLists(lst):
    return tuple(elem for tup in flatList(lst,list) for elem in tup)

def makeListOfString(lst):
    l = makeListOfTuples(lst)
    t = makeTupleOfLists(lst)
    return list(elem for elem in flatList(lst, str) if not isInListOrTuple(elem,l,t))

def makeListOfNumbers(lst):
    l = makeListOfTuples(lst)
    t = makeTupleOfLists(lst)
    return tuple(elem for elem in flatList(lst, (int, float, complex)) if not isInListOrTuple(elem,l,t))

def main():
    lst = eval(input("enter a list "))
    print("list of tuples ", makeListOfTuples(lst))
    print("tuple of lists ", makeTupleOfLists(lst))
    print("list of strings ", makeListOfString(lst))
    print("tuple of numbers ", makeListOfNumbers(lst))

if __name__ == "__main__":
    main()
