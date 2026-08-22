''' write a program for male female marriage compatibility as per below link, 
accept birth day and birth month from user as separate input. decide zodiac sign as per 
previous example and then use zodiac sign to decide  marriage compatibility '''

male_day = int(input("Enter Male Birth-Day: "))
male_month = int(input("Enter Male Birth-Month: "))

female_day = int(input("Enter Female Birth-Day: "))
female_month = int(input("Enter Female Birth-Month: "))



if (male_month == 1 and male_day >= 20) or (male_month == 2 and male_day <= 18):
    male_zodiac = "Aquarius"

elif (male_month == 2 and male_day >= 19) or (male_month == 3 and male_day <= 20):
    male_zodiac = "Pisces"

elif (male_month == 3 and male_day >= 21) or (male_month == 4 and male_day <= 19):
    male_zodiac = "Aries"

elif (male_month == 4 and male_day >= 20) or (male_month == 5 and male_day <= 20):
    male_zodiac = "Taurus"

elif (male_month == 5 and male_day >= 21) or (male_month == 6 and male_day <= 21):
    male_zodiac = "Gemini"

elif (male_month == 6 and male_day >= 22) or (male_month == 7 and male_day <= 22):
    male_zodiac = "Cancer"

elif (male_month == 7 and male_day >= 23) or (male_month == 8 and male_day <= 22):
    male_zodiac = "Leo"

elif (male_month == 8 and male_day >= 23) or (male_month == 9 and male_day <= 22):
    male_zodiac = "Virgo"

elif (male_month == 9 and male_day >= 23) or (male_month == 10 and male_day <= 22):
    male_zodiac = "Libra"

elif (male_month == 10 and male_day >= 24) or (male_month == 11 and male_day <= 21):
    male_zodiac = "Scorpio"

elif (male_month == 11 and male_day >= 22) or (male_month == 12 and male_day <= 21):
    male_zodiac = "Sagittarius"

elif (male_month == 12 and male_day >= 22) or (male_month == 1 and male_day <= 19):
    male_zodiac = "Capricorn"

else:
    male_zodiac = "Invalid"



if (female_month == 1 and female_day >= 20) or (female_month == 2 and female_day <= 18):
    female_zodiac = "Aquarius"

elif (female_month == 2 and female_day >= 19) or (female_month == 3 and female_day <= 20):
    female_zodiac = "Pisces"

elif (female_month == 3 and female_day >= 21) or (female_month == 4 and female_day <= 19):
    female_zodiac = "Aries"

elif (female_month == 4 and female_day >= 20) or (female_month == 5 and female_day <= 20):
    female_zodiac = "Taurus"

elif (female_month == 5 and female_day >= 21) or (female_month == 6 and female_day <= 21):
    female_zodiac = "Gemini"

elif (female_month == 6 and female_day >= 22) or (female_month == 7 and female_day <= 22):
    female_zodiac = "Cancer"

elif (female_month == 7 and female_day >= 23) or (female_month == 8 and female_day <= 22):
    female_zodiac = "Leo"

elif (female_month == 8 and female_day >= 23) or (female_month == 9 and female_day <= 22):
    female_zodiac = "Virgo"

elif (female_month == 9 and female_day >= 23) or (female_month == 10 and female_day <= 22):
    female_zodiac = "Libra"

elif (female_month == 10 and female_day >= 24) or (female_month == 11 and female_day <= 21):
    female_zodiac = "Scorpio"

elif (female_month == 11 and female_day >= 22) or (female_month == 12 and female_day <= 21):
    female_zodiac = "Sagittarius"

elif (female_month == 12 and female_day >= 22) or (female_month == 1 and female_day <= 19):
    female_zodiac = "Capricorn"

else:
    female_zodiac = "Invalid"


print("\nMale Zodiac Sign:", male_zodiac)
print("Female Zodiac Sign:", female_zodiac)



if male_zodiac == "Invalid" or female_zodiac == "Invalid":
    print("Invalid Date")


elif (male_zodiac == "Aries" and female_zodiac == "Leo") or (male_zodiac == "Leo" and female_zodiac == "Aries"):
    print("Marriage Compatibility: Great Match")

elif (male_zodiac == "Aries" and female_zodiac == "Sagittarius") or (male_zodiac == "Sagittarius" and female_zodiac == "Aries"):
    print("Marriage Compatibility: Great Match")

elif (male_zodiac == "Aries" and female_zodiac == "Gemini") or (male_zodiac == "Gemini" and female_zodiac == "Aries"):
    print("Marriage Compatibility: Great Match")

elif (male_zodiac == "Aries" and female_zodiac == "Libra") or (male_zodiac == "Libra" and female_zodiac == "Aries"):
    print("Marriage Compatibility: Great Match")

elif (male_zodiac == "Aries" and female_zodiac == "Aquarius") or (male_zodiac == "Aquarius" and female_zodiac == "Aries"):
    print("Marriage Compatibility: Great Match")

elif (male_zodiac == "Taurus" and female_zodiac == "Virgo") or (male_zodiac == "Virgo" and female_zodiac == "Taurus"):
    print("Marriage Compatibility: Great Match")

elif (male_zodiac == "Taurus" and female_zodiac == "Capricorn") or (male_zodiac == "Capricorn" and female_zodiac == "Taurus"):
    print("Marriage Compatibility: Great Match")

elif (male_zodiac == "Taurus" and female_zodiac == "Cancer") or (male_zodiac == "Cancer" and female_zodiac == "Taurus"):
    print("Marriage Compatibility: Great Match")

elif (male_zodiac == "Taurus" and female_zodiac == "Scorpio") or (male_zodiac == "Scorpio" and female_zodiac == "Taurus"):
    print("Marriage Compatibility: Great Match")

elif (male_zodiac == "Taurus" and female_zodiac == "Pisces") or (male_zodiac == "Pisces" and female_zodiac == "Taurus"):
    print("Marriage Compatibility: Great Match")

elif (male_zodiac == "Gemini" and female_zodiac == "Leo") or (male_zodiac == "Leo" and female_zodiac == "Gemini"):
    print("Marriage Compatibility: Great Match")

elif (male_zodiac == "Gemini" and female_zodiac == "Libra") or (male_zodiac == "Libra" and female_zodiac == "Gemini"):
    print("Marriage Compatibility: Great Match")

elif (male_zodiac == "Gemini" and female_zodiac == "Aquarius") or (male_zodiac == "Aquarius" and female_zodiac == "Gemini"):
    print("Marriage Compatibility: Great Match")

elif (male_zodiac == "Cancer" and female_zodiac == "Virgo") or (male_zodiac == "Virgo" and female_zodiac == "Cancer"):
    print("Marriage Compatibility: Great Match")

elif (male_zodiac == "Cancer" and female_zodiac == "Scorpio") or (male_zodiac == "Scorpio" and female_zodiac == "Cancer"):
    print("Marriage Compatibility: Great Match")

elif (male_zodiac == "Cancer" and female_zodiac == "Pisces") or (male_zodiac == "Pisces" and female_zodiac == "Cancer"):
    print("Marriage Compatibility: Great Match")

elif (male_zodiac == "Leo" and female_zodiac == "Sagittarius") or (male_zodiac == "Sagittarius" and female_zodiac == "Leo"):
    print("Marriage Compatibility: Great Match")

elif (male_zodiac == "Leo" and female_zodiac == "Libra") or (male_zodiac == "Libra" and female_zodiac == "Leo"):
    print("Marriage Compatibility: Great Match")

elif (male_zodiac == "Leo" and female_zodiac == "Aquarius") or (male_zodiac == "Aquarius" and female_zodiac == "Leo"):
    print("Marriage Compatibility: Great Match")

elif (male_zodiac == "Virgo" and female_zodiac == "Capricorn") or (male_zodiac == "Capricorn" and female_zodiac == "Virgo"):
    print("Marriage Compatibility: Great Match")

elif (male_zodiac == "Virgo" and female_zodiac == "Scorpio") or (male_zodiac == "Scorpio" and female_zodiac == "Virgo"):
    print("Marriage Compatibility: Great Match")

