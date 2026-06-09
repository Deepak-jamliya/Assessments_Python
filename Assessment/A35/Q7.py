'''
7.
=========================================
MISSING ALPHABET FINDER
=========================================

Enter a sentence and find which
alphabets are missing.

Menu:
1. Enter Sentence
2. Display Missing Alphabets
3. Count Missing Alphabets
4. Exit

Requirements:
- Use Set containing a-z.
'''
aplphaset = frozenset('abcdefghijklmnopqrstuvwxyz')
sen = set()

while True:
    print("\nMenu")
    print("1.Enter Sentance")
    print("2. Display Missing Alphabets")
    print("3. Count Missing Alphabets")
    print("4. Exit")

    choice = int(input("Enter Choice = "))
    match choice:
        case 1:
            sentance = input("Enter Sentance = ").lower()
            sen = {ch for ch in sentance}
        case 2:
            print("Missing alphabets = ")
            print(aplphaset - sen)
        case 3:
            print("Count = ",len(aplphaset - sen))
        case 4:
            print("Exiting Menu")
            break
        case _:
            print("Invalid Choice")

