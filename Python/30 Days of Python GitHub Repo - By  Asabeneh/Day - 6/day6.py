#Q1 - Q5
empty_tuple = ()
print(empty_tuple)

brothers = ("Abeanse", "Poarkt", "Oplayfa")
sister = ("Polit", "Woalf", "Olrad")
siblings = brothers + sister
print(siblings)

len_siblings = len(siblings)
print(len_siblings)

#Q5 
family_members = list(siblings)
print(family_members)
family_members.append("Shaui")
family_members.append("Lallu")
print(family_members)

#Excercise 2

fruits = ("mango", "apple", "litchi")
vegetables = ("soya Bean", "potato")
animal_products = ("milk", "eggs")
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

food_stuff_list = list(food_stuff_tp)
food_slice = food_stuff_list[0:3] + food_stuff_list[4:]
print(food_slice)

food_slice_first = food_stuff_list[3:]
food_slice_last = food_stuff_list[0:4]
print(food_slice_first)
print(food_slice_last)

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
check_1 = 'Estonia' in nordic_countries
check_2 = 'Iceland' in nordic_countries
print(check_1)
print(check_2)