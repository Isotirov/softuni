data = input()

link = data.split("\\")

name = link[-1].split(".")[0]
extension = link[-1].split(".")[1]

print(f"File name: {name}")
print(f"File extension: {extension}")