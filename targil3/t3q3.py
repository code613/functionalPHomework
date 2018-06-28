#ben marcus 305568867
#reverse num
#bool something = True,some1 = True,some2 = True



#if something and \(some1 or some2):
#    print('something')


def  reverseNum(n):
    x = str(n)
    return  x[::-1]#dose this work???  what would it meen to do [-1,0:-1] it said it was valid
def  main():
    theNumber = int(input('enter a number to reverse please '))
    print('the reverse of the number is ',theNumber)

if __name__ == '__main__':
    main()


