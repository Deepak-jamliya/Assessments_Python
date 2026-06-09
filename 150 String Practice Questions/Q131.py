'''
131Check if a string is a valid email address. 
S = "test@example.com" 
TRUE
'''

s = "test@example.com"
valid = True
if s.count("@") != 1:
    valid = False
else:
    at_index = s.index("@")
    local = s[:at_index]
    domain = s[at_index+1:]
    if len(local) == 0 or len(domain) == 0:
        valid = False
    elif "." not in domain:
        valid = False
    else:
        dot_index = domain.rindex(".")
        if dot_index == 0 or dot_index == len(domain) - 1:
            valid = False
        for ch in local:
            if not (ch.isalnum() or ch in "._%-+"):
                valid = False
print("Valid email:", valid)