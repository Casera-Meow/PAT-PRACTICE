'''
Tips:
Without using additional array，there need to use tag to traverse
the movement of the tag(marker) is stimulation of the shift of the array
'''
n, m = map(int, input().split())
numberList = list()
inputNum = input().split()
for i in range(0, len(inputNum)):
    numberList.append(eval(inputNum[i]))
i = 0
while i < len(numberList):
    if i == len(numberList) - 1:
        print(numberList[(len(numberList) - m + i) % len(numberList)])
    else:
        print(numberList[(len(numberList) - m + i) % len(numberList)], end=' ')
    i += 1
