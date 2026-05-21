'''
2. Reverse Sentence + Reverse Each Word

Secret Military Communication Decoder
A defense organization stores highly confidential messages in encrypted form.
To decode the message:

1. Reverse the entire sentence.
2. Reverse every individual word.
3. Store the final result back into the original string variable.

You must use the split() method.
Input:


Python is powerful


Output:


lufrewop si nohtyP
'''

str = input("Enter String = ")

words = str.split()

i = len(words) - 1
while i>=0:
    ch = words[i]
    rev = ""
    j = len(ch) - 1
    while j >= 0:
        rev = rev + ch[j]
        j-=1 
    print(rev, end = " ")
    i-=1