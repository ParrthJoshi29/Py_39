'''
write a program to findout whether given shape is landscape or portrait or square using decision making statement if 
'''

length = float(input("Enter length : "))
width = float(input("Enter width  : "))

if length > width:
    print("The shape is LANDSCAPE")

if length < width:
    print("The shape is PORTRAIT")

if length == width:
    print("The shape is SQUARE")