'''
write a program to findout elder brother from given two brother's age. 
'''


age1 = int(input("Enter age of BROTHER 1 : "))
age2 = int(input("Enter age of BROTHER 2 : "))

if age1 > age2:
    print("BROTHER 1 is elder by", age1 - age2, "years")
elif age2 > age1:
    print("BROTHER 2 is elder by", age2 - age1, "years")
else:
    print("Both brothers are of the same age")