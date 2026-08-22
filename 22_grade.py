'''
Write a program that takes a 5 subject marks from user. calculate total and average  and prints the grade using the following conditions:

| Percentage | Grade |
| ---------- | ----- |
| 90–100     | A+    |
| 80–89      | A     |
| 70–79      | B     |
| 60–69      | C     |
| 50–59      | D     |
| below 50   | Need to improve  |
----------------------------------------
'''

m1 = float(input("Enter marks of subject 1 : "))
m2 = float(input("Enter marks of subject 2 : "))
m3 = float(input("Enter marks of subject 3 : "))
m4 = float(input("Enter marks of subject 4 : "))
m5 = float(input("Enter marks of subject 5 : "))

total = m1 + m2 + m3 + m4 + m5
average = total / 5
percentage = total / 500 * 100

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "Need to improve"

print()
print("Total marks :", total, "out of 500")
print("Average     :", round(average, 2))
print("Percentage  :", round(percentage, 2), "%")
print("Grade       :", grade)