'''
32Count frequency of each word. 
S = "apple banana apple" 
apple: 2, banana: 1
'''

str = input("Enter string = ")

words = str.split()

new = ""
for i in words:
    if i not in new:
        count = 0
        for ch in words:
            if ch == i:
                count+=1
        print(i," : ",count)
        new = new + i
    