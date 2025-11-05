# #Day 8 - Dictionary

# #Creating a Dictionary
# dct_create = {
#     "first_name" : "Abanease",
#     "last_name" : "Bobby",
#     "age" : 25,
#     "is_married" : True,
#     "country" : "London"
# }
# print(dct_create)

# len_dic = len(dct_create)
# print(len_dic)

# dct_create["key_item"] = "Okayy"
# print(dct_create)

# #Accessing Items
# sec_item = dct_create.get("age")
# print(sec_item)

# thr_item = dct_create["is_married"]
# print(thr_item)

# #Modifying Items in a dictionary
# dct_create = {
#     "first_name" : "Abanease",
#     "last_name" : "Bobby",
#     "age" : 25,
#     "is_married" : True,
#     "country" : "London"
# }

# dct_create["is_married"] = False
# print(dct_create)

# #Checking Keys in a Dict
# dct_create = {
#     "first_name" : "Abanease",
#     "last_name" : "Bobby",
#     "age" : 25,
#     "is_married" : True,
#     "country" : "London"
# }

# check_item = "first_name" in dct_create
# print(check_item)

# check_item_2 = "city" in dct_create
# print(check_item_2)

#Removing key and value pairs
dct_create = {
    "first_name" : "Abanease",
    "last_name" : "Bobby",
    "age" : 25,
    "is_married" : True,
    "country" : "London"
}

dct_create.pop("age")
print(dct_create)

dct_create.popitem()
print(dct_create)

del dct_create["is_married"]
print(dct_create)