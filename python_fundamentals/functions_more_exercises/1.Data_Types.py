def data_types(data):
    if data == "int":
        return int(input()) * 2
    elif data == "real":
        return f"{float(input()) * 1.5:.2f}"
    elif data == "string":
        return f"${input()}$"


data_type = input()
print(data_types(data_type))