from operations.perfect import perfect
from operations.prime_no import prime
from operations.rev_no import rev
from operations.factorial_no import factorial
from operations.factors_of_no import factors

while True:
    print("\nMENU")
    print("1. Check Perfect Number")
    print("2. Check Prime Number")
    print("3. Find Reverse of a Number")
    print("4. Calculate Factorial")
    print("5. Display Factors of a Number")
    print("6. Exit")

    choice = int(input("Enter Choice = "))
    match choice:
        case 1:
            n = int(input("Enter Number = "))
            if perfect(n):
                print(n,"is a perfect Number")
            else:
                print(n,"is not a perfect Number")
        case 2:
            n = int(input("Enter Number = "))
            print(prime(n))

        case 3:
            n = int(input("Enter Number = "))
            print("Reverse Number :", rev(n))

        case 4:
            n = int(input("Enter Number = "))
            print("Factorial :", factorial(n))

        case 5:
            n = int(input("Enter Number = "))
            print("Factors :", *factors(n))

        case 6:
            print("Program Terminated")
            break

        case _:
            print("Invalid Choice. Try Again.")