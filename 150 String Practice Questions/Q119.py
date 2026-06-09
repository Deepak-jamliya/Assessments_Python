'''
119Find the smallest substring containing all vowels. 
S = "aeiouy" 
"aeiou"

'''
s = "aeiouy"
n = len(s)

for i in range(n):
    a = e = i = o = u = False

    for j in range(i, n):
        ch = s[j]

        if ch == 'a':
            a = True
        elif ch == 'e':
            e = True
        elif ch == 'i':
            i = True
        elif ch == 'o':
            o = True
        elif ch == 'u':
            u = True

        if a and e and i and o and u:
            print(s[i:j+1])
            quit()