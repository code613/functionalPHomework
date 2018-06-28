
def trainglePoints(x,y,z):
    if ((x+y)>z and (y+z)>x and (x+z)>y):
        print("they are correct triangle sides lengths".center(40))
    else:
        print("they are in error.".center(20))

print ('enter 3 numbers')
#take in  3 numbers
x = int( input("please enter first of 3 numbers to see if it fits in a triangle "))
y = input("second number ")
z = int( input("last number "))
trainglePoints(x,int(y),z)