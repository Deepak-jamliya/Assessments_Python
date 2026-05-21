'''
7. Remove Duplicate Words from a String

Voice Assistant Noise Correction System

A voice assistant records spoken commands from users.

Due to microphone disturbance and network lag, some words are repeated multiple 
times.

The company wants a Python program that removes duplicate words while maintaining 
the original order.

``
hello hello how are are you


Output:


hello how are you
'''

str = input("Enter Command = ")

check = ""

words = str.split()

i = 0
while i< len(words):
    if words[i] not in check:
        check = check + " " + words[i]
    i+=1
print(check)
