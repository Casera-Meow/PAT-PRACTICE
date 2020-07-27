import math

inputList = input().split()
n = int(inputList[0])
inputNum = inputList[1:]
inputNum = [int(x) for x in inputNum]
Atag = [0 for x in range(0, 5)]
Anum = [0 for x in range(0, 5)]
for x in range(0, len(inputNum)):
    if inputNum[x] % 5 == 0 and inputNum[x] % 2 == 0:
        Anum[0] += inputNum[x]
        Atag[0] += 1
        continue
    if inputNum[x] % 5 == 1:
        Anum[1] += int(math.pow(-1, Atag[1])) * inputNum[x]
        Atag[1] += 1
        continue
    if inputNum[x] % 5 == 2:
        Anum[2] += 1
        Atag[2] += 1
        continue
    if inputNum[x] % 5 == 3:
        Anum[3] += inputNum[x]
        Atag[3] += 1
        continue
    if inputNum[x] % 5 == 4:
        Anum[4] = max(Anum[4], inputNum[x])
        Atag[4] += 1
        continue
for i in range(0, len(Atag)):
    if Atag[i] == 0:
        Anum[i] = 'N'
if Anum[3] != 'N':
    Anum[3] /= Atag[3]
    Anum[3] = format(Anum[3], ".1f")
print(" ".join(str(i) for i in Anum))
