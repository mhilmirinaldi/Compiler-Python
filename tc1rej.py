print('Test\n')
print("TEXT GOES HERE")

print("Enter a value of x: ")
x = int(input()

if x > 3:
    print("x is larger than three")
elif x < 3:
    print("x is smaller than three")
else:
    print("x is three")

''' Multiline comment
'''

def text(x):
    ''' another comment '''
    print(x)

def writeHello():
    print('Hello')

print('Enter your name: ')
name = str(input())
writeHello()
print(name)