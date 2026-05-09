'''
2.
Digit Threshold Break Analyzer

A monitoring system analyzes numeric IDs to detect high-value digits. 
The system keeps adding digits one by one, but stops processing as soon as the running sum exceeds a given threshold.

Write a program to:

Accept a number and a threshold value
Traverse digits from right to left
Keep adding digits to a running sum
Display each digit added
The moment sum exceeds the threshold, stop using break
Display:
- Digits processed
- Final sum
- Count of digits processed
If threshold is never exceeded, print Threshold Not Reached

Use loops and break wherever required.

Input:
57294
Threshold = 10

Output:
Digits Processed: 4 9
Sum = 13
Count = 2
Threshold Exceeded

Input:
1234
Threshold = 15

Output:
Digits Processed: 4 3 2 1
Sum = 10
Count = 4
Threshold Not Reached '''

num = int(input("Enter Number = "))
threshold = int(input("Enter Threshold = "))

sum = 0
count = 0
check = 0

print("Digits Processed = ",end = " ")
while num > 0:
    digit = num % 10
    sum = sum + digit
    print(digit, end = " ")
    count+=1
    if sum > threshold:
        check = 1
        break
    num = num // 10
print("\nSum = ",sum)
print("Count = ",count)

if check == 0:
    print("Threshold Never Exceeedded")
else:
    print("Threshold Exceeded")

'''1.
Digit Frequency Balance Analyzer

A data security system analyzes numeric IDs to check digit distribution patterns.

For a given number, the system evaluates how frequently each digit appears.

Write a program to:

Count how many times each digit appears in the number
Display only the digits that appear more than once
Find the total count of repeated digits
Find the digit with maximum frequency
If no digit repeats, print Unique Number
If at least one digit repeats, print Repeated Pattern Detected

Use loops wherever required.

Input:
1223451

Output:
Repeated Digits: 1 2
Total Repeated Count = 4
Max Frequency Digit = 1
Repeated Pattern Detected'''
'''
num = input("Enter Number = ")
check = ""
repeat = ""

for digit in num:
    if digit in check:
        print(digit,end = " ")
        repeat = repeat + digit
        repeat = repeat + digit
    check = check + digit

print("\nTotal Repeated Count = ",len(repeat))'''








