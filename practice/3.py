n=int(input())
items=dict()

for i in range(n):

    a = list(input().split())

    x = a[0]

    y = int(a[1])

    for j in range(2,len(a)):

        items[a[j]] = x

m=int(input())
list1=[]

for i in range(m):

    s=input()
    k=True

    for key in items.keys():

        if key==s:
            
            print(items[key])

            k=False
            
    if k:
        print("Unknown")