'''
134Convert an integer to Roman numeral string. N = 14 "XIV"

'''

n = 14
val =  [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
result = ""
for i in range(len(val)):
    while n >= val[i]:
        result += syms[i]
        n -= val[i]
print("Roman:", result)