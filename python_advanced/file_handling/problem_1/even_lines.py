symbols = {"-", ",", ".", "!", "?"}

i = 0

with open("text.txt", "r") as file:
    while True:
        line = file.readline().strip()
        if not line:
            break
        if i % 2 == 0:
            for char in line:
                if char in symbols:
                    line = line.replace(char, "@")
            print(' '.join(line.split()[::-1]))
        i += 1