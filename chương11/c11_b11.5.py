list=[1,-3,2,8,-4,7]
while True:
 i=int(input("tiếp tục nhập giá trị ? 1: Có, 0: không:"))
 if i==1:
    a=int(input('Nhập giá trị:'))
    list.append(a)
 elif i==0:
    break
print('Danh sách bạn vừa nhập là:',list)
#các số nguyên tố trong list
def songuyento(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
# Xuất ra các số nguyên tố từ list
snt = [num for num in list if songuyento(num)]
print("Các số nguyên tố trong list là:",snt)
#trung bình cộng âm dương trong list
def trungbinhcong(lst):
    duong = [num for num in lst if num > 0]
    am = [num for num in lst if num < 0]
    tbcd = sum(duong) / len(duong) if duong else 0
    tbca = sum(am) / len(am) if am else 0
    return duong,am
# Tính trung bình cộng các số dương và số âm trong list
soduong,soam= trungbinhcong(list)
print("Trung bình cộng các số dương là:",soduong)
print("Trung bình cộng các số âm là:",soam)
#max/min trong list
print('giá trị max trong list là:',(max(list)))
print('giá trị min trong list là:',(min(list)))
#list tăng dần
list.sort()
print(list)
