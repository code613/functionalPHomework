#
#eratosthenes.py
#
def napa(N):
    prime = [True]*N #what is the True there for??? ok now i know see next line..
    #print(prime) // ok so what the above line does is it makes 'prime' into a array of 'True' objects
    #
    prime[0] = False
    #make the 'prime' to be an array of True values for the prime numbers
    for i in range(2,N):
        if prime[i]:
            for something in range(i*2,N,i):
                prime[something] = False
    restOfNumbers = []
    for i,item in enumerate(prime):
        if item:
            restOfNumbers.append(i)
    return restOfNumbers
