''' Svita Kiran
09/13/23
CS 152 A
Project 01
Program for first CS152 project
'''
#VERSION 1
print('version 1')
print('sum', 42 + 21 + 5)
print('avg', (42 + 21 + 5) / 3)

def myfunction(a, b, c):
    print('sum', a + b + c)

myfunction(4, 5, 6)


#VERSION 2
print('version 2')
print('sum', 42 + 21 + 5)
print('avg', (42 + 21 + 5) // 3)

myfunction(4, 5, 6)


#VERSION 3
print('version 3')
print('sum', 42 + 21 + 5.0)
print('avg', (42 + 21 + 5) // 3.0)

myfunction(4, 5, 6)


#VERSION 4
a = 42
b = 21
c = 5
print('version 4')
print('sum', a + b + c)
print('avg', (a + b + c) / 3.0)

myfunction(4, 5, 6)


#VERSION 5
a = input("Enter first number: ")
a = int(a)
b = input("Enter second number: ")
b = int(b)
c = input("Enter last number: ")
c = int(c)

print('version 5')
print('sum', a + b + c)
print('avg', (a + b + c) / 3.0)

myfunction(4, 5, 6)

#VERSION 6
def stats(a, b, c):
    print('version 6')
    print('sum', a + b + c)
    print('avg', (a + b + c) / 3.0)
    myfunction(4, 5, 6)

stats(42, 21, 5)
stats (3, 36, 14)