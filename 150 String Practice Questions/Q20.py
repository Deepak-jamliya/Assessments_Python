'''
Find the lowest frequency character. 
S = "aabbcde" 
c', 'd', 'e' (any one or all)
'''


str = input("Enter string = ")

smallest = len(str)
answer = ""

for i in str:
    count = 0
    for ch in str:
        if ch == i:
            count+=1
    if count < smallest:
        smallest = count
        answer = i
print(answer)