marks = {"-", ",", ".", "!", "?", "'"}

with open("text.txt") as file, open("new_text.txt", "w") as result:
    i = 1
    for line in file:
        current_mark_count = 0
        current_letter_count = 0
        for char in line:
            if char in marks:
                current_mark_count += 1
            elif char.isalpha():
                current_letter_count += 1
        result.write(f"Line {i}: {line.strip()} ({current_letter_count})({current_mark_count})")
        result.write("\n")
        i += 1