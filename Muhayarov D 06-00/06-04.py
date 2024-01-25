stud = set()
stud_c = int(input()) + int(input())

for _ in range(stud_c):
    new_stud = {input()}
    if new_stud <= stud:
        stud = stud - new_stud
        new_stud.pop()
    else:
        students = stud | new_stud

if stud:
    print(len(stud))
else:
    print("No")