command = input()

course_dict = {}

while not command == "end":
    course, student = command.split(" : ")
    if course not in course_dict:
        course_dict[course] = []
    course_dict[course].append(student)
    command = input()

sorted_count = dict(sorted(course_dict.items(), key=lambda kvp: -len(kvp[1])))

for key, value in sorted_count.items():
    print(f"{key}: {len(value)}")
    for x in sorted(sorted_count[key]):
        print(f"-- {x}")