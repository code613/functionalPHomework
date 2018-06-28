#this program question 2 of targil 2 was edited by ben marcus 305568867
#what it is supposed to do is take a list of again list's tupals , strings and numbers
#then it will say how manny of each there are
def flatListToTypes(lst):
    dictionary = {'numb':0, 'str':0, 'list':0, 'tuple':0}
    for elem in lst:
        if isinstance(elem,int):
            num = dictionary['numb'] + 1
            dictionary['numb'] = num
        if isinstance(elem,float):
            num = dictionary['numb'] + 1
            dictionary['numb'] = num
        if isinstance(elem,str):
            num = dictionary['str'] + 1
            dictionary['str'] = num
        if isinstance(elem,list):
            num = dictionary['list'] + 1
            dictionary['list'] = num
        if isinstance(elem,tuple):
            num = dictionary['tuple'] + 1
            dictionary['tuple'] = num
    return dictionary




def main():
    lst = eval(input("enter a list "))
    d = flatListToTypes(lst)
    print('total amount of numbers is ', d['numb'])
    print('total amount of strings is ', d['str'])
    print('total amount of lists is ', d['list'])
    print('total amount of tuples is ', d['tuple'])

#i don't understand this line so well...
if __name__ == "__main__":
    main()