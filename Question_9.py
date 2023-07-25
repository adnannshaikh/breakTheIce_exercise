'''
Write a program that accepts sequence of lines as input and
prints the lines after making all characters in the sentence capitalized.
'''
# sent = input()
# sent.upper()
# print(sent)

lst = []
while True:
    x = input()
    if len(x) == 0:
        break
    lst.append(x.upper())
for i in lst:
    print(i)