n = eval(input())
i = j = k = result = 0
numList = numGroup = resultList = list()
for m in range(0, n):
    result = "false"
    numGroup = input().split()
    numGroup = [int(x) for x in numGroup]
    i = numGroup[0]
    j = numGroup[1]
    k = numGroup[2]
    if i + j > k:
        result = "true"
    resultList.append(result)
for m in range(0,n):
    print("Case #", m + 1, ": ", resultList[m], sep='',end = '\n')
