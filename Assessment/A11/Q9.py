'''
9. Neon Number LED Unlock Game
You're programming a new LED display game. The game level unlocks only when a neon number is entered.

A neon number is a number where the sum of the digits of its square is equal to the number itself.
Example: 9 → 9² = 81 → 8 + 1 = 9

Accept a number from the player.
Check whether it is a neon number using loops.

If true, display:
Glowing Success! You've found the Neon Number!

Otherwise display:
Try again! Not quite glowing yet.

Input:
9

Output:
Glowing Success! You've found the Neon Number!'''

# while loop
'''num = int(input("Enter number : "))
temp = num
sum = 0
num = num**2
while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10

if sum == temp:
    print("Glowing Success! You've found the Neon Number!")
else:
    print("Try again! Not quite glowing yet")'''


# for loop

num = int(input("Enter Number = "))
temp = num
sq = num * num
sum = 0

for i in range(len(str(sq))):
    digit = num % 10
    sum = sum + digit
    num = num // 10

if sum == temp:
    print("Glowing Success! You've found the Neon Number!")
else:
    print("Try again! Not quite glowing yet")