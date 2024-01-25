M = int(input())
N = int(input())
K = int(input())
first = set()
second = set()
for i in range(M + N + K):
    student = input()
    if student not in first:
        first.add(student)
    elif student not in second:
        second.add(student)
    else:
        second.remove(student)
if len(second):
    print(len(second))
else:
    print('NO')