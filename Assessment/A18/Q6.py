'''
6.
Data Validation System – Character Identifier
A system needs to validate user input characters.
If the input is:
Alphabet → display "Alphabet"
Digit → display "Digit"
Otherwise → display "Special Character"
Write a program using inline if to classify the character.'''

a = input("Enter Character = ")

print("Alphabet") if "a"<=a<="z" or "A"<=a<="Z" else print("Digit") if "0"<=a<="9" else print("Special Character")
