'''1. 3 marks
 Check if Two Strings Differ by Exactly One Character**

A typing tutor application compares a student's typed word with the expected word.
The application should determine whether the typed word differs from the expected word by exactly one character.
 A difference can occur in one of the following ways:

* One character is inserted
* One character is deleted
* One character is replaced

Write a Python program to check whether two given strings differ by exactly one character. If they do, display **True**; otherwise, display **False**.

**Input Format:**

* The first line contains the first string `S1`.
* The second line contains the second string `S2`.

**Output Format:**

* Print `True` if the two strings differ by exactly one character.
* Otherwise, print `False`.

**Constraints:**

* The strings contain only lowercase English alphabets.
* `1 ≤ length of string ≤ 100`

**Sample Input 1:**
pale
ple

**Sample Output 1:**
True

**Explanation:**
The strings `"pale"` and `"ple"` differ by exactly one character because removing `'a'` from `"pale"` results in `"ple"`.

**Sample Input 2:**
pale
bale

**Sample Output 2:**
True

**Explanation:**
The strings differ by exactly one character because `'p'` in `"pale"` is replaced by `'b'` in `"bale"`.

**Sample Input 3:**
pale
pales

**Sample Output 3:**
True

**Explanation:**
The strings differ by exactly one character because `'s'` is inserted at the end of `"pale"`.

**Sample Input 4:**
pale
pale

**Sample Output 4:**
False

**Explanation:**
The strings are identical and do not differ by any character.

**Sample Input 5:**
pale
bake

**Sample Output 5:**
False

**Explanation:**
More than one character change is required to convert `"pale"` into `"bake"`.'''

s1 = input("Enter String 1 = ")
s2 = input("Enter String 2 = ")

l1 = len(s1)
l2 = len(s2)

if (l1-l2) > 1:
    print(False)
else:
    i = 0
    j = 0
    diff = 0

    while i < l1 and j < l2:
        if s1[i]!= s2[j]:
            diff+=1
            if diff > 1:
                break
            if l1 > l2:
                i+=1
            elif l2 > l1:
                j+=1
            else:
                i+=1
                j+=1
        else:
            i+=1
            j+=1
    diff += (l1-i) + (l2-j)
print(diff == 1)    






