# import sys

def FileToArray():
    fileInput = open(str(input()), "r")
    fileInput = fileInput.readlines()
    prev = ''
    
    codeArray = []
    for i in fileInput:
        length = len(i)
        if i[0] == ' ':
            startIndent = True
        else:
            startIndent = False
        ctr = 0
        while (startIndent & (ctr < length)):
            if i[ctr] != ' ':
                startIndent = False
                ctr -= 1
            ctr += 1

        codeLine = []
        for j in range(ctr, length):
            if (prev == ' ') & (i[j] != ' '):
                codeLine.append(' ')
                codeLine.append(i[j])
            elif i[j] != ' ':
                codeLine.append(i[j])
            prev = i[j]
        codeArray.append(codeLine)

    return codeArray

A = FileToArray()
print(A)
for i in A:
    print(i)

print('\n========== Border 1 ==========\n')
for i in A:
    for j in i:
        print (j, end='')
    print()

print("\nDone.")