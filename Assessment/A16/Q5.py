'''
5. Digit Alternating Sum System

A coding system calculates alternating sum of digits (add, subtract, add...).

Write a program to:

Traverse digits from left to right
Add first digit, subtract second, add third, and so on
Display final alternating sum
If result is positive → print Positive Pattern
Else → print Negative Pattern

Input:
1234

Output:
Result = -2
Negative Pattern

Input:
8642

Output:
Result = 8
Positive Pattern'''

num=int(input("enter number "))
rev=0
while num>0:
    t=num%10
    rev=rev*10+t
    num=num//10

count=1
r1=0
r2=0
while rev>0:
    t=rev%10
    if count%2!=0:
        r1=r1+t
    else:
        r2=r2-t
    rev=rev//10
    count+=1

result=r1+r2
print("Result: ",result)
if result<0:
    print('Negative pattern')
else:
    print("Positive pattern ")