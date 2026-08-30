# 3)   1    -8   27  -64  .....    1000

number = 1

print(number,end = " ") # 1
number  = number + 1

''' number = number + 1 # 2
number = number * min_number * number
print(number,end = " ")


number = number + 1 # 3
number = number * number * number
print(number,end = " ") '''

while number <= 10:
    term = number * number * number
    if number % 2 == 0:
        term = -term
    print(term, end=" ")
    number += 1

