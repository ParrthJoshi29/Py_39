# write a program to findout whether given year is millennium year or not. using if else decision making statements.

year = int(input("Enter year to check if it is millennium or not: "))

if year % 1000 == 0:
    print("It is a Millennium Year!")

else:
    print("It is Not a Millennium Year!")