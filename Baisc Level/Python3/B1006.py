n = eval(input())
outputlist = list()
while n >= 1:
    outputlist.append(n % 10)
    n = int(n / 10)
outputlist.reverse()
if len(outputlist) == 3:
    print('B' * outputlist[0], 'S' * outputlist[1], sep='', end='')
    for i in range(0, outputlist[2]):
        print(i + 1, end='')
elif len(outputlist) == 2:
    print('S' * outputlist[0], sep='', end='')
    for i in range(0, outputlist[1]):
        print(i + 1, end='')
elif len(outputlist) == 1:
    for i in range(0, outputlist[0]):
        print(i + 1, end='')
