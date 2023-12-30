#list of animals
list_animals=['ant','bear','cat','dog','elephant','fish','goat','hippo']
print("List of animals:",list_animals)
print("Number of animals:",len(list_animals))
a = str(input("nhập con thú cần tìm: "))
b = list_animals.index(a)
print('con thú bạn cần tìm ở vị trí thứ ',b,'trong chuỗi các con thú')