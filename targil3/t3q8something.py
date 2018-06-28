#a pure function is a function that doesn't change a local variable
#this is supposed to be pure function's

def add3dicts(d1, d2, d3):
    KeyList = lambda d1, d2, d3: list(set(list(d1.keys()) + list(d2.keys()) + list(d3.keys())))

    def func1(k, l):
        if len(l) == 0:
            return []
        if k in l[0]:
            return [l[0][k]] + func1(k, l[1:])
        else:
            return func1(k, l[1:])

    def func2(k):
        l = func1(k, [d1, d2, d3])
        if len(l) == 1:
            return l[0]
        else:
            return tuple(l)

    def func3(lKey):
        if len(lKey) == 0:
            return []
        return [(lKey[0], func2(lKey[0]))] + func3(lKey[1:])

    return dict(func3(KeyList(d1, d2, d3)))


def main():
    #dict1 = dict(input("enter the first list of tuples (as the form of a dictionary)  "))
    #dict2 = dict(input("enter the first list of tuples (as the form of a dictionary)  "))
    #dict3 = dict(input("enter the first list of tuples (as the form of a dictionary)  "))
    dict1 = dict({(1,'a'), (3,'d'), (5,'e')})
    dict2 = dict({(1,'wea'), (4,'dr'), (5,'wee')})
    dict3 = dict({(1,'qwwa'), (4,'ed'), (5,'sdfe')})
    dictCombo =  add3dicts(dict1,dict2,dict3)
    print("the combined dictionary's are",dictCombo )#

if __name__ == "__main__":
    main()