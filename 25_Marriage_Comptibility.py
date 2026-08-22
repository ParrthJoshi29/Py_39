'''write a program to accept birth day and birth month from user as separate input. decide zodiac sign from below table 
    Aries: March 21–April 19
    Taurus: April 20–May 20
    Gemini: May 21–June 21
    Cancer: June 22–July 22
    Leo: July 23–August 22
    Virgo: August 23–September 22
    Libra: September 23–October 22
    Scorpio: October 24–November 21
    Sagittarius: November 22–December 21
    Capricorn: December 22–January 19
    Aquarius: January 20–February 18
    Pisces: February 19–March 20 '''

b_day = int(input("Enter Your Birth-Day: "))
b_month = int(input("Enter Your Birth-Month: "))

if (b_month == 1 and b_day >= 20) or (b_month == 2 and b_day <= 18):
    print(f"Your Birthdate is {b_day}/{b_month} and Your Zodiac Sign is Aquarius")

elif (b_month == 2 and b_day >= 19) or (b_month == 3 and b_day <= 20):
    print(f"Your Birthdate is {b_day}/{b_month} and Your Zodiac Sign is Pisces")

elif (b_month == 3 and b_day >= 21) or (b_month == 4 and b_day <= 19):
    print(f"Your Birthdate is {b_day}/{b_month} and Your Zodiac Sign is Aries")

elif (b_month == 4 and b_day >= 20) or (b_month == 5 and b_day <= 20):
    print(f"Your Birthdate is {b_day}/{b_month} and Your Zodiac Sign is Taurus")

elif (b_month == 5 and b_day >= 21) or (b_month == 6 and b_day <= 21):
    print(f"Your Birthdate is {b_day}/{b_month} and Your Zodiac Sign is Gemini")

elif (b_month == 6 and b_day >= 22) or (b_month == 7 and b_day <= 22):
    print(f"Your Birthdate is {b_day}/{b_month} and Your Zodiac Sign is Cancer")

elif (b_month == 7 and b_day >= 23) or (b_month == 8 and b_day <= 22):
    print(f"Your Birthdate is {b_day}/{b_month} and Your Zodiac Sign is Leo")

elif (b_month == 8 and b_day >= 23) or (b_month == 9 and b_day <= 22):
    print(f"Your Birthdate is {b_day}/{b_month} and Your Zodiac Sign is Virgo")

elif (b_month == 9 and b_day >= 23) or (b_month == 10 and b_day <= 22):
    print(f"Your Birthdate is {b_day}/{b_month} and Your Zodiac Sign is Libra")

elif (b_month == 10 and b_day >= 24) or (b_month == 11 and b_day <= 21):
    print(f"Your Birthdate is {b_day}/{b_month} and Your Zodiac Sign is Scorpio")

elif (b_month == 11 and b_day >= 22) or (b_month == 12 and b_day <= 21):
    print(f"Your Birthdate is {b_day}/{b_month} and Your Zodiac Sign is Sagittarius")

elif (b_month == 12 and b_day >= 22) or (b_month == 1 and b_day <= 19):
    print(f"Your Birthdate is {b_day}/{b_month} and Your Zodiac Sign is Capricorn")

else:
    print("Invalid date")