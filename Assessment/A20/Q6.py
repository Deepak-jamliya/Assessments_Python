'''6.
Palindrome Number Range Checker

A barcode verification system checks for palindrome numbers within a specific range.
The user enters starting and ending numbers.
The system displays all palindrome numbers using nested loops.

Input:
Enter starting number: 100
Enter ending number: 200

Output:
Palindrome Numbers are:
101
111
121
131
141
151
161
171
181
191'''

s = int(input("Enter Starting Number = "))
e = int(input("Enter Ending Number = "))

for i in range(s,e+1):
    rev = 0
    temp = i
    while i > 0:
        digit = i % 10
        rev = rev * 10 + digit
        i = i // 10
    if temp == rev:
        print(rev)
        