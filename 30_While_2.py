# 2)   1    8   27   125  ....... 1000

number = 1
cube = 0

print(number,end = " ")

'''number = number + 1 # 2   
cube  = number * number * number # 0 = 2 * 2 * 2 = 8
print(cube,end = " ") # 8

number = number + 1 # 3 
cube = number * number * number # 27 = 3 * 3 * 3 
print(cube,end = " ")


number = number + 1 # 4
cube = number * number * number # 27 = 4 * 4 * 4 
print(cube,end = " ")


number = number + 1 # 5
cube = number * number * number # 125 = 5 * 5 * 5 
print(cube,end = " ")'''

while number <= 9:
    number = number + 1  
    cube  = number * number * number 
    print(cube,end = " ") 
