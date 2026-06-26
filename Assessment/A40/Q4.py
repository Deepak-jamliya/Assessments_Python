'''
4.
Assignment 10: Cyber Security (Strong Password Check)

A cybersecurity company considers a numeric password to be "strong" if every digit is even.

Task

Write a recursive function to check whether all digits of the given number are even.

Input 1
Enter Password:
248620
Output 1
Strong Password
Input 2
Enter Password:
248621
Output 2
Weak Password
'''

def even(n):
    if n == 0:
        return True 
    else:
        digit = n % 10
        if digit % 2 != 0:
            return False
        else:
            return even(n // 10)
def main():
    n = int(input("Enter Password: "))
    if even(n):
        print("Strong Password")
    else:
        print("Weak Password")
main()