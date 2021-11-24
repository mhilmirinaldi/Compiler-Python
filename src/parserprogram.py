import re, sys, CYK

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

    '''Load CNF'''
    CYK.load_cnf('cnf_model.txt')

    '''Tokenize the Code'''
    filename = sys.argv[1]
    codeToken = makeTokenInput(filename)

    '''CYK'''
    cyk_table = CYK.cyk(codeToken)

    if ("S" in cyk_table[-1][-1]):
        print("Accepted")
    else:
        print("Syntax Error")

