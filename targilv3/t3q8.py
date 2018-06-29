#ben marcus 305568867 and tuvya epstein
#returns a dictionary that is the merge of 3 dictionary's
#6/27/18
def addict(dict1,dict2,dict3):
    set1 = set(dict1.keys())
    set2 = set(dict2.keys())
    set3 = set(dict3.keys())
    set4 = set1 | set2 | set3

    tempDict = {}
    for i in set4:
        tempSet = []
        if i in dict1:
            tempSet.append(dict1[i])
        if i in dict2:
            tempSet.append(dict2[i])
        if i in dict3:
            tempSet.append(dict3[i])
        tempDict[i] = tempSet
    return tempDict
    #   [(1,'a'), (3,'d'), (5,'e')]

def main():
    #dict1 = dict(input("enter the first list of tuples (as the form of a dictionary)  "))
    #dict2 = dict(input("enter the first list of tuples (as the form of a dictionary)  "))
    #dict3 = dict(input("enter the first list of tuples (as the form of a dictionary)  "))
    dict1 = dict({(1,'a'), (3,'d'), (5,'e')})
    dict2 = dict({(1,'wea'), (4,'dr'), (5,'wee')})
    dict3 = dict({(1,'qwwa'), (4,'ed'), (5,'sdfe')})
    dictCombo =  addict(dict1,dict2,dict3)
    print("the combined dictionary's are",dictCombo )#

if __name__ == "__main__":
    main()