'''4. Electricity Bill Management System

You are developing an Electricity Bill Management System for a power distribution company.
The system helps calculate electricity bills for customers based on their unit consumption.

Sometimes, the operator may try to calculate the bill or apply surcharge before entering the
number of units consumed. Your system must handle such situations properly.

👉 Important Condition:
If units are not entered, the system should display:
"Please enter units consumed first"
and should not perform further calculations.

The system should be menu-driven and must continue running until the user selects Exit. 
All operations should be handled using match-case.

Menu Options:
1 → Enter Units Consumed
2 → Calculate Bill Amount

* First 100 units → ₹5 per unit
* Next 100 units → ₹7 per unit
* Above 200 units → ₹10 per unit
  3 → Apply Surcharge
* If bill > 2000 → 10% surcharge
* Otherwise → 5% surcharge
  4 → Display Final Bill
  5 → Exit

---

Sample Run 1:
Input:
Enter your choice: 2

Output:
Please enter units consumed first

---

Sample Run 2:
Input:
Enter your choice: 1
Enter units consumed: 250

Output:
Units recorded successfully

---

Sample Run 3:
Input:
Enter your choice: 2

Output:
Bill Amount: 1700

(Explanation: 100×5 = 500, 100×7 = 700, 50×10 = 500 → Total = 1700)

---

Sample Run 4:
Input:
Enter your choice: 3

Output:
Surcharge: 85

---

Sample Run 5:
Input:
Enter your choice: 4

Output:
----- Final Bill -----
Units: 250
Bill Amount: 1700
Surcharge: 85
Total Payable: 1785

---

Sample Run 6 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

---

Sample Run 7 (Exit):
Input:
Enter your choice: 5

Output:
Exiting system... Thank you!'''


units = None
bill = 0

while True:
    print("\n\n------ MENU OPTIONS ------")
    print("1 → Enter Units Consumed")
    print("2 → Calculate Bill Amount")
    print("3 → Apply Surcharge")
    print("4 → Display Final Bill")
    print("5 → Exit")

    choice = int(input("Enter Choice = "))
    match choice:
        case 1:
            units = int(input("Enter Units Consumed = "))
            print("Units recorded successfully")
        case 2:
            if units == None:
                print("Please enter units consumed first")
            else:
                if units <= 100:
                    bill = units * 5
                    print("Bill Amount = ",bill)
                elif units <= 200:
                    bill = (100 * 5) + ((units - 100) * 7)
                    print("Bill Amount = ",bill)
                else:
                    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
                    print("Bill Amount = ",bill)
        case 3:
            if units == None:
                print("Please enter units consumed first")
            else:
                if bill > 2000:
                    surcharge = bill * 10/100
                    print("Surcharge = ",surcharge)
                else:
                    surcharge = bill * 5/100
                    print("Surcharge = ",surcharge)
        case 4:
            print("------ FINAL BILL ------")
            print("Units = ",units)
            print("Bill Amount = ",bill)
            print("Surcharge = ",surcharge)
            total = bill + surcharge
            print("Total Payable = ",total)
        case 5:
            print("Exiting system... Thank you!")
            break
        case _:
            print("Invalid Choice")
            
            

                    