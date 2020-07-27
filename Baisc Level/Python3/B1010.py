'''
Tips:
For the polynomial with only two bits and exponent term of 0
there needs to print 0,0
'''
numStore = input().split()
numStore = [eval(x) for x in numStore]
i = 0
j = 1
while j < len(numStore):
    numStore[i] *= numStore[j]
    numStore[j] -= 1
    if len(numStore) == 2 and numStore[j] < 0:
        numStore[i] = numStore[j] = 0
    if numStore[j] < 0:
        numStore.pop(i)
        numStore.pop(i)
        break
    i += 2
    j += 2
for i in range(0, len(numStore)):
    if i == len(numStore) - 1:
        print(numStore[i], end='')
    else:
        print(numStore[i], end=' ')
