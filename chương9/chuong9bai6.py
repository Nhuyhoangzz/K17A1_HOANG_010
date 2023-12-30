def kiem_tra_so_nguyen_to(x):
    if x <= 1:
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True
so_can_kiem_tra = 17 
ket_qua = kiem_tra_so_nguyen_to(so_can_kiem_tra)
if ket_qua:
    print(f"{so_can_kiem_tra} là số nguyên tố")
else:
    print(f"{so_can_kiem_tra} không là số nguyên tố")

    