import os

found_files = {}

for y in os.listdir():
    if os.path.isdir(os.path.join(os.getcwd(), y)):
        for x in os.listdir(os.path.join(os.getcwd(), y)):
            if os.path.isfile(os.path.join(y, x)):
                ext = x.split(".")[1]
                name = x.split(".")[0]
                if ext not in found_files:
                    found_files[ext] = []
                found_files[ext].append(x)

found_files = sorted(found_files.items(), key=lambda kvp: (kvp[0], kvp[1].sort()))

desktop = os.path.join(os.environ.get("USERPROFILE"), "Desktop")
open(os.path.join(desktop, "report.txt"), "w").close()
file = os.path.join(desktop, "report.txt")

with open(file, "r+") as current_file:
    for key, value in found_files:
        current_file.write(key)
        current_file.write('\n')
        for v in value:
            current_file.write(f"- - - {v}")
            current_file.write('\n')