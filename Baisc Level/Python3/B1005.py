# Cullatz Guests using list tag
n = eval(input())
inputlist = input().split()
inputlist = [int(x) for x in inputlist]  # translate the type from str to int
checklist = [x for x in inputlist]  # record output
for i in range(0, n):
    a = inputlist[i]
    while a > 1:
        if a % 2 == 0:
            a = int(a / 2)
        else:
            a = int((3 * a + 1) / 2)
        if a in inputlist and a in checklist:  # find the key num
            checklist.remove(a)
checklist.sort(reverse=True)
for i in range(0, len(checklist) - 1):
    print(checklist[i], end=' ')
print(checklist[len(checklist) - 1], end='')
