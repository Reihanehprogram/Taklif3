a = (input("bede radif 1 ro "))
b = (input("bede radif 2 ro "))
c = 0

indices = [0, 2, 4, 6, 8, 10, 12, 14]
for i in indices:
    if a[i] == b[i] and a[i] == "1":
        c += 1
print (c)