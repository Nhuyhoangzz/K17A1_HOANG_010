#giải hpt bậc nhất
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
if a == 0:
    print("Hệ phương trình không phải là hệ phương trình bậc nhất.")
else:
    x = -b / a
    print(f"Nghiệm của hệ phương trình là x = {x}")

#tính số ngày của 1 tháng một năm nào đó
nam = int(input("Nhập năm: "))
# Kiểm tra năm nhuận
if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    thang_2_ngay = 29
else:
    thang_2_ngay = 28
# Định nghĩa số ngày của các tháng
so_ngay_cac_thang = [31, thang_2_ngay, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# Tính tổng số ngày của 12 tháng
tong_so_ngay = sum(so_ngay_cac_thang)
print(f"Số ngày của 1 tháng 1 năm {nam} là {tong_so_ngay}")

#tim UCLN
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
if a < b:
    a, b = b, a
while b != 0:
    r = a % b
    a, b = b, r
print(f"UCLN của {a} và {b} là {a}")

