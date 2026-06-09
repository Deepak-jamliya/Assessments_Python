'''
93Match strings with wildcard characters ($\*$, ?). 
Pattern = "a?c", Text = "axcde" 
TRUE
'''

pattern = input("Enter pattern = ")
text = input("Enter text = ")

ok = True

for i in range(len(pattern)):
    if pattern[i] == '*':
        break
    elif pattern[i] == '?' or pattern[i] == text[i]:
        continue
    else:
        ok = False
        break

print("TRUE" if ok else "FALSE")