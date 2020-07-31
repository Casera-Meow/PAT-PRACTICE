import sys

frequency = eval(input())
mora = {'C': 1, 'J': 0, 'B': -1}


def setmora(b, c, j, string):
    if string == 'C':
        c += 1
    elif string == 'J':
        j += 1
    elif string == 'B':
        b += 1
    return b,c,j


def findMaxofFrequency(b, c, j):
    if b >= c:
        if b >= j:
            return 'B'
        else:
            return 'J'
    else:
        if c >= j:
            return 'C'
        else:
            return 'J'


def main():
    winA, loseA, drawA = 0, 0, 0
    winB, loseB, drawB = 0, 0, 0
    aforB, aforC, aforJ = 0, 0, 0
    bforB, bforC, bforJ = 0, 0, 0
    # This op is to reduce the access to the list
    for i in range(frequency):
        moraInput = sys.stdin.readline().split()
        stra, strb = moraInput[0], moraInput[1]
        a, b = mora[stra], mora[strb]
        if stra == strb:
            drawA += 1
            drawB += 1
        elif a - b == 1 or a - b == -2:  # Indicates a win
            winA += 1
            loseB += 1
            aforB, aforC, aforJ = setmora(aforB, aforC, aforJ, stra)
        elif a - b == -1 or a - b == 2:  # Indicates b win
            winB += 1
            loseA += 1
            bforB, bforC, bforJ = setmora(bforB, bforC, bforJ, strb)
    print(winA, drawA, loseA)
    print(winB, drawB, loseB)
    print(findMaxofFrequency(aforB, aforC, aforJ), end=' ')
    print(findMaxofFrequency(bforB, bforC, bforJ), end='')


main()
#Tips:避免使用列表进行多次访问，时间开销大
