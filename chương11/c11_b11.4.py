list=[]
while True:
 i=int(input("tiếp tục nhập giá trị ? 1: Có, 0: không:"))
 if i==1:
    a=int(input('nhập giá trị muốn them danh sách:'))
    list.append(a)
 elif i==0:
    break
print('danh sách bạn vừa nhập là:',list)
num_list = [10,5,-2,23,5,6,7] 
 # Nhập số x
x = int(input("Nhập số giá trị: "))
 # Tính tổng các phần tử trong list
total_sum = sum(num_list)
print("Tổng các giá trị trong list:", total_sum)
 # Kiểm tra x có xuất hiện trong list không và xuất hiện bao nhiêu lần
count_x = num_list.count(x)
if count_x > 0:
    print(f"{x} xuất hiện trong list {count_x} lần.")
else:
    print(f"{x} không xuất hiện trong list.")
 # Kiểm tra x có lớn hơn tất cả các số trong list không
if x > max(num_list):
    print(f"{x} lớn hơn tất cả các số trong list.")
else:
    greater_than_x = [num for num in num_list if num > x]
    if len(greater_than_x) > 0:
        print(f"{x} nhỏ hơn những số sau trong list:", greater_than_x)
    else:
        print(f"{x} không nhỏ hơn bất kỳ số nào trong list.")

list = []

while True:
 i = int(input('Tiếp tục nhập giá trị không ? 1:Có, 2: không :   '))
 if i==1:
     a = int(input('Nhập giá trị bạn muốn thêm vào danh sách: '))
     list.append(a)
 elif i ==0:
    break
print("List bạn vừa nhập là : ",list)
# tìm giá trị x trong list
x = int(input('NHập X đi iem yêu :'))
find = x in list
if find:
   print(x,'Có lặp trong dãy List ,số lần lặp của x là :',list.count(x))
else:
   print(x,'không xuất hiện trong dãy List')

# tìm coi phải max không
list1 =[]
if x == max(list):
   print(x,'Là number lớn nhất in List bạn vừa nhập')
else:
   for i in list:
      if i >x:
         list1.append(i)
print('danh sách các số lớn hơn ',x,'là',list1)
    
   
print('tổng các number trong list là :', sum(list))