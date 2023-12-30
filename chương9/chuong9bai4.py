def tinh_S(n,x):
    S=(x**2+1)**n
    return S
x=int(input("nhập số x:"))
n=int(input("nhập số n:"))
print(tinh_S(n,x))