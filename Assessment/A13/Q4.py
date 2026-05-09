'''
4. Prime Security Code Checker – Advanced

A high-security lab accepts only prime numbered access codes.

When a user enters a number, the software must:

- Check whether number is prime
- If prime, print next immediate prime number
- If not prime, print previous immediate prime number

Write a program using loops only.

Input:
29

Output:
Prime Number
Next Prime = 31
'''

num = int(input("Enter Number = "))
next = num + 1
prev = num - 1

if num <= 1:
    print("Not Prime")

else:
    i = 2
    prime = 1
    while i <= num//2:
        if num%i == 0:
            prime = 0
            break
        i+=1
if prime:
    print("Prime Number")
    while True:
        i = 2
        prime = 1
        while i < next//2:
            if next%i == 0:
                prime = 0
                break
            i+=1
        if prime:
            print("Next Prime = ",next)
            break
        next+=1
else:
    while True:
        i = 2
        prime = 1
        while i <= prev//2:
            if prev%i == 0:
                prime = 0
                break
            i+=1
        if prime:
            print("Previous Prime = ",prev)
            break
        prev-=1



