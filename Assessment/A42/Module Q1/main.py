from numbers_q import duplicate_ages,second_highest_age,senior_count
from strings_q import long_name,start_vowels


emp = []
no = int(input("Enter Number of Employees = "))
for i in range(no):
    age = int(input(f"Enter age {i+1} = "))
    emp.append(age)

names = input("Enter Names = ")


while True:
    print("\n========== EMPLOYEE DATA PROCESSING SYSTEM ==========")
    print("1. Find Second Highest Employee Age")
    print("2. Count Senior Employees")
    print("3. Remove Duplicate Ages")
    print("4. Count Names Starting with a Vowel")
    print("5. Find Longest Employee Name")
    print("6. Exit")
    print("====================================================")

    choice = int(input("Enter Choice = "))
    match choice:
        case 1:
            print("\nSecond Highest Employee Age :")
            print(second_highest_age.sec(emp))
        case 2:
            print("\nSenior Employee Count :")
            print(senior_count.count_emp(emp))
        case 3:
            print("\nUnique Ages :")
            print(duplicate_ages.dup(emp))
        case 4:
            print("\nNames Starting with Vowel : ")
            print(start_vowels.cvowels(names))
        case 5:
            print("\nLongest Employee Name : ")
            print(long_name.longest(names))
        case 6:
            print("Exiting Program")
            break
        case _:
            print("Invalid Choice")
