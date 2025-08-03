# there are many types of the dictionary mthods 
# a.get()--------------> returns the value for the given key if it exists in the dictionary.
# a.key()--------------> returns the key for the given value if it exists in the dictionary.
# a.value()------------> returns the value for the given key if it exists in the dictionary.
# a.items()------------> returns a list of a tuple where the first element of the tuple is
# a.add(key, value)--> adds a new key-value pair to the dictionary.
# a.update(dict)----> updates the dictionary with the key-value pairs from another dictionary


# 
# lets do the methods examples

dict = {
    "name": "dhananjaya",
    "age": 5,
    "address": "ktm"
}

# here the key ="name " and the value = "dhananjaya"
print(dict.get("name"))  # Output: dhananjaya

print(dict.keys())  # Output: dict_keys(['name', 'age', 'address']

print(dict.values())  # Output: dict_values(['dhananjaya', 5, 'ktm'])

print(dict.items())  # Output: dict_items([('name', 'dhananjaya'), ('age', 5), ('address', 'ktm')])

print(dict.clear()) # Output: {}

print(dict.update({"name": "ram"}) )# Output: {'name': 'ram', 'age': 5, 'address': 'ktm'}


