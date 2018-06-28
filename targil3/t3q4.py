#ben marcus 305568867
#chech to see if a number is a Palindrome

def  reverseNum(n):
    x = str(n)
    return  x[::-1]#dose this work???  what would it meen to do [-1,0:-1] it said it was valid

def isPalindrome(n):
    return n == reverseNum(n)
'''something like this'''