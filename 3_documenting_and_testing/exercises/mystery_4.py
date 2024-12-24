def mystery_4(a):
    b = []

    c = 0
    while len(b) < a:
        b.append(c)
        c = c + 1

    return b
""" exapmle:
a=3
the process:
-3>0 true
- we add c which is 0 to b
-b=[0]
Now c =1 
-3>1? true 
-we add c which is 1 to b
-b=[0,1]
Now c =2
-3>2? true 
-we add c which is 2 to b
-b=[0,1,2]
Now c =3
-3>3? False
THEN we get out of the while loop AND return b 
the OUTPUT b = [0,1,2]
"""

