n=int(input())
s1=set()
s2=set()

for i in range(n):
    x=input()
    
    if i==0:
        for j in x:
            s2.add(j)
    
    for j in x:
        s1.add(j)
    s2=s2.intersection(s1)
    s1.clear()

if len(s2)==0:
    print("NO COMMON CHARACTERS")
else:
    print(*sorted(s2,key=str))