data = input()

company = {}

while not data == "End":
    company_name, employee_id = data.split(" -> ")
    if company_name not in company:
        company[company_name] = []
        company[company_name].append(employee_id)
    else:
        if employee_id not in company[company_name]:
            company[company_name].append(employee_id)
    data = input()

for key, value in sorted(company.items()):
    print(key)
    for ids in value:
        print(f"-- {ids}")
