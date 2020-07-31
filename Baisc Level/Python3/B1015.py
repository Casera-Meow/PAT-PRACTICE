import sys

# 建立列表的列表对信息进行存储，最外层索引为总成绩(201)，次一层索引为德分(101)，内层存储学生学号信息
def stuAppend(list, sumScore, dScore, stuNumber):
    # Store student number to list
    # list structure: sumScore[dScore[stuNumber]]
    if list[sumScore] == 0:
        list[sumScore] = [0] * 101
        list[sumScore][dScore] = [stuNumber]
    elif list[sumScore][dScore] == 0:
        list[sumScore][dScore] = [stuNumber]
    else:
        list[sumScore][dScore].append(stuNumber)


def printResult(l):
    for sumScore in l[::-1]:
        if sumScore:
            for dScore in sumScore[::-1]:
                if dScore:
                    for k in sorted(dScore):
                        sys.stdout.write(student.get(k))

# dictionary used to convert string to int
score_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
              '10': 10, '11': 11, '12': 12, '13': 13, '14': 14, '15': 15, '16': 16, '17': 17,
              '18': 18, '19': 19, '20': 20, '21': 21, '22': 22, '23': 23, '24': 24, '25': 25,
              '26': 26, '27': 27, '28': 28, '29': 29, '30': 30, '31': 31, '32': 32, '33': 33,
              '34': 34, '35': 35, '36': 36, '37': 37, '38': 38, '39': 39, '40': 40, '41': 41,
              '42': 42, '43': 43, '44': 44, '45': 45, '46': 46, '47': 47, '48': 48, '49': 49,
              '50': 50, '51': 51, '52': 52, '53': 53, '54': 54, '55': 55, '56': 56, '57': 57,
              '58': 58, '59': 59, '60': 60, '61': 61, '62': 62, '63': 63, '64': 64, '65': 65,
              '66': 66, '67': 67, '68': 68, '69': 69, '70': 70, '71': 71, '72': 72, '73': 73,
              '74': 74, '75': 75, '76': 76, '77': 77, '78': 78, '79': 79, '80': 80, '81': 81,
              '82': 82, '83': 83, '84': 84, '85': 85, '86': 86, '87': 87, '88': 88, '89': 89,
              '90': 90, '91': 91, '92': 92, '93': 93, '94': 94, '95': 95, '96': 96, '97': 97,
              '98': 98, '99': 99, '100': 100}
inputList = [int(x) for x in sys.stdin.readline().split()]  # list store num,l,h
stuNum,low,high= inputList[0],inputList[1],inputList[2] #此处赋值减少访问开销
student = {}  # dictionary for dictionary:studentInfo ,used to print the result




def main():
    stu1,stu2,stu3,stu4 = [0] * 201,[0] * 201,[0] * 201,[0] * 201
    for i in range(0, stuNum):
        stuInformPrint = sys.stdin.readline()
        stuInform = stuInformPrint.split()  # store student information
        # 此处通过提取列表元素，减少对列表元素的访问，节省时间开销，否则超时
        a = score_dict[stuInform[1]]
        b = score_dict[stuInform[2]]
        sumScore = a + b
        if a >= high and b >= high:
            stuAppend(stu1, sumScore, a, stuInform[0])
            student[stuInform[0]] = stuInformPrint
            continue
        elif a >= high and b >= low:
            stuAppend(stu2, sumScore, a, stuInform[0])
            student[stuInform[0]] = stuInformPrint
            continue
        elif a >= b and b >= low:
            stuAppend(stu3, sumScore, a, stuInform[0])
            student[stuInform[0]] = stuInformPrint
            continue
        elif a >= low and b >= low:
            stuAppend(stu4, sumScore, a, stuInform[0])
            student[stuInform[0]] = stuInformPrint
            continue
    print(len(student))
    printResult(stu1)
    printResult(stu2)
    printResult(stu3)
    printResult(stu4)

main()
'''
Tips: 
Note1:
    sys.stdin.readline 比 input 快 10倍（100w测试）
    input 会默认将每行最后的换行符删除掉，有一定的开销。等同于 sys.stdin.readline.strip(),而sys.stdin.readline 
        比 sys.stdin.readline.strip() 快20%（100w测试）
Note2:
    for 循环中的大量int类型的转换，造成了大量的开销，使用字典可以解决该问题
Note3:
    使用列表对成绩进行索引，减少append操作的开销
Note4：
    对于列表的存取会有时间开销，在条件判断之前将它们取出到变量中可以减少时间开销
'''
