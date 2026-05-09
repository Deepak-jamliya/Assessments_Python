'''
Assignment 13: Expression Evaluation

A shopping application applies offers using exponent and grouped calculations with unary adjustments.

Input:
25 + (5 * (6**2) // 3) - (-(8 % 5)) + (+2)
-------------------------------------------------------------------------------------------------------'''

print("""
25 + (5 * (6**2) // 3) - (- (8 % 5)) + (+2)
25 + (5 * 36 // 3) - (-3) + 2
25 + (180 // 3) + 3 + 2
25 + 60 + 3 + 2
85 + 3 + 2
88 + 2
90


""")
print(25 + (5 * (6**2) // 3) - (-(8 % 5)) + (+2))