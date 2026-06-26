'''
7.
Assignment: File Compression System (String Compression)

A file compression company wants to reduce the size of text files before storing them. 
One simple compression technique is to replace consecutive repeated characters with the character 
followed by its count.

For example:

AAABBCCCCD → A3B2C4D1

As a software developer, your task is to write a recursive Python program to compress a given string.

Task

Write a recursive function that compresses a string by counting consecutive occurrences of each 
character.

Input
Enter a String:
AAABBCCCCD
Output
Compressed String = A3B2C4D1
Sample Input 2
Enter a String:
WWWWXXYYZ
Sample Output 2
Compressed String = W4X2Y2Z1
Sample Input 3
Enter a String:
AAAAA
Sample Output 3
Compressed String = A5
'''

def compress(s):
    if len(s) == 0:
        return ""
    else:
        count = 1
        while len(s) > 1 and s[0] == s[1]:
            count += 1
            s = s[1:]
        return s[0] + str(count) + compress(s[1:])
def main():
    s = input("Enter a String: ")
    string = compress(s)
    print("Compressed String =", string)
main()