#list number 3
lists=(74,74,72,72,73,69,69,71,76,71)
#đổi inch sang mét:
def inch_to_meter_list(inches_list):
    meters_list = [inch * 0.0254 for inch in inches_list] 
     # Chuyển đổi từng phần tử từ inch sang mét
    return meters_list
# Đổi từ inch sang mét cho danh sách
meters_list = inch_to_meter_list(lists)

print("Danh sách sau khi đổi từ inch sang mét:")
print(meters_list)

#in ra 3 chiều cao đầu tiên
print("Ba chiều cao đầu tiên là:")
for i in range(3):
    print(lists[i])
#3 chiều cao cuối cùng
chiều_cao_cuối = lists[-3:]
print("Ba chiều cao cuối cùng là:")
for lists in chiều_cao_cuối:
    print(lists)
#sắp xếp list theo thứ tự tăng,giảm dần
lists.sort()
print('list theo thứ tự tăng dần là:',lists)
lists.reverse()
print('list theo thứ tự giảm dần là:',lists)