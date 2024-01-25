n = int(input("Введите кол-во школьников: "))
list = []
for i in range(n):
    word = input("Введите фамилии школьников с их оценками: ")
    list.append(word)
for students in list:
    print(students)
print()
for student in list:
    if student[0] in ['4', '5']:
        print(student)