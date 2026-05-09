'''
Next Prime Cabin Number Generator

A luxury hotel gives only prime numbered cabins to VIP guests.

Manager enters the last allotted cabin number.
System must find the next available prime cabin number.

Write a program using loops.

Input:
24

Output:
Next Prime Cabin = 29'''

num = int(input("Enter Number = "))
temp = num+1
while True:
    i = 2
    prime = 1
    while i < num // 2:
        if num%i == 0:
            prime = 0
            break
        i+=1
    if prime:
        print("Next Prime Cabin = ",num)
        break
    num+=1
    


