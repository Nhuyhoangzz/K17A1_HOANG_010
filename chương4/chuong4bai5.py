def ucln(a, b):
    while b:
        a, b = b, a % b
    return a
def bcnn(a, b):
    return abs(a * b) // ucln(a, b)
so1 = int(input("Nhập số thứ nhất: "))
so2 = int(input("Nhập số thứ hai: "))
result = bcnn(so1, so2)
print(f"BCNN của {so1} và {so2} là: {result}")






