'''
Assignment 11: Expression Evaluation

A billing system applies nested calculations with discounts and extra charges using brackets and unary operators.

Input:
50 + (10 * (+(2**3))) / 4 - (-6 % 4)
-------------------------------------------------------------------------------------------------------------------------'''


print("""
   50 + (10 * (+ 8)) / 4 - (-6 % 4)
   50 + (10 * (8)) / 4 - (-6 % 4)
   50 + 80 / 4 - (-6 % 4)
   50 + 80 / 4 - 2
   50 + 20 - 2
   70 - 2
   68""")
print("\n\n",50 + (10 * (+(2**3))) / 4 - (-6 % 4))