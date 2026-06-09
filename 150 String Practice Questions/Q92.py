'''
92Check if two strings are pq-balanced. 
S1 = "pqqp", S2 = "qpqp" 
Example dependent on specific "pq-balanced" definition

'''

s1 = input("Enter S1 = ")
s2 = input("Enter S2 = ")

if s1.count('p') == s1.count('q') and s2.count('p') == s2.count('q'):
    print("PQ-BALANCED")
else:
    print("NOT PQ-BALANCED")