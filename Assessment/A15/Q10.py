'''
10.
Electricity Bill Processing System (Multi-House)

An electricity board processes bills for multiple houses in a society.

Write a program to:

- Read number of houses n
- For each house:
    - Read units consumed
    - Calculate bill using slab rates:

        First 100 units      → ₹5 per unit  
        Next 100 units      → ₹7 per unit  
        Above 200 units     → ₹10 per unit  

    - Apply conditions:
        - If bill > ₹2000 → add 10% surcharge  
        - If units < 50 → give ₹100 subsidy  

    - Print bill for each house

- After processing all houses:
    - Print total bill collected
    - Print highest bill

---

Input:
3
120
250
40

Output:
House 1 Bill = 640
House 2 Bill = 1700
House 3 Bill = 100

Total Collection = 2440
Highest Bill = 1700'''

num = int(input("Enter Number Of houses = "))
total = 0
highest = 0

for i in range(1,num+1):
    units = int(input(f"Enter Units Of House{i} = "))

    bill = 0

    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = (100 * 5) + ((units - 100) * 7)
    else:
        bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    
    if bill > 2000:
        bill = bill + (bill * 10/100)
    if units < 50:
        bill = bill - 100
        if bill <= 0:
            bill = 0

    print(f"House {i} Bill = ",bill)
    
    total = total + bill
    if highest < bill:
        highest = bill

print("Total collection = ",total)
print("Highest Bill = ",highest)
