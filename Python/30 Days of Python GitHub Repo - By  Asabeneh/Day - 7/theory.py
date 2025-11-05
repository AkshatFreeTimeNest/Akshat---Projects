# #Day 7 - Sets

# #Making a Set
# st = {"item1", "item2", "item3", "item4"}
# print(st)

# st_length = len(st)
# print(st_length)

# st_check = "item1" and "item2" in st
# print(st_check)

# #Adding an Item in a set
# #1st method - add()

# st.add("item5")
# print(st)

# #Removing an item from a set
# st.remove('item2')
# print(st)

# item2 = st.pop()
# print(item2)


# #Clearing a set
# sett = {1, 2, 3}
# sett.clear()
# print(sett)

# set_list = list(sett)
# print(set_list)

## Joining List
# st_1 = {"item1", "item2", "item3"}
# st_2 = {"item4", "item5"}
# st_1.update(st_2)
# # print(st_1)

# #Intersection of two sets
# st1 = {"item1", "item2", "item3", "item4"}
# st2 = {"item3", "item4"}
# st_int = st1.intersection(st2)
# print(st_int)   

# #Subset and SuperSet
# # syntax
# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item2', 'item3'}
# subset = st2.issubset(st1) # True
# superset = st1.issuperset(st2) # True

# print(subset)
# print(superset)

# #Symmetric Difference
# # syntax
# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item2', 'item3', 'item5'}
# # it means (A\B)∪(B\A)
# symm = st2.symmetric_difference(st1) # {'item1', 'item4'}
# print(symm)

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
dis = st2.isdisjoint(st1) # False
print(dis)