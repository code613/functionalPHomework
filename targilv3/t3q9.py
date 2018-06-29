#import targil3.t3q1
#from targil3 import t3q1
import targilv3.t3q1
'''
import targil3.t3q2
import targil3.t3q3
import targil3.t3q4
import targil3.t3q5
import targil3.t3q6
import targil3.t3q7
import targil3.t3q8
'''

#dictionary menu and 1 whould be do targil3 question1
def main():
    #hum maybe should put a while here while key or number is!= 0
    print('''
    enter a number to go to a specific question number in targil 3
    0 to exit
    targil 1 penta number function
    targil 2 sum digits
    targil 3 reverse num
    targil 4 chech to see if a number is a Palindrome
    targil 5 return sigma of i/(i+1) of the number given
    targil 6 return approximation of pi through function to Nth correctness
    targil 7 returns a dictionary prime numbers that are different only by 2
    targil 8 returns a dictionary that is the merge of 3 dictionary's
    and btw dear user this was your menu (in case you were wondering)
    ((you know i love you))
    ''')
    #ok so need to se if there is a wy tpo just run the main there
    #ok now need a dictionarry
    targilDictionary = {1:targilv3.t3q1.mainq1()}
    num  = input("please enter yor number here: ")
    eval(targilDictionary[num])




'''
   n = 10
   print( reverseNum(n))
'''
if __name__ == "__main__":
    main()
