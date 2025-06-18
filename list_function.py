fruits = ['Apple', 'Mango', 'peach' 'Orange', 'Watermelon', 'Grape']

# print(len(fruits)) 

# fruits.insert(1, 'Pineapple') # add some element in specific index & we must mention the index number.
# print(fruits)

# fruits.append(['Guava', 'Apricot']) # add item in the last index as a nested list
# print(fruits)

# fruits.extend(['Guava', 'Apricot']) ## add item in the last index not in a nested list.
# print(fruits)

# append -> add element in the last index as a nested list
# extend -> add element in the last index not in a nested list

# fruits.remove('Apple') # remove an element from the list

# fruits.pop() # remove an element from the last index

# remove -> remove an element & need to mention the element name not index number
# pop -> remove and element from the last index, don't need to mention the index number or element name

# print(fruits.index('Mango')) # find specific element index number

scores = [1,2,3,4,5,6,7,8,9,65,34,23,23]

print(max(scores))
print(min(scores))