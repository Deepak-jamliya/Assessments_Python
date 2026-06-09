'''
120Find the longest substring containing only vowels.
 S = "abaeiouy" 
 "aeiou"

'''


s = "abaeiouy"
longest = curr = ""

for ch in s:
    if ch in "aeiou":
        curr += ch
        if len(curr) > len(longest):
            longest = curr
    else:
        curr = ""

print(longest)