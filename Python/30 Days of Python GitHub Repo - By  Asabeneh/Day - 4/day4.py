# #Q1 
# str1 = "Thirty"
# str2 = "Days"
# str3 = "Of"
# str4 = "Python"

# str_con = f"{str1} {str2} {str3} {str4}."
# print(str_con)

# #Q2
# s1 = "Coding"
# s2 = "For"
# s3 = "All"
# s = "{} {} {}." .format(s1, s2, s3)
# print(s)

# #Q3 - Q9
# company = "Coding For All"
# print(company)

# company_length = len(company)
# print(company_length)

# company_uppercase = company.islower()
# company_lowercase = company.isupper()
# company_capitalize = company.capitalize()
# company_title = company.title()
# company_swapcase = company.swapcase()
# company_strip = company.strip("Coding")

# company_index = company.index("Coding")
# company_find = company.find("Coding")
# company_replace = company.replace("Coding", "Python")
# comapny_replace_2 = company.replace("Coding For All", "Python for Everyone")
# company_split = company.split()

# comp = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
# comp_split = comp.split(", ")
# print(comp_split)

# company_index_0 = company[0]
# company_index_2 = company[-1]
# company_index_10 = company[10]

# #Q18 and Q19
# acro1 = "PFE"
# print(acro1)

# acro2 = "CFA"
# print(acro2)

# #Q20 - Q22
# name_index = "Coding For All"
# index1 = name_index.index("C")
# index2 = name_index.index("F")
# rfind = name_index.rfind("L")

# #Q23 - Q27
# sent = "You cannot end a sentence with because because because is a conjunction"
# find_because = sent.find("because")
# rindex_because = sent.rindex("because")
# slice_because = sent.replace("because because because","")

# first_occ = find_because
# slice_because2 = slice_because

# #Q28 - Q30
# substring = "Coding For All"
# check_sub = substring.startswith("Coding")
# check_end = substring.endswith("coding")

# strip_space = '   Coding For All      '
# strip = strip_space.strip(" ")
# print(strip)

# #Q31 - Q32
# sen1 = "30DaysOfPython"
# sen2 = "thirty_days_of_python"
# check1 = sen1.isidentifier()
# check2 = sen2.isidentifier()
# print(check1)
# print(check2)

# #Q33
# print("I am enjoying this challenge.\nI just wonder what is next.")

# #Q34
# print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

# #Q35
# radius = 10
# area = 3.14 * radius ** 2
# ans = "The area of a circle with radius %.2f is %.2f meters square" %(radius, area)
# print(ans)

# ans2 = f"The area of a circle with radius {radius} is {area} meters square"
# print(ans2)

# ans3 = "The area of the circle with radius {:.2f} is {:.4f} meters square" .format(radius, area)
# print(ans3)

# #Q36
# a = 8
# b = 6

# sum = f"{a} + {b} = {a + b}"
# diff = "{} - {} = {}" .format(a, b, a - b)
# mult = "%.2f * %.2f = %.2f" %(a, b, a * b)
# div = f"{a} / {b} = {a / b}"
# rem = f"{a} % {b} = {a % b}"
# floor = f"{a} // {b} = {a // b}"
# exp = "{:.4f} ** {:.4f} = {:.4f}" .format(a, b, a ** b)

company = "Coding For All"
last_char = company[-1] # Gets the character 'l'
last_index_num = len(company) - 5 # Gets the index number 13
print(last_index_num)