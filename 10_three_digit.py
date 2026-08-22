'''
write a program to convert 3 digit amount into words
input :123 output one two three
amount = 123

'''

words = ["zero", "one", "two", "three", "four",
         "five", "six", "seven", "eight", "nine"]

amount = int(input("Enter 3 digit amount : "))

hundred_digit = amount // 100
ten_digit = (amount // 10) % 10
unit_digit = amount % 10

print("Amount   :", amount)
print("In words :", words[hundred_digit], words[ten_digit], words[unit_digit])

