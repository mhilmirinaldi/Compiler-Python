import re

global grammar
grammar = {}

def load_cnf(file_name):
    file = open(file_name).read()
    rules = file.split('\n')

    for i in range (len(rules)-1):
        x = rules[i].split(' -> ')[0]
        y = rules[i].split(' -> ')[1]
        y = y.replace(" ","")
        z = y.split('|')
        for j in range (len(z)):
            value = grammar.get(z[j])
            if (value == None):
                grammar.update({z[j] : [x]})
            else :
                grammar[z[j]].append(x)

def cyk(codeToken):
    regex_list = [r'[A-Za-z_][A-Za-z_0-9]*', r'[0-9]*', r'[A-z0-9]*']

    regex_map = {r'[A-Za-z_][A-Za-z_0-9]*' : ["variable"],
                r'[0-9]*' : ["number"],
                r'[A-z0-9]*' : ["string"],}

    cyk_table = [[[] for j in range(i)] for i in range(len(codeToken),0,-1)]
    for i in range(len(codeToken)):
        try:
            cyk_table[0][i].extend(grammar[codeToken[i]])
        except KeyError:
            for pattern in regex_list:
                if(re.match(pattern, codeToken[i])):
                    for regex_type in regex_map[pattern]:
                        try:
                            cyk_table[0][i].extend(grammar[regex_type])
                        except KeyError:
                            continue
                
    for i in range(1,len(codeToken)):
        for j in range(len(codeToken)-i):
            for k in range(i):
                for rule1 in cyk_table[i-k-1][j]:
                    for rule2 in cyk_table[k][j+i-k]:
                        try:
                            cyk_table[i][j]=grammar[rule1+rule2]
                        except KeyError:
                            continue
                    
    return cyk_table