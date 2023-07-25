'''
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 _ C _ D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
'''
from math import * # importing all math functions
C,H = 50,30

def calc(D):
    D = int(D)
    return str(int(sqrt((2*C*D)/H)))

D = input("Enter numbers").split(',')
D = list(map(calc,D))   # applying calc function on D and storing as a list
print(",".join(D))
