'''
Assignment 7: Cricket Run Rate

In cricket, overs are given in decimal format (e.g., 48.3 means 48 overs and 3 balls). Convert overs into total balls and calculate run rate.

Input:
Total runs = 275
Overs = 48.3

Expected Output:
Total Balls = 291
Run Rate = 5.67
----------------------------------------------------------------------------------------------------'''


total = int(input("Enter total runs : "))
overs = float(input("Enter overs : "))

tovers = int(overs)
ball = (overs - tovers)*10
tball = (tovers*6) + ball

aovers = tovers + (ball/6)

rr = total/aovers



print(f"Total Balls = {tball}\nRun rate = {round(rr,2)}")

