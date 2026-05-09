'''Assignment 6: Data Storage Conversion

A user wants to convert data from GB into MB and KB.

Input:
Data = 5 GB

Expected Output:
In MB = 5120.0
In KB = 5242880.0
--------------------------------------------------------------------------'''


Data = int(input("Enter storage in GB : "))
MB = float(Data * 1024)
KB = float(MB * 1024)

print(f"In MB = {MB}\nIn KB = {KB}")
