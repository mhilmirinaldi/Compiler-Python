import re
import sys


'''Tokenize Code'''
def makeTokenInput(filename):
    f = open(filename, 'r')
    file = f.read()
    file = file.split()
    f.close()

    res = file
    operators = [':', ',', '=', '<', '>', '>=', '<=', '==', '!=', r'\+', '-', r'\*', '/', r'\*\*', r'\(', r'\)',r'\'\'\'', r'\'', r'\"']

    for operator in operators :
        temp = []
        for stat in res :
            format = r"[A..z]*(" + operator + r")[A..z]*"
            resTemp = re.split(format, stat)

            for split in resTemp:
                temp.append(split)
        res = temp
    
    temp = []
    for statment in res :
        if statment != '' :
            temp.append(statment)
        res = temp

    return res




'''Main Program'''
if __name__ == '__main__' :

    filename = sys.argv[1]
    '''Load CNF'''

    '''Tokenize the Code'''
    codeToken = makeTokenInput(filename)
    print(codeToken)

    '''CYK'''

