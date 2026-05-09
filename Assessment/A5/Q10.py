'''
10. Online Exam System
    System evaluates exam conditions:

* If marks ≥ 40 → Pass
* If attendance ≥ 75 → Eligible for certificate

Input:
Enter marks: 60
Enter attendance: 80

Output:
Pass
Eligible for certificate
------------------------------------------------------------------------------'''

marks = int(input("Enter marks : "))
atten = int(input("Enter attendance : "))

if(marks >= 40):
    print("Pass")
if(marks < 40):
    print("Fail")

if(atten >= 75):
    print("Eligible for certificate")
if(atten < 75):
    print("not Eligible for certificate")