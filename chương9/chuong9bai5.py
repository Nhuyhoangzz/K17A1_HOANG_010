def tinh_A(x,n):
    A=(x**2+x+1)**n+(x**2-x+1)**n
    return A
x=float(input("nhập x:"))
n=float(input("nhập n:"))
print(tinh_A(x,n))
