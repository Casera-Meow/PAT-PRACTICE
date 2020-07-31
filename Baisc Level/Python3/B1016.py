numInput = input().split()
aNum, dA = numInput[0], numInput[1]
bNum, dB = numInput[2], numInput[3]
aNum, bNum = list(aNum), list(bNum)
a = aNum.count(dA)
b = bNum.count(dB)
if a == 0 and b == 0:
    output = 0
elif a == 0:
    output = int(dB * b)
elif b == 0:
    output = int(dA * a)
else:
    output = int(dA * a) + int(dB * b)
print(output)
#Tips:Pay attention to the condition that .count() is zeros