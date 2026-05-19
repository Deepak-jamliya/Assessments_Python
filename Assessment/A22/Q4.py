'''
4.
Consonant Counter in Student Name Record

A school management system wants to count how many consonants are present in student names.

Input: Enter student name: Ajay Singh Thakur

Output: Total consonants: 11

NOTE:

Ignore case sensitivity (treat A and a same)
Consider only English alphabets for vowel/consonant counting
Vowels: A, E, I, O, U
'''

str = input("Enter student name = ")
count = 0

str1 = str.lower()
for i in range(len(str1)):
    ch = str1[i]
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == " ":
        pass
    else:
        count+=1
print("Total Consonants = ",count)

    
