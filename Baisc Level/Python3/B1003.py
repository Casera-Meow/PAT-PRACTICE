'''
Tips:
    xPATx
    PT => PAT => PAAT
    APATA => APATA => APAATAA
The number of 'A' before 'P' multiple by the number of 'A' between 'P'&'T' is the number of 'A' after 'T'
'''
n = eval(input())  # the number of loops
listArr = list()
for i in range(0, n):
    listArr.append(tuple(input()))

for i in range(0, n):
    listTemp = listArr[i]
    length = len(listTemp)
    P_rec = A_rec = T_rec = otherAlpha_rec = -1
    for j in range(0, length):
        if listTemp[j] != 'P' and listTemp[j] != 'A' and listTemp[j] != 'T':
            otherAlpha_rec = 1
            break
        elif listTemp[j] == 'P' and P_rec == -1:
            P_rec = j
            continue
        elif listTemp[j] == 'T' and T_rec == -1:
            T_rec = j
            continue
        elif listTemp[j] == 'A':
            A_rec = j
            continue
    if otherAlpha_rec != -1:
        print("NO")
        continue
    if (P_rec * (T_rec - P_rec - 1) == length - T_rec - 1) and A_rec != -1:
        print("YES")
    else:
        print("NO")
