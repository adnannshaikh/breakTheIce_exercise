'''
Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''

class stringPlay():
    def getString(self):
        self.string_value = input("Enter a sentence: ")

    def printString(self):
        print(self.string_value.upper())


x = stringPlay()
x.getString()
x.printString()