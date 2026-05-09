'''3)	WAP to find out all the leap years between two entered years'''

s = int(input("Enter Starting Year = "))
e = int(input("Enter Ending Year = "))

for i in range(s,e+1):
    if (i%400 == 0) or (i%4 == 0 and i%100 != 0):
        print(i)