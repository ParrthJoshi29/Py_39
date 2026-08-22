'''
 Create Dictionary store 10 different types of detail about you. 
    add dob into it.
    display Dictionary
    remove dob from Dictionary 
    get only keys 
    get only values 
    update age key 
    update city key using update method 
    copy Dictionary into another Dictionary using shallow copy technique
    empty copied Dictionary 
    display empty Dictionary 
'''

my_detail = {"name": "Parth",
             "age": 25,
             "gender": "Male",
             "city": "Ahmedabad",
             "state": "Gujarat",
             "pincode": 380015,
             "height": 5.9,
             "married": False,
             "hobbies": ["coding", "cricket"],
             "language": ("Gujarati", "Hindi", "English")}

my_detail["dob"] = "15-08-2000"
print("After adding dob :")
print(my_detail)

print()
print("Display dictionary :")
print(my_detail)

my_detail.pop("dob")
print()
print("After removing dob :")
print(my_detail)

print()
print("Only keys   :", my_detail.keys())


print("Only values :", my_detail.values())


my_detail["age"] = 26
print()
print("After updating age :", my_detail["age"])


my_detail.update({"city": "Surat"})
print("After update() on city :", my_detail["city"])


copied_detail = my_detail.copy()
print()
print("Copied dictionary :")
print(copied_detail)


copied_detail.clear()


print()
print("Copied dictionary after clear() :", copied_detail)
print("Original dictionary is safe     :")
print(my_detail)