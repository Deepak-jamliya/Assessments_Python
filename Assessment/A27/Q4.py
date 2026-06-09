'''
# 4. Cloud Storage Duplicate File Name Resolver

A cloud storage company stores uploaded filenames from users.

Sometimes multiple duplicate filenames are uploaded.

The system should:

* Keep the first occurrence unchanged
* Add (1), (2), (3)... for duplicates

### Input:

text
file file image file image data


### Output:

text
file file(1) image file(2) image(1) data
'''

str = input("Enter String = ")
words = str.split()

new = ""
i = 0
while i < len(str):
    count = 0
    if words[i] not in new:
        new = new + " " + words[i]
    else:
