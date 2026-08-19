'''write a program to findout which is cheaper approach to buy IPhone 17 pro max.  consider user is going usa should he buy 
iphone from usa or from india. take required input from user and suggest from where he should buy i-phone (india or USA)'''

us_price = float(input("Enter USA IPhone Price in Dollar: "))
i_price = float(input("Enter India IPhone Price in Rupee: "))
rupee = float(input("Enter Rupee per Dollar: "))


u_price = us_price * rupee

print("USA Price in Rupee:",u_price)
print("Indian Price in Rupee:",i_price)

if u_price > i_price:
    print("He should buy IPhone from India")
else:
   print("He should buy IPhone from USA") 