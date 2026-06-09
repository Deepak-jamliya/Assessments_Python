'''
116Check if a string is a valid shuffle of two other strings. 
S1 = "xy", S2 = "12", S3 = "x1y2" 
TRUE

'''

s1 = input("Enter S1 = ")
s2 = input("Enter S2 = ")
s3 = input("Enter S3 = ")

i = j = 0

if len(s1) + len(s2) != len(s3):
    print("FALSE")
else:
    for ch in s3:
        if i < len(s1) and ch == s1[i]:
            i += 1
        elif j < len(s2) and ch == s2[j]:
            j += 1
        else:
            print("FALSE")
            break
    else:
        print("TRUE")