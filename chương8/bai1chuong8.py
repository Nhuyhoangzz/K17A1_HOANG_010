#tìm số lớn nhất-số nhỏ nhất
a=float(input("nhập a:"))
b=float(input("nhập b"))
c=float(input("nhập c:"))
d=float(input("nhập d:"))
max = a
min = a
if b > max:
    max = b
if b < min:
    min = b
if c > max:
    max = c
if c < min:
    min = c
if d > max:
    max = d
if d < min:
    min = d
print("Số lớn nhất là:", max)
print("Số nhỏ nhất là:", min)