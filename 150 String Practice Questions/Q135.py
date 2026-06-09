'''
135Check if two strings differ by exactly one character. S1 = "pale", S2 = "ple" False (differs by insertion/deletion)

'''

s1 = "pale"
s2 = "bale"
diff = 0
if len(s1) == len(s2):
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff += 1
    print("Differ by exactly one char:", diff == 1)
else:
    print("Differ by exactly one char: False")