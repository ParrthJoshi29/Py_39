'''
 write a program to accept 2 number from user. and accept choice for operations.
operations will be addition, subtraction, multiplication, division
do operation and display result as per user choice using switch statements.
'''

num1 = float(input("Enter first number  : "))
num2 = float(input("Enter second number : "))

print()
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Enter your choice (1 to 4) : "))

if choice == 1:
    result = num1 + num2
    print("Result :", result)
elif choice == 2:
    result = num1 - num2
    print("Result :", result)
elif choice == 3:
    result = num1 * num2
    print("Result :", result)
elif choice == 4:
    if num2 == 0:
        print("Division by zero is not possible")
    else:
        result = num1 / num2
        print("Result :", result)
else:
    print("Invalid choice")