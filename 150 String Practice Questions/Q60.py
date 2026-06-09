'''
60Append two strings but remove duplicate adjacent characters. 
S1 = "miss", S2 = "issippi" 
"misisipi"

'''
s1 = input("Enter String 1 = ")
s2 = input("Enter String 2 = ")

s3 = s1 + s2

result = ""
prev = ""
for i in s3:
    if i != prev:
        result+=i
        prev = i

print(result)

    