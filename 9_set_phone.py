'''
assume there are two list friends and families both have 10 mobile numbers. it is quite possible that both list have same numbers. you job is to create telephone_directory which must not contain any duplicate number using set 
write a program to convert 3 digit amount into words
input :123 output one two three
amount = 123

write a program to convert 4 digit amount into words
input :1234 output one two three four 

#write a program to convert given grams into kg and remaining grams.
input : 2500 grams
output : 2 kg and 500 grams 

'''
friends = [9876543210, 9825011223, 9998877665, 9723456789, 9033445566,
           9876543210, 9601122334, 9825011223, 9712345678, 9909988776]

families = [9825011223, 9426778899, 9998877665, 9558877441, 9377665544,
            9265544332, 9723456789, 9106677889, 9426778899, 9879001122]

print("Friends numbers  :", len(friends))
print("Families numbers :", len(families))
print("Total numbers with duplicates :", len(friends) + len(families))

telephone_directory = set(friends + families)

print()
print("TELEPHONE DIRECTORY :")
print(telephone_directory)
print()
print("Unique numbers :", len(telephone_directory))