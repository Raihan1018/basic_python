# a dictionaries is a collection of key and values
# always have a key and a value

# dictionary = {
#     key: value
# }

peoples = {
    "John": 23,
    'Rob': 40,
    "Tim": 20
}

peoples_id = {
    1: "Ford",
    2: "Walton",
    3: "Parker"
}

# print(peoples_id[2])
# print(peoples)
# print(peoples['Rob'])
# print(peoples['Tim'])


# mutability of dictionary
peoples["Rob"] = 100
print(peoples["Rob"])