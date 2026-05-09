'''
9. Library Access System
   A library checks:

* If membership is active → Entry allowed
* If books issued < 3 → Can issue more books

Input:
Membership active (yes/no): yes
Books issued: 2

Output:
Entry allowed
Can issue more books
------------------------------------------------------------'''

check = input("Membership active (yes/no) : ")
book = int(input("Book issued : "))

if(check == "yes"):
    print("Entry allowed")

if(check == "no"):
    print("Entry not allowed")

if(book < 3):
    print("Can issue more books")

if(book >= 3):
    print("Can't issue more books")


