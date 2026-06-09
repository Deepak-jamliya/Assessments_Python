'''
44Check if two strings are anagrams. 
S1 = "listen", S2 = "silent" 
TRUE
'''

s1 = input("Enter String = ")
s2 = input("Enter Second String = ")

if  len(s1) != len(s2):
    print("Not Anagram")

else:
    flag = 1
    check = ""
    i = 0
    while i < len(s1):
        ch = s1[i]
        if ch not in check:
            c1 = 0
            c2 = 0
            j = 0
            while j < len(s1):
                if s1[j] == ch:
                    c1 +=1
                j+=1
            j = 0
            while j < len(s2):
                if s2[j] == ch:
                    c2+=1
                j+=1
            if c1 != c2:
                flag = 0
                break
        check+=ch
        i+=1
if flag:
    print("Anagram")
else:
    print("Not Anagram")
