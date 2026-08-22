'''
write a program to display dinomations of currency for given amount
input : 387 Rupees 
output : 
200 x 1 = 200
100 x 1 = 100
50 x 1 =  50
20 x 1 =  20
10 x 1 =  10
5 x 1 =   05
2 x 1 =   02
1 x 1 =   01

'''


amount = int(input("Enter amount in Rupees : "))

balance = amount

note_500 = balance // 500
balance = balance % 500

note_200 = balance // 200
balance = balance % 200

note_100 = balance // 100
balance = balance % 100

note_50 = balance // 50
balance = balance % 50

note_20 = balance // 20
balance = balance % 20

note_10 = balance // 10
balance = balance % 10

note_5 = balance // 5
balance = balance % 5

note_2 = balance // 2
balance = balance % 2

note_1 = balance

print()
print("Denomination for Rs.", amount)
print("500 x", note_500, "=", 500 * note_500)
print("200 x", note_200, "=", 200 * note_200)
print("100 x", note_100, "=", 100 * note_100)
print(" 50 x", note_50, "=", 50 * note_50)
print(" 20 x", note_20, "=", 20 * note_20)
print(" 10 x", note_10, "=", 10 * note_10)
print("  5 x", note_5, "=", 5 * note_5)
print("  2 x", note_2, "=", 2 * note_2)
print("  1 x", note_1, "=", 1 * note_1)