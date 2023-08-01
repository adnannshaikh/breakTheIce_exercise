'''
Write a program that accepts a sentence and
calculate the number of upper case letters and lower case letters.
'''

sent = input("Enter a sentense with upper and lower case aplhabets:\n")
upper=[]
lower=[]
for i in sent:
    if i.isupper():
        upper.append(i)
    elif i.islower():
        lower.append(i)

print(f"UPPER CASE:{len(upper)}\nlower case:{len(lower)}")
