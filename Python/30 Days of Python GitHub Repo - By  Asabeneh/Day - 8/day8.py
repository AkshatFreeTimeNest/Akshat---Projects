#Q1 - Q2 Empty Dictionary 
dog = dict()
print(dog)

dog["name"] = "Abanease"
dog["color"] = "green"
dog["breed"] = "Lab"
dog["age"] = 22
print(dog)

#Q3 - Q5
student = {
    "first_name" : "Abanase",
    "last_name" : "Bobby",
    "gender" : "Male",
    "age" : 22,
    "is_married" : True,
    "skills" : ["HTML", "CSS", "Python"],
    "country" : "India",
    "city" : "Euurpo",
    "address" : "98, House no 12, Euposria."
}

student_length = len(student)
print(student_length)

skills_value = student["skills"]
skills_type = type(skills_value)
print(skills_type)

#Q6 
student["skills"].append("JS")
student["skills"].append("Bootstrap")
print(student)

#Q7 - Q8
dct_list_keys = student.keys()
print(dct_list_keys)

dct_list_values = student.values()
print(dct_list_values)

#Q9 - #Q10
dct_tuple = student.items()
print(dct_tuple)

del student["age"]

del student