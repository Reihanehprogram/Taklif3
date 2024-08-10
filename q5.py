a = input("amaliat mored nazar ra benevisid\n")
b = a[-1] 
c = a[0]
d = a[1]
if d == " ":
    d = a[2]
else:
    pass

if d == "+":
    f = int(b)+int(c)
if d == "-":
    f = int(b)-int(c)
if d == "*":
    f = int(b)*int(c)
if d == "/":
    f = int(b)/int(c)
print(f)
