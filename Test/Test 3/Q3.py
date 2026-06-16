'''3. 3.5 marks

Secure Password Analysis

A cybersecurity team wants to identify pairs of passwords having no common characters.

Problem Statement:

Given N strings, count the number of pairs that do not share any common character.

Example:

Input

N = 4
passwords[] = {"abc", "de", "fg", "ad"}

Output

3

Explanation

("abc","de") 
("abc","fg")
("de","fg")'''

n = int(input("Enter Number Of strings = "))

passwords = []
for i in range(n):
    x = input(f"Enter String {i+1}= ")
    passwords.append(x)

count = 0
for i in range(n):
    for j in range(i+1,n):
        common = 0
        for ch in passwords[i]:
            if ch in passwords[j]:
                common = 1
                break
        if common == 0:
            count+=1
print(count)



    