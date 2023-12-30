#loại phòng
#standard:1.260.000
#superior garden view:1.550.000
#superior ocean view:1.830.000
#garden view bungalow:1.830.000
#pool view bungalow:2.120.000
#family room:2.120.000
#beach front bungalow:2.540.000
#vip sea view:4.800.000


#input so_phong, so_dem
#output so_tien
phong1 = float(1260000) 
phong2 = float(1550000)
phong3 = float(1830000) 
phong4 = float(1830000)
phong5 = float(2120000) 
phong6 = float(2120000)
phong7 = float(2540000) 
phong8 = float(4800000)
def tinh_tien_phong(so_phong, so_dem): 
    if(so_phong == 1) :
        tien_phong_1_dem = phong1
    elif(so_phong == 2):
        tien_phong_1_dem = phong2
    elif(so_phong == 3):
        tien_phong_1_dem = phong3
    elif(so_phong == 4):
        tien_phong_1_dem = phong4
    elif(so_phong == 5):
        tien_phong_1_dem = phong5
    elif(so_phong == 6):
        tien_phong_1_dem = phong6
    elif(so_phong == 7):
        tien_phong_1_dem = phong7
    elif(so_phong == 8):
        tien_phong_1_dem = phong8    

    if (so_dem == 1):
        so_tien = tien_phong_1_dem * 1
    elif (so_dem >= 2 and so_dem <= 3):
        so_tien = tien_phong_1_dem * so_dem * 0.75
    else:
        so_tien = tien_phong_1_dem * so_dem * 0.7
    return so_tien

so_phong=float(input("nhập loại phòng:"))
so_dem=float(input("nhập số đêm:"))
tong_so_tien = tinh_tien_phong(so_phong, so_dem)
print(f"thành tiền:{tong_so_tien} vnđ")
