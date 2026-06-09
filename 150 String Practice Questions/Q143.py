'''
143Check if a string is valid JSON format (basic check). S = '{\text{"key"}: \text{"value"}}' TRUE

'''

s = '{"key": "value"}'
s = s.strip()
valid = False
if (s.startswith("{") and s.endswith("}")) or \
   (s.startswith("[") and s.endswith("]")):
    valid = True
print("Valid JSON (basic):", valid)