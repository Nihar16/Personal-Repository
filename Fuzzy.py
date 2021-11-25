# fuzzy controller for Washing Machine Problem
# Rule Base
rule_base = {('sd', 'ng'): 'vs', ('sd', 'mg'): 'm', ('sd', 'lg'): 'l', ('md', ' ng'): 's', ('md', 'mg'): 'm',
             ('md', 'lg'): 'l', ('ld', 'ng'): 'm', ('ld', 'mg'): 'l', ('ld', 'lg'): 'vl'}

dirt = int(input("Enter dirt percentage : "))
grease = int(input("Enter grease percentage: "))
# Membership values
dirt_table =['-']*3
if (dirt>= 0 and dirt<=50):
    dirt_table [0] = (50-dirt) /50
    dirt_table [1] = (dirt) /50
elif (dirt>= 50 and dirt<=100):
    dirt_table [1] = (100-dirt)/50
    dirt_table[2] = (dirt - 50) / 50

grease_table = ['-'] * 3
if (grease >= 0 and grease <= 50):
    grease_table[0] = (50 - grease) / 50
    grease_table[1] = (grease) / 50
elif (grease >= 50 and grease <= 100):
    grease_table[1] = (100 - grease) / 50
    grease_table[2] = (grease - 50) / 50

# rule strength table
max_strength = -1
rule_strengthTable = [[-1]*3]*3
for i in dirt_table:
    if (i == '-'):
        continue
    for j in grease_table:
        if (j == '-'):
            continue
    m = min(i,j)
    a = dirt_table.index(i)
    b = grease_table.index(j)
    rule_strengthTable[a][b] = m
    if (max_strength < m):
        max_strength = m
        time_level = (a, b)
# very small
if (time_level == (0, 0) ):
    time = 10 - m * 50
# small
elif (time_level == (1, 0)):
    a = m * 10
    b = 25 - m * 15
    time = max(a, b)
# medium
elif (time_level == (0, 1) or time_level == (1, 1) or time_level == (2, 0)):
    a = m * 15 + 10
    b = 40 - m * 15
    time = max(a, b)

# large
elif(time_level == (0, 2) or time_level == (1, 2) or time_level == (2,1)):
    a = m*15+25
    b = 60-20*m
    time = max(a,b)
#very large
else:
    time = m * 20 + 40

print("Washing Time is", time, "min")
