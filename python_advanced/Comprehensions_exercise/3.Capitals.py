# country_names = [x for x in input().split(", ")]
# capitals = [x for x in input().split(", ")]
#
# dictionary = {country: name for country, name in zip(country_names, capitals)}

# dictionary_1 = dict(zip([x for x in input().split(", ")], [x for x in input().split(", ")]))

print('\n'.join(f"{country} -> {capital}" for country, capital in dict(zip([x for x in input().split(", ")],
                                                                           [x for x in input().split(", ")])).items()))