# import sys

# Meminta nama input file dan dijadikan sebagai suatu array
# Return Array of Arrays
def FileToArray():
    fileInput = open(str(input()), "r")
    fileInput = fileInput.readlines()

    prev = ''
    codeArray = []
    for i in fileInput:
        length = len(i)

        # Kalau line hanya berisi \n, akan di skip
        if (length == 1) & (i[0] == '\n'):
            continue

        if i[0] == ' ':
            startIndent = True
        else:
            startIndent = False

        # Menghapus indentasi
        ctr = 0
        while (startIndent & (ctr < length)):
            if i[ctr] != ' ':
                startIndent = False
                ctr -= 1
            ctr += 1

        # Menulis ulang isi dari file serta menghapus spasi yang berlebihan
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

