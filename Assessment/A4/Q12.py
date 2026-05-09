'''
Assignment 12: Expression Evaluation

A gaming score system calculates bonus points using exponent and applies penalties using unary negative values and brackets.

Input:
100 - (20 * (3**2)) + (40 / (+5)) - (-3)
-------------------------------------------------------------------------------------------------------------------------'''

print("""
100 - (20 * (3**2)) + (40 / (+5)) - (-3)
100 - (20 * 9) + (40 / 5) + 3
100 - 180 + (40/5) + 3
100 - 180 + 8 + 3
-80 + 8 + 3
-72 + 3
-69

""")

print(100 - (20 * (3**2)) + (40 / (+5)) - (-3))