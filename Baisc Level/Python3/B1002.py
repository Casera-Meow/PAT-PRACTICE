n = input()  # n is the input number
length = len(n)
sum = 0  # sum is the sum of each digit
for i in range(0, length):
    sum += (ord(n[i]) - ord('0'))
pingYin = ['ling', 'yi', 'er', 'san', 'si', 'wu', 'liu', 'qi', 'ba', 'jiu']
list1 = list(str(sum))
for i in range(0, len(list1)):
    if i == len(list1) - 1:
        print(pingYin[eval(list1[i])], end='')
    else:
        print(pingYin[eval(list1[i])] + ' ', end='')
