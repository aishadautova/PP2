nums = list(map(int, input().split()))

res = ""

for x in nums:
    if x > 0:
        res += str(x)
        res += " "

for x in nums:
    if x == 0:
        res += str(x)
        res += " "
 
print(res)
