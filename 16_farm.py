'''
write a program to accept length and width of two different farm from user. and findout & display which farm is bigger 
'''
length1 = float(input("Enter length of FARM 1 : "))
width1 = float(input("Enter width  of FARM 1 : "))

length2 = float(input("Enter length of FARM 2 : "))
width2 = float(input("Enter width  of FARM 2 : "))

area1 = length1 * width1
area2 = length2 * width2

print()
print("Area of FARM 1 :", area1)
print("Area of FARM 2 :", area2)

if area1 > area2:
    print("FARM 1 is bigger by", area1 - area2, "square units")
elif area2 > area1:
    print("FARM 2 is bigger by", area2 - area1, "square units")
else:
    print("Both farms are of SAME size")