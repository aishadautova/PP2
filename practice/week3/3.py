num = input()
num = num.split(" ")

list1 = list(num)

list1.reverse()
res = ""
for x in list1:
    res += x
    res += " "

print(res) 