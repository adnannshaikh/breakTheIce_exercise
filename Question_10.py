'''
Write a program that accepts a sequence of whitespace separated words as input and
prints the words after removing all duplicate words and sorting them alphanumerically.
'''
sent = input("Enter a sentence: ").split()
dup = []
for i in sent:
    if i not in dup:
        dup.append(i)
dup.sort()
print(" ".join(dup))