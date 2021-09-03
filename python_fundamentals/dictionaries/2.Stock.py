data = input().split()
searched_list = input().split()

data_list = {}

for ind in range(0, len(data), 2):
    product = data[ind]
    qt = int(data[ind + 1])
    data_list[product] = qt

for prod in searched_list:
    if prod in data_list:
        print(f"We have {data_list[prod]} of {prod} left")
    else:
        print(f"Sorry, we don't have {prod}")