'''
70Compare the number of times 'the' and 'is' appear. 
S = "the cat is on the mat" 
the: 2, is: 1 (theis)
'''

s = input("Enter Input = ")
words = s.split()

tcount = 0
icount = 0
for i in words:
    if i == "the":
        tcount+=1
    elif i == "is":
        icount+=1

print("the : ",tcount,"is : ",icount)