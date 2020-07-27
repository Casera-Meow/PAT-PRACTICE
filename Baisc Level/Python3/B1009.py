strTemp = input().split()
strTemp.reverse()
for i in range(0, len(strTemp)):
    if i == len(strTemp) - 1:
        print(strTemp[i], end='')
    else:
        print(strTemp[i], end=' ')
