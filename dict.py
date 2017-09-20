my_dictionary = {}



my_dictionary={"name":"brian", "address": "9 Harlow", "city": "Fair Lawn"}

print(my_dictionary)

del my_dictionary["city"]

print(my_dictionary)

my_dictionary["city"] = "paramus"

print(my_dictionary)

for key, value in my_dictionary.items():
    print(key)
    print(value)
