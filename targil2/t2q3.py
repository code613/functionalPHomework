import os
import re

def splitFile(fileList):
    d = {}
    for elem in fileList:
        if elem is "\n":
            continue
        lst = elem.split(" ")
        for ele in lst:
            if ele is "," or ele is "." or ele is ";" or ele is "?" or ele is "!" or ele is "\n" or ele is ":":
                continue
            a = ele[-1:]
            if a is "," or a is "." or a is ";" or a is "?" or a is "!" or a is "\n" or a is ":":
                b = a[-1:]
                if b is "," or b is "." or b is ";" or b is "?" or b is "!" or b is "\n" or b is ":":
                    continue
                else:
                    ele = ele[0:-1]
            if ele in d:
                num = d[ele] + 1
            else:
                num = 1
            d[ele] = num
    return d

fn = os.path.join(os.path.dirname(__file__), 'shakespeare.txt')
txtobj = open(fn,'r')
txtFile = txtobj.readlines()
d = splitFile(txtFile)
for key, value in d.items():
    print(key + "  :  " + str(value))