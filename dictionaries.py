# a dictionaries is a collection of key and values
# always have a key and a value

# dictionary = {
#     key: value
# }

# peoples = {
#     "John": 23,
#     'Rob': 40,
#     "Tim": 20
# }

# peoples_id = {
#     1: "Ford",
#     2: "Walton",
#     3: "Parker"
# }

# print(peoples_id[2])
# print(peoples)
# print(peoples['Rob'])
# print(peoples['Tim'])


# mutability of dictionary
# peoples["Rob"] = 100
# print(peoples["Rob"])



# create a dictionary
city1 = dict(
    BD = 'Dhaka',
    USA = 'NY',
    UK = 'London'
)

city2 = {
    'BD': 'Dhaka',
    'USA': 'NY',
    'UK': "London"
}

# print(city1)
# print(city2)

people = dict(
    john = 32,
    rob = 45,
    tim = 20
)

people['mike'] = 90
del people['tim'] # delete an item

# print(people['tim'])
print(people)