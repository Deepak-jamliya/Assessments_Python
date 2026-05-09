'''3.
Prime Number Range Checker

A cyber security system generates prime numbers for encryption analysis.
The user enters a starting number and ending number.
The system checks and displays all prime numbers between the given range using nested loops.

Input:
Enter starting number: 10
Enter ending number: 50

Output:
Prime Numbers are:
11
13
17
19
23
29
31
37
41
43
47'''

s = int(input("Enter Starting Number = "))
e = int(input("Enter Ending Number = "))

for i in range(s,e+1):
    t = 2
    prime = 1
    while t < i//2:
        if i%t == 0:
            prime = 0
            break
        t+=1
    if prime:
        print(i)
    