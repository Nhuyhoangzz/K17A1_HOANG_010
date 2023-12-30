dien_tich_hinh_tron = lambda r: 3.14159 * r**2
dien_tich_hinh_chu_nhat = lambda a, b: a * b
chu_vi_hinh_chu_nhat = lambda a, b: 2 * (a + b)
ban_kinh = 5
chieu_dai = 4
chieu_rong = 6
print(f"Diện tích hình tròn có bán kính {ban_kinh}: {dien_tich_hinh_tron(ban_kinh)}")
print(f"Diện tích hình chữ nhật có chiều dài {chieu_dai} và chiều rộng {chieu_rong}: {dien_tich_hinh_chu_nhat(chieu_dai, chieu_rong)}")
print(f"Chu vi hình chữ nhật có chiều dài {chieu_dai} và chiều rộng {chieu_rong}: {chu_vi_hinh_chu_nhat(chieu_dai, chieu_rong)}")
