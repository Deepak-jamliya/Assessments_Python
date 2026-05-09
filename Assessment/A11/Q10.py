'''
10. Student ID Validity Checker (Count Odd Digits)
A school management system assigns numeric IDs to students. The administration wants to
verify IDs by checking how many odd digits are present in each ID number. IDs with more
odd digits are sent for manual review.

Write a program to count the number of odd digits in a given student ID using loops.

Input:
572943

Output:
Odd Digits Count = 3'''

# while loop
'''num = int(input("Enter number : "))
count = 0

while num > 0:
    digit = num % 10
    if digit % 2 != 0:
        count+=1
    num = num // 10
print("Odd Digits Count = ",count)'''

# for loop

num = int(input("Enter Number = "))
count = 0

for i in range(len(str(num))):
    digit = num % 10
    if digit%2 != 0:
        count+=1
    num = num // 10
print("Odd Digits Count = ",count)
