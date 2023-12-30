def kiem_tra_so_hoan_hao(num):
    if num <= 0:
        return False
    tong_uoc = 0
    for i in range(1, num):
        if num % i == 0:
            tong_uoc += i
    return tong_uoc == num
so_can_kiem_tra = 28  
if kiem_tra_so_hoan_hao(so_can_kiem_tra):
    print(f"{so_can_kiem_tra} là số hoàn hảo")
else:
    print(f"{so_can_kiem_tra} không là số hoàn hảo")
