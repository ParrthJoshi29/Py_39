''' create a python program to accept user's age as input and calculate how many year he will leave assuming maximum age is 100 year. 
    example:-
    -----------------------------
    age : 25 
    remaining_age = 100 - 25'''

age = int(input("Enter your age : "))

remaining_age = 100 - age

print("Your age      :", age)
print("Remaining age :", remaining_age, "years")