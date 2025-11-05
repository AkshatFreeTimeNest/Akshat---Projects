# #escape characters in strings
# print("I hope you are doing great.\nAre you?")
# print("Day\tTime\tYear")
# print("21\t5pm\t2007")
# print("1\t3am\t2090")
# print("12\t6am\t2050")
# print("14\t9pm\t2000")

# # String Formatting -Old style
# f_name = "Abemese"
# l_name = "Bobb"
# job = "Puu"
# full_name = "I am %s %s, and my job is %s." %(f_name, l_name, job)
# print(full_name)

# radius = 10
# pi = 3.141
# area = pi * radius ** 2
# formatted_string = "The radius of the circle is %d and its area is %.4f." %(radius, area)
# print(formatted_string)

# # String Formatting -New Style
# f_name = "Abeeenssse"
# l_name = "bobby"
# skill = "Python"
# full_name = "Hi, My name is {} {}, i know {}." .format(f_name, l_name, skill)
# print(full_name)

# radius = 10
# pi = 3.14
# area = pi * radius ** 2
# formm = "The area of the circle of radius {} is {:.4f}." .format(radius, area)
# print(formm)

# a = 4
# b = 3
# print("{} + {} = {}" .format(a, b, a + b))

# # f-string formatting
# a = 4
# b = 3
# print(f"{a} + {b} = {a + b}")
# print(f"{a} ** {b} = {a ** b}")

#Unpacking Characters
language = "Python"
# a,b,c,d,e,f = language
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)

# last_letter = language[-1]
# print(last_letter)

# last_three = language[0:3]
# print(last_three)

# #reversing
# greeting = "Hello World!"
# reverse = greeting[::-1]
# print(reverse)


# skip = language[0 : 6 : 2]
# print(skip)

#String Methods
challenge = "thirty\tdays\tof\tpython"
print(challenge.expandtabs(10))