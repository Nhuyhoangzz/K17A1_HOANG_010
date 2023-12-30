from numbers import Number
def tinh_S(x,n):
    S=(pow(x,2)+1)*n
    return S
a=float(input("nhập x:"))
b=float(input("nhập n:"))
print("biểu thức có giá trị là:",tinh_S(a,b))