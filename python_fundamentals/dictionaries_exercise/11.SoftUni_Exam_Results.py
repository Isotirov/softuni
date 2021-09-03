data = input()

lang_submission = {}
user_data = {}

while not data == "exam finished":
    current_data = data.split("-")
    username = current_data[0]
    if current_data[1] == "banned":
        if username in user_data:
            del user_data[username]
    else:
        lang = current_data[1]
        points = int(current_data[2])
        if lang not in lang_submission:
            lang_submission[lang] = [username]
        else:
            lang_submission[lang].append(username)
        if username not in user_data:
            user_data[username] = points
        elif user_data[username] < points:
            user_data[username] = points
    data = input()

print("Results:")
max_score = sorted(user_data.items(), key=lambda x: (-x[1], x[0]))
for user, point in max_score:
    print(f"{user} | {point}")
print("Submissions:")
lang_count = sorted(lang_submission.items(), key=lambda x: (-len(x[1]), x[0]))
for language, count in lang_count:
    print(f"{language} - {len(count)}")