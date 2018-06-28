from random import randint

def nihushTest(numbers,*args):
    lst = []
    for i in range(len(numbers)):
        if numbers[i] == args[i]:
            lst.append(numbers[i])
        else:
            lst.append("X")
    return tuple(lst)


N = int(input("enter N between 3 and 9 - "))
numbers = tuple(randint(0,9) for i in range(N))
print(numbers)
maxSuccessNihush = 0
while True:
    print("enter " + str(N) + "numbers ")
    lst = []
    num = None
    for i in range(N):
        num = int(input("enter number " + str(i+1) + " "))
        if num == -1:
            break
        lst.append(num)
    if num == -1:
        break
    userNumbers = tuple(lst)
    nihushNumbers = nihushTest(numbers, *(i for i in userNumbers))
    numX = nihushNumbers.count('X')
    successRate = (len(nihushNumbers)-numX)/N
    if maxSuccessNihush < successRate:
        maxSuccessNihush = successRate
    print("nihush: {0}, success rate: {1}".format(nihushNumbers,successRate))
    if successRate == 1:
        break
print("numbers are : ", numbers)
print("max success rates is : ",maxSuccessNihush)
