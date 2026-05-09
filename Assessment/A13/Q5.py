'''
5. Next Prime ID Generator – Smart Version

A company gives prime numbered employee IDs to premium staff.

Manager enters current ID.
System must:

- Find next prime number after current ID
- Find difference between current ID and next prime

Write a program using loops.

Input:
20

Output:
Next Prime ID = 23
Gap = 3'''

num = int(input("Enter Number = "))
next = num + 1

while True:
    i = 2
    is_prime = 1
    while i < next//2:
        if next%i == 0:
            is_prime = 0
            break
        i+=1
    if is_prime:
        print("Next Prime = ",next)
        print("Gap = ",next - num)
        break
    next+=1