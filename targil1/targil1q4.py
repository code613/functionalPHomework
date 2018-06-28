#edetted by ben marcus
#305568867
#4 functions to m ove binary numbers

#this function moves the binary numbers left by n bits replacing with 0's on right most side
def shiftL(binNr,n):
    return binNr[n:] + '0'*n
#this function moves the binary numbers right by n bits replacing with 0's on left most side
def shiftR(binNr,n):
    return '0'*n + binNr[:-n]
#this function moves the binary numbers left chaining in fallen numbers
def shiftCL(binNr,n):
    l = binNr[0:n]
    return binNr[n:] + l
#this function moves the binary numbers right chaining in fallen numbers
def shiftCR(binNr,n):
    l = binNr[-n:]
    return l + binNr[:-n]



print(shiftL("110001110",2)  +'  110001110  shiftL   moved 2 ')
print(shiftR("110001110",2)  +'  110001110 shiftR    moved 2 ')
print(shiftCL("110001110",2) +'  shiftCL 110001110   moved 2 ')
print(shiftCR("110001110", 2)+'  shiftCR 110001110   moved 2 ')
