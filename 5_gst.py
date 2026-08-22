'''
 write a program to calculate total amount from user given amount and gst rate 
input : amount 100 rate 18 total amount = 18
input : amount 1000 rate 5 total amount = 1050

'''


amount = float(input("Enter amount       : "))
rate = float(input("Enter GST rate (%) : "))

gst_amount = amount * rate / 100
total_amount = amount + gst_amount

print("Amount       :", amount)
print("GST rate     :", rate, "%")
print("GST amount   :", gst_amount)
print("Total amount :", total_amount)

