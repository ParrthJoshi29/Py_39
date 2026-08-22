'''
create two list fruits and vegis (both might have duplicate values) 
convert both list into single set refrigerator 

'''

fruits = ["apple", "banana", "mango", "apple", "grapes", "banana"]
vegis = ["potato", "tomato", "onion", "tomato", "brinjal", "potato"]

print("Fruits list :", fruits)
print("Vegis list  :", vegis)
print("Total items with duplicates :", len(fruits) + len(vegis))


refrigerator = set(fruits + vegis)

print()
print("Refrigerator :", refrigerator)
print("Unique items :", len(refrigerator))