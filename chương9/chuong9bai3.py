#tinh bmi
def tinh_bmi(w,h):
    chieu_cao=h/100
    bmi=w/(chieu_cao**2)
    return bmi
w=float(input("nhập chiều cao của bạn(m):"))
h=float(input("nhập cân nặng của bạn(kg):"))
bmi = tinh_bmi(w,h)
print(f"Chỉ số BMI của bạn là: {bmi:.2f}")