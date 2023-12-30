def kiem_tra(day,month,year):
    if year < 1:
        return False
    if month < 1 or month > 12:
        return False
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day<1 or day>31:
            return False
    elif month in [4, 6, 9, 11]:
        if day<1 or day>30:
            return False
    else:
        if year%4==0 and (year%100!=0 or year%400 == 0):
            if day<1 or day> 29:
                return False
        else:
            if day<1 or day> 28:
                return False
    return True
def xuat_ngay_dinh_dang(day,month,year):
    return f"{day:02d}-{month:02d}-{year}"
def nam_nhuan(year):
    if (year%4==0 and year%100!= 0) or (year%400==0):
        return True
    else:
        return False
def thu_trong_tuan(day,month,year):
    # Tính thứ của ngày/tháng/năm nhập vào
    import datetime
    ngay= datetime.datetime(year,month,day).weekday() + 1
    return ngay
def so_ngay_trong_thang(month,year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        if year%4==0 and (year%100!=0 or year%400==0):
            return 29
        else:
            return 28
#nhập dl
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))
if kiem_tra(ngay, thang, nam):
    print("Ngày tháng năm vừa nhập:", xuat_ngay_dinh_dang(ngay, thang, nam))
    if nam_nhuan(nam):
        print("Năm nhuận.",nam)
    else:
        print(f"Năm {nam} không là năm nhuận")
    print(xuat_ngay_dinh_dang(ngay, thang, nam),"là thứ",thu_trong_tuan(ngay,thang,nam))
    print("số ngày trong tháng là:",so_ngay_trong_thang(thang,nam))
else:
    print("Ngày tháng năm không hợp lệ")
