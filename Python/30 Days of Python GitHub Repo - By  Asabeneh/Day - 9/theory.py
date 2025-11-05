#Day 9 Theory
#If Statements

a = 10
if a > 0:
    print("A is positive")

#If Else Statements

b = 0
if b > 0:
    print("B is positive.")
else:
    print("B is either negative or zero")

#If Elif Else Statements
c = 0 
if c > 0:
    print('C is positive')
elif c < 0:
    print("C is negative")
else:
    print("C is zero.")

#Short Hand
d = 7
print("D is greater than equal to 10.") if d >= 10 else print("D is less than 10")

#Nested Condition
enter_number = int(input("Enter a number: "))
if enter_number > 0:
    if enter_number % 2 == 0:
        print(f"{enter_number} is positive and even integer.")

    else:
        print(f"{enter_number} is positive.")

elif enter_number == 0:
    print(f"{enter_number} is zero")

else:
    print(f"{enter_number} is a negative number.")

#