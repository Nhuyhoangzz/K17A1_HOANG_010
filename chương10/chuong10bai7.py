def chuoi_s(s, s_sub, s_find, s_replace):
    # Loại bỏ khoảng trắng ở đầu và cuối chuỗi
    s = s.strip()
    print("Chuỗi sau khi loại bỏ khoảng trắng đầu cuối:", s)
    # Đếm số lần 
    c=s.count(s_sub)
    print("Số lần s_sub xuất hiện trong s:", c)
    # Tìm kiếm
    s=s.replace(s_find, s_replace)
    #đầu chuỗi viết hoa
    s = s.capitalize()
    print("Chuỗi s sau khi thay thế:", s)
s = input("Nhập chuỗi s: ")
s_sub = input("Nhập chuỗi s_sub: ")
s_find = input("Nhập chuỗi s_find: ")
s_replace = input("Nhập chuỗi s_replace: ")
chuoi_s(s, s_sub, s_find, s_replace)
