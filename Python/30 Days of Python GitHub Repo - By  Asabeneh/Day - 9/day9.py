#Exercises: Level 1
#Q1

user_age = int(input("Enter your age: "))
if user_age > 18:
    print("You are old enough to learn to drive.")

else:
    b = "You need " + str(18 - user_age) + " more years to learn to drive."
    print(b)

#Q2
your_age = int(input("Enter your age: "))
my_age = 20

if your_age > my_age:
    if your_age - my_age == 1:
        print("You are 1 year older than me.")
    else:
        age_diff_old = "You are " + str(your_age - my_age) + " years older than me."
        print(age_diff_old)

elif your_age == my_age:
    print("We are both the same ages.")

else: 
    age_diff_young = "You are " + str(my_age - your_age) + " years younger than me."
    print(age_diff_young)

#Q3
num_one = int(input("Enter the first number: "))
num_two = int(input("Enter the second number: "))

if num_one > num_two:
    print(f"{num_one} is greater than {num_two}.")

elif num_one < num_two:
    print(f"{num_one} is less than {num_two}.")

else:
    print(f"{num_one} is equal to {num_two}.")

#Exercises: Level 2
Q1

ent_grade = int(input("Enter your score: "))
if ent_grade >= 80 and ent_grade <= 100:
    print("Your Grade is A")

elif ent_grade >= 70 and ent_grade <= 79:
    print("Your Grade is B")

elif ent_grade >= 60 and ent_grade <= 69:
    print("Your Grade is C")

elif ent_grade >= 50 and ent_grade <= 59:
    print("Your Grade is D")

elif ent_grade >= 0 and ent_grade <= 49:
    print("Your Grade is F")

else:
    print("Invalid Score")

#Q2
month_input = input("Enter the month: ").capitalize().isalpha()
if month_input == "September" or month_input == "October" or month_input == "November":
    print("The season is Autumn.")

elif month_input == "December" or month_input == "January" or month_input == "Febuary":
    print("The season is Winter.")

elif month_input == "March" or month_input == "April" or month_input == "May":
    print("The season is Spring.")

else: 
    print("The season is Summer")

#Q3
fruits = ["banana", "orange", "mango", "lemon"]
fruits_input = input("Enter a fruit name: ")

if fruits_input in fruits:
    print("That fruit already exist in the list.")

else:
    len_last = len(fruits) - 1
    fruits.insert(len_last, fruits_input)
    print(fruits)

#Exercises: Level 3
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
                }
        }

if "skills" in person:
    list_copy = person['skills'].copy()
    mid_term = list_copy[2]
    print(mid_term)

if "skills" in person:
    if 'Python' in person['skills']:
        print(True)
    else:
        print(False)

if person['is_marred'] == True and person['country'] == 'Finland':
    print('Asabeneh Yetayeh lives in Finland. He is married.')
