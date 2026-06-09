'''
64Count frequency of each vowel. 
S = "programming" 
o: 1, a: 1 (e, i, u: 0)
'''

s = input("Enter String = ")

check = ""
for i in s:
    if i in 'aeiou' and i not in check:
        count = 0
        for ch in s:
            if ch == i:
                count+=1
        print(i, " : ",count)
        check+=i