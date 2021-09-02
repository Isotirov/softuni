data = input()

id_name = {}
id_course = {}

while ":" in data:
    name, identification, course = data.split(":")
    course = course.split()
    course = '_'.join(course)
    id_name[identification] = name
    id_course[identification] = course
    data = input()

for x, y in id_course.items():
    if data in y:
        print(f"{id_name[x]} - {x}")