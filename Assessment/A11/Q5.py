'''
5. Count Factors of Number
A mathematics learning app gives practice questions where students must
know how many factors a number has. The app should automatically count the
total factors of the entered number.
Write a program to count total factors of a number using loops.

Input:
12

Output:
Factors Count = 6'''


# while loop
num = int(input("Enter Number = "))
count = 0
i = 1
while i <= num:
    if num%i == 0:
        count+=1
    i+=1
print("factors Count = ",count)

# for loop
'''num = int(input("Enter nummber : "))
count = 0

for i in range(1,num+1):
    if num % i == 0:
        count+=1

print("Factors count = ",count)'''