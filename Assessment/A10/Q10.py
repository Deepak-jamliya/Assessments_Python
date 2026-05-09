'''
. Even Numbers Between Two Numbers*
A teacher wants to assign only even roll numbers for a special activity. The system should display all
 even numbers between two given numbers.
Write a program to *display all even numbers between two numbers using loops*.

Input: 10, 20
Output: 10 12 14 16 18 20'''

num1,num2 = map(int,input("Enter num1 and num2 = ").split())

# while loop

i = num1
while i <= num2:
    if i%2 == 0:
        print(i,end = " ")
    i+=1

# for loop
'''for i in range(num1,num2+1):
    if i%2 == 0:
        print(i,end = " ")
    else:
        pass'''