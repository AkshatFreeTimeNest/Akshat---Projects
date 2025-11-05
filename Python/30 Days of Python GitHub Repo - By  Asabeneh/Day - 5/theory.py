#Unpacking List Items
lst = ["item1", "item2", "item3", "item4", "item5"]
first_item, second_item, third_item, *last2= lst
print(first_item)
print(last2)

#Accessing List Items
fruits = ["mango", "orange", "apple"]
first_item = fruits[0]
print(first_item)

range_items = fruits[1: 3]
print(range_items)

last_index = len(fruits) - 1
last_item = fruits[last_index]
print(last_item)

# Slicing Items in a list
fruits = ["mango", "orange", "apple", "guava", "kiwi"]
reverse_order = fruits[::-1]
print(reverse_order)

first_three = fruits[0:3]
print(first_three)

step_2 = fruits[::2]
print(step_2)

#Modifying Lists
fruits = ["mango", "orange", "apple", "guava", "kiwi"]
fruits[1] = "not orange"
print(fruits)

#Checking Items in a list
fruits = ["mango", "orange", "apple", "guava", "kiwi"]
does_have = "mango" in fruits
print(does_have)

#Adding items in a list
fruits = ["mango", "orange", "apple", "guava", "kiwi"]
fruits.append("strawberry")
print(fruits)

fruits.insert(3, "papaya")
print(fruits)

# Removing Items in list
fruits = ["mango", "orange", "apple", "guava", "kiwi"]
fruits.pop(3)
print(fruits)

fruits.remove("mango")
print(fruits)

del fruits[1:3]
print(fruits)

fruits = ["mango", "orange", "apple", "guava", "kiwi"]
fruits.clear()
print(fruits)

#Copyting a list
fruits = ["mango", "guava", "apple"]
fruits_copy = fruits.copy()
print(fruits_copy)

#Joining a list
pos_num = [1, 2, 3, 4]
zero = [0]
neg_num = [-3, -2, -1]
integers = neg_num + zero + pos_num
print(integers)


