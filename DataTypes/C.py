k = int(input())

h = k // 3600

m = (k - h * 3600) // 60

print("It is", h, "hours", m, "minutes.")