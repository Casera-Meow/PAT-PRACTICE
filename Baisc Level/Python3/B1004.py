'''
Tips:for variable grade,the input is string type and must convert to int type.
The function max()，min() require the variable type int
'''
n = eval(input())
name = list()
course = list()
grade = list()
for i in range(0, n):
    InputArr = input()
    name.append(InputArr.split()[0])
    course.append(InputArr.split()[1])
    grade.append(int(InputArr.split()[2]))
maxT = grade.index(max(grade))
minT = grade.index(min(grade))
print(name[maxT], course[maxT])
print(name[minT], course[minT], end='')

