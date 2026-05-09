'''
Assignment 10: Time Conversion

Convert total seconds into hours, minutes, and seconds.

Input:
Total seconds = 7384

Expected Output:
Hours = 2
Minutes = 3
Seconds = 4
------------------------------------------------------------------------------------'''


total = int(input("Enter total duration in seconds : "))

hrs = total // 3600
remain = total % 3600
min = remain // 60
sec = remain % 60

print(f"Hours = {hrs}\nMinutes = {min}\nSeconds = {sec}")