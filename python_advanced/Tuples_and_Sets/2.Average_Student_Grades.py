# n = int(input())
#
# students_grades = {}
#
# for _ in range(n):
#     student, grade = input().split()
#     if student not in students_grades:
#         students_grades[student] = []
#     students_grades[student].append(float(grade))
#
# for student, grade in students_grades.items():
#     average = sum(grade) / len(grade)
#     print(f"{student} -> {' '.join(map(lambda x: f'{x:.2f}', grade))} (avg: {average:.2f})")


def average_score(value):
    return sum(value) / len(value)


n = int(input())

data = {}

for _ in range(n):
    name, score = input().split()
    score = float(score)
    if name not in data:
        data[name] = []
    data[name].append(score)

[print(f"{name} -> {' '.join(str(f'{x:.2f}') for x in data[name])} (avg: {average_score(value):.2f})") for name, value in data.items()]