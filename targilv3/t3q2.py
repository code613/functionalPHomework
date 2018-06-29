#ben marcus 305568867
#sum digits
def  sumDigits(n):
    #ok this isn't right.
    m = 0
    for num in range(1,abs(n),10):
        m = m+1
    return m

def  sumDigits1(n):
    #return sum(int(list(str(n))))
    #[int(num) for num in list(str(n))]
    return sum([int(num) for num in list(str(abs(n)))])#is abs extra??

def main():
    n1 = sumDigits(int(input("enter a positive or negative number  ")))
    print('the sum of the numbers is '.n1)


if __name__ == "__main__":
    main()