import math

def main():
    numInput = input().split()
    aNum, bNum = list(numInput[0]), eval(numInput[1])
    #除数为0的情况
    if bNum == 0:
        print('0',numInput[0],end = '')
        return 0
    #被除数不够除的情况
    if len(numInput[0]) == 1 and int(numInput[0])<bNum:
        print('0',numInput[0],end = '')
        return 0
    qNum = list()
    remainder = 0
    for i in range(len(aNum)):
        valueforaNum_i = eval(aNum[i])
        if i > 0:
            temp = remainder * 10 + valueforaNum_i
            if temp < bNum:
                qNum.append(str(0))
                remainder = temp
            else:
                quotient = math.floor(temp / bNum)
                qNum.append(str(quotient))
                remainder = temp - bNum * quotient
        else:
            if valueforaNum_i < bNum:
                remainder = valueforaNum_i
            else:
                quotient = math.floor(valueforaNum_i / bNum)
                qNum.append(str(quotient))
                remainder = valueforaNum_i - bNum * quotient
    print(''.join(qNum), str(remainder), end='')

main()