books_in_library = set()

library_c = int(input())
list_c = int(input())

for i in range(library_c):
    books_in_library.add(input())
for i in range(list_c):
    if input() in books_in_library:
        print("YES")
    else:
        print("NO")