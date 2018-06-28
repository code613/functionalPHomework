import random

random.randint(1,20)  #this way can get random numbers

s = input("enter a string:  ")
D = dict([])
for char in s:
    if char in D:
        D[char] +=1
    else:
        D[char] = 1
print(D)
