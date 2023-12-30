def tinh_bieu_thuc(x,n):
    A=(x*x+x+1)**n + (x*x-x+1)**n
    return A
n=int(input("nhập n:"))
x=float(input("nhập x:"))
A=tinh_bieu_thuc(x,n)
print(f"kết quả của biểu thức là {A}")