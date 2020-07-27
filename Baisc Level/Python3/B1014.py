Week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
hour = {"0": "00", "1": "01", "2": "02", "3": "03", "4": "04", "5": "05", "6": "06", "7": "07", "8": "08", "9": "09", \
        "A": "10", "B": "11", "C": "12", "D": "13", "E": "14", "F": "15", "G": "16", "H": "17", "I": "18", "J": "19", \
        "K": "20", "L": "21", "M": "22", "N": "23"}
string1 = input()
string2 = input()
string3 = input()
string4 = input()
flag = 0
for i in range(0, min(len(string1), len(string2))):
    if string1[i] == string2[i]:
        if flag == 0 and string1[i].isupper() and ord(string1[i]) - ord('A') < 7:
            print(Week[ord(string1[i]) - ord('A')], end=' ')
            flag = 1
            continue
        elif flag == 1 and hour.get(string1[i]):
            print(hour.get(string1[i]), end=':')
            break
for j in range(0, min(len(string3), len(string4))):
    if (string3[j] == string4[j] and string3[j].isalpha()):
        if j < 10:
            print(hour.get(str(j)), end='')
            break
        else:
            print(str(j), end='')
            break
# the judgement of alphabet can also use .isupper() .islower() .isalpha() function
# 坑：12行处一定要限制ord(string1[i]) - ord('A') < 7， 否则结果出错，异常值返回