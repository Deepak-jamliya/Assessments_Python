'''
5.
 Hospital Record System (Search Digit)


A hospital stores patient IDs as numbers. The administrator wants to verify whether a specific 
digit exists in a patient ID.

Task

Write a recursive function to determine whether a given digit is present.

Input
Enter Patient ID:
5837264

Enter Digit:
7
Output
Digit Found
'''

def find(n,m):
    if n == 0 and m == 0:
        return True
    else:
        digit = n % 10
        if digit == m:
            return True
        else:
            return find(n//10, m)
def main():
    n = int(input("Enter Patient ID = "))
    m = int(input("Enter Digit = "))
    if find(n,m):
        print("Digit Found")
    else:
        print("Not Found")   
main()         