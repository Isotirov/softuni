n = int(input())

students = {}
remaining_students = {}

for _ in range(n):
    student_name = input()
    grade = float(input())
    if student_name not in students:
        students[student_name] = []
    students[student_name].append(grade)

for key, value in students.items():
    average = sum(value) / len(value)
    if average >= 4.50:
        remaining_students[key] = average

remaining_students = sorted(remaining_students.items(), key=lambda x: -x[1])

for name, grade in remaining_students:
    print(f"{name} -> {grade:.2f}")