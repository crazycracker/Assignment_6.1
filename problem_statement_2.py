import numpy as np

'''
    array: numpy array
    N    : Number of columns in the output
           In general N is optional, if N is not provided by default it would be len(x)
    increasing: 
           Order of the powers of the columns.  If True, the powers increase 
           from left to right, if False (the default) they are reversed.

    Step 1: Enter the number of elements of the array
    Step 2: Enter the elements of the array
    Step 3: Enter the value of N
'''
print("Enter the number of digits to be entered")
n = (int)(input())
l = list()

for x in range(0,n):
    k = (int)(input())
    l.append(k)
print("Enter the value of N")
N = (int)(input())
array = np.array(l)
print(np.vander(array,N,False))

