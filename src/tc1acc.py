import sys

_x = sys.argv[1]

def writeHello():
    print(_x)

print('Enter your name: ')
name = str(input())
writeHello()
print(name)

''' comment '''