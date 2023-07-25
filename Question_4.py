'''
Write a program which accepts a sequence of comma-separated numbers from console and
generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
'''


num_list = input("Enter some numbers: ").split(',')
print(num_list)
tup = tuple(num_list)
print(tup)
