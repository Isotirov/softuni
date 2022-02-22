import os

command = input()

while not command == "End":
    current_command = command.split("-")
    action = current_command[0]
    file_name = current_command[1]
    if action == "Create":
        open(file_name, "w").close()
    elif action == "Add":
        content = current_command[2]
        with open(file_name, "a") as file:
            file.write(content)
            file.write("\n")
    elif action == "Replace":
        old_string = current_command[2]
        new_string = current_command[3]
        if os.path.exists(file_name):
            with open(file_name, "r+") as file:
                current_content = file.read().replace(old_string, new_string)
                file.seek(0)
                file.truncate()
                file.write(current_content)
        else:
            print("An error occurred")
    elif action == "Delete":
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")

    command = input()