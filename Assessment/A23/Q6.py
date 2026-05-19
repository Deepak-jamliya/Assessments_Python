'''
6.

Product Code Verification System

An e-commerce company wants to verify whether two product codes are rearranged versions of each 
other.

Conditions:
- Ignore spaces
- Ignore case sensitivity

Input:
Enter first product code: Dormitory
Enter second product code: Dirty Room

Output:
Both Product Codes are Matching
'''

code1 = input("Enter first product code : ")
code2 = input("Enter second product code : ")

code1 = code1.replace(" ","").lower()
code2 = code2.replace(" ","").lower()

if len(code1) != len(code2):
    print("Codes are not Matching")

else:
    code1s = sorted(code1)
    code2s = sorted(code2)

    if code1s == code2s:
        print("Both Product Codes are Matching")
    else:
        print("Codes are not Matching")