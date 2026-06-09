'''
104Check if a string contains balanced brackets of all types ((), {}, []). 
S = "{[()]}" 
TRUE

'''

s = input("Enter string = ")

prev = ""

while s != prev:
    prev = s
    s = s.replace("()", "")
    s = s.replace("{}", "")
    s = s.replace("[]", "")

if s == "":
    print("TRUE")
else:
    print("FALSE")