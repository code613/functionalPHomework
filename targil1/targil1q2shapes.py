'''
alright here is my moltiple line comment thing
so this was EDDITED by ben marcus 305568867
here i write the problem / what i am edditing to answwr the question...
'''



#
#  Example program for Targil 1
#
import math
from myboolfuncs import *
#
# Area calculation program
def rectangleArea(w, h):
     return w*h
#
def circleArea(r):
     return math.pi * r**2
#
def ballValume(radius):
    return radius**3*math.pi*4/3
def triangleArea(w, h):
    return w*h*1/2
# printing the menu options
def prtMenu(shapes):
   for i in range(len(shapes)):
      print (i+1, shapes[i])
   return
#sphere
#def
# main program
#
print ("Welcome to the Area calculation program")
print ("---------------------------------------")
# Print out the menu
shapes = ("Rectangle = 1", "Circle = 2","ball = 3","triangle = 4")
while True:
    print ("\nPlease select a shape (press 0 to quit):")
    prtMenu(shapes)
    # Get the user's choice:
    shape = input("> ")
    # Calculate the area:
    if shape == "1":
         height = getNumber("Please enter the height: ")
         width  = getNumber("Please enter the width: ")
         area = rectangleArea(width, height)
         print ("The area is", area)
         continue
    elif shape == "2":
         radius = getNumber("Please enter the radius: ")
         area   = circleArea(radius)
         print ("The area is", area)
         continue
    elif shape == "3":
         radius = getNumber("Please enter the radius: ")
         area = ballValume(radius)
         print("The area is", area)
         continue
    elif shape == "4":
         height = getNumber("Please enter the height: ")
         width = getNumber("Please enter the width: ")
         area = triangleArea(width, height)
         print("The area is", area)
         continue
    elif shape == "0":
         print ("Bye!")
         break
    else:
         print ("Invalid shape")


         #
