def kiem_tra_zip_code(chuoi):
    if len(chuoi) == 6 and chuoi.isdigit():
        return True
    else:
        return False
chuoi_kiem_tra = "156"
ket_qua = kiem_tra_zip_code(chuoi_kiem_tra)
if ket_qua:
    print(f"{chuoi_kiem_tra} là mã ZIP code hợp lệ của Việt Nam")
else:
    print(f"{chuoi_kiem_tra} không phải là mã ZIP code hợp lệ của Việt Nam")

