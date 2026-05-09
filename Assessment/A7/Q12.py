'''
12. Restaurant Bill with GST System

A restaurant applies GST based on the total bill amount:

* Up to ₹1000 → 5% GST
* ₹1001 to ₹5000 → 12% GST
* Above ₹5000 → 18% GST
  Additionally, if the bill exceeds ₹3000, a service charge of ₹200 is added.

Write a Python program to calculate the final bill.

Input:
Enter bill amount: 4000

Output:
Final Bill Amount: ₹4680
--------------------------------------------------------------------------------------------'''

bill = int(input("Enter Bill amount : "))

if bill <= 1000:
  fbill = bill * 0.05
  bill = fbill + bill
  print("Final Bill Amount : ",bill)
elif bill > 1000 and bill < 5000:
  if bill > 3000:
      fbill = bill * 0.12 + 200
      bill = fbill + bill
      print("Final Bill Amount : ",bill)
  else:
      fbill = bill * 0.12
      bill = fbill + bill
      print("Final Bill Amount : ",bill) 
else:
    fbill = bill * 0.18
    bill = fbill + bill
    print("Final Bill Amount : ",bill)