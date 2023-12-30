def tinh_bieu_thuc(x,n):
    S=(x**2+1)**n
    return S
n=int(input("nhập n:"))
x=float(input("nhập x:"))
S = tinh_bieu_thuc(x, n)

print(f"Kết quả của biểu thức là {S}")