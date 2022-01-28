# def age_assignment(*args, **kwargs):
#     ages = {name: 0 for name in args}
#
#     for key, value in kwargs.items():
#         for name in ages:
#             if name.startswith(key):
#                 ages[name] = value
#
#     return ages
#
#
# print(age_assignment("Peter", "George", G=26, P=19))


def age_assignment(*args, **kwargs):
    new_age = {}

    for letter, age in kwargs.items():
        for name in args:
            if name.startswith(letter):
                new_age[name] = age
    return new_age