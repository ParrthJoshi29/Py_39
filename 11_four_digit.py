'''
write a program to convert 4 digit amount into words
input :1234 output one two three four 

'''

words = ["zero", "one", "two", "three", "four",
         "five", "six", "seven", "eight", "nine"]

amount = int(input("Enter 4 digit amount : "))

thousand_digit = amount // 1000
hundred_digit = (amount // 100) % 10
ten_digit = (amount // 10) % 10
unit_digit = amount % 10

print("Amount   :", amount)
print("In words :", words[thousand_digit], words[hundred_digit],
      words[ten_digit], words[unit_digit])