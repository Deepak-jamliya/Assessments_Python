'''4.
Armstrong Number Finder

A digital number analysis system checks for Armstrong numbers within a range.
The user enters starting and ending numbers.
The system finds all Armstrong numbers using nested loops.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Armstrong Numbers are:
1
153
370
371
407'''

s = int(input("Enter Starting Number = "))
e = int(input("Enter Ending Number = "))

for i in range(s,e+1):
    power = len(str(i))
    temp = i
    sum = 0
    while i > 0:
        digit = i % 10
        sum = sum + digit**power
        i = i // 10
    if temp == sum:
        print(sum)
    