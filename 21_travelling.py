'''write a program to decide which is cheaper approach to go from ahmedabad to delhi. by car or by train. 
consider person has his own petrol car  and he prefer to travel by 1st class train '''

train_price = int(input("Enter 1st Class Train Price: "))
petrol_price = int(input("Enter Petrol Price per Litre: "))
mileage = int(input("Enter Mileage of the car: "))
distance = int(input("Enter distance in kilometer: "))

petrol_needed = distance // mileage
cost = petrol_price * petrol_needed

print(f"By Car Price:{cost}\nBy Train Price:{train_price}\n")

if cost > train_price:
    print("User should go by Train")
    
else:
    print("User should go by Car")


