grade_book = {"vivaan": 99, "arjun": 92, "ishita": 78, "viansh": 65, "ronav": 90}

total = 0
for score in grade_book.values():
    total += score
average = total / len(grade_book)
print("Average Grade:", average)

max_grade = max(grade_book.values())
min_grade = min(grade_book.values())
print("Maximum Grade:", max_grade)
print("Minimum Grade:", min_grade)

name = input("Enter the student's name to check their grade: ")

if name in grade_book:

    print(grade_book[name])
else:
    print("Student not found.")