elif (male_zodiac == "Capricorn" and female_zodiac == "Scorpio") or (male_zodiac == "Scorpio" and female_zodiac == "Capricorn"):
    print("Marriage Compatibility: Great Match")

elif (male_zodiac == "Capricorn" and female_zodiac == "Pisces") or (male_zodiac == "Pisces" and female_zodiac == "Capricorn"):
    print("Marriage Compatibility: Great Match")

elif (male_zodiac == "Scorpio" and female_zodiac == "Pisces") or (male_zodiac == "Pisces" and female_zodiac == "Scorpio"):
    print("Marriage Compatibility: Great Match")



elif (male_zodiac == "Aries" and female_zodiac == "Virgo") or (male_zodiac == "Virgo" and female_zodiac == "Aries"):
    print("Marriage Compatibility: Favorable Match")

elif (male_zodiac == "Aries" and female_zodiac == "Pisces") or (male_zodiac == "Pisces" and female_zodiac == "Aries"):
    print("Marriage Compatibility: Favorable Match")

elif (male_zodiac == "Taurus" and female_zodiac == "Leo") or (male_zodiac == "Leo" and female_zodiac == "Taurus"):
    print("Marriage Compatibility: Favorable Match")

elif (male_zodiac == "Taurus" and female_zodiac == "Libra") or (male_zodiac == "Libra" and female_zodiac == "Taurus"):
    print("Marriage Compatibility: Favorable Match")

elif (male_zodiac == "Gemini" and female_zodiac == "Virgo") or (male_zodiac == "Virgo" and female_zodiac == "Gemini"):
    print("Marriage Compatibility: Favorable Match")

elif (male_zodiac == "Gemini" and female_zodiac == "Capricorn") or (male_zodiac == "Capricorn" and female_zodiac == "Gemini"):
    print("Marriage Compatibility: Favorable Match")

elif (male_zodiac == "Cancer" and female_zodiac == "Leo") or (male_zodiac == "Leo" and female_zodiac == "Cancer"):
    print("Marriage Compatibility: Favorable Match")

elif (male_zodiac == "Cancer" and female_zodiac == "Sagittarius") or (male_zodiac == "Sagittarius" and female_zodiac == "Cancer"):
    print("Marriage Compatibility: Favorable Match")

elif (male_zodiac == "Leo" and female_zodiac == "Scorpio") or (male_zodiac == "Scorpio" and female_zodiac == "Leo"):
    print("Marriage Compatibility: Favorable Match")

elif (male_zodiac == "Leo" and female_zodiac == "Pisces") or (male_zodiac == "Pisces" and female_zodiac == "Leo"):
    print("Marriage Compatibility: Favorable Match")

elif (male_zodiac == "Virgo" and female_zodiac == "Aquarius") or (male_zodiac == "Aquarius" and female_zodiac == "Virgo"):
    print("Marriage Compatibility: Favorable Match")

elif (male_zodiac == "Libra" and female_zodiac == "Pisces") or (male_zodiac == "Pisces" and female_zodiac == "Libra"):
    print("Marriage Compatibility: Favorable Match")

elif (male_zodiac == "Scorpio" and female_zodiac == "Aries") or (male_zodiac == "Aries" and female_zodiac == "Scorpio"):
    print("Marriage Compatibility: Favorable Match")

elif (male_zodiac == "Scorpio" and female_zodiac == "Leo") or (male_zodiac == "Leo" and female_zodiac == "Scorpio"):
    print("Marriage Compatibility: Favorable Match")

elif (male_zodiac == "Aquarius" and female_zodiac == "Scorpio") or (male_zodiac == "Scorpio" and female_zodiac == "Aquarius"):
    print("Marriage Compatibility: Favorable Match")

elif (male_zodiac == "Aquarius" and female_zodiac == "Pisces") or (male_zodiac == "Pisces" and female_zodiac == "Aquarius"):
    print("Marriage Compatibility: Favorable Match")

else:
    print("Marriage Compatibility: Not Favorable")