def tinh_can(nam):
    can = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
    chi = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]
    can_index = nam % 10
    chi_index = nam % 12
    nam_amlich = f"{can[can_index]} {chi[chi_index]}"
    return nam_amlich
nam = int(input("Nhập năm dương lịch: "))
# Gọi hàm và in kết quả
nam_amlich = tinh_can(nam)
print(f"Năm {nam} là năm {nam_amlich} trong năm âm lịch.")