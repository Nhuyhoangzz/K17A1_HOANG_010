#elementwise_greater_than
def elementwise_greater_than(L, thresh):
    # Tạo danh sách kết quả ban đầu là danh sách rỗng
    result = []
    # Duyệt qua từng phần tử trong danh sách L
    for element in L:
        # So sánh phần tử với ngưỡng thresh và thêm kết quả vào danh sách kết quả
        result.append(element > thresh)
    return result
# Danh sách ban đầu
L= [1,2,3,4]
# Ngưỡng thresh
thresh = 2
# Gọi phương thức và lưu kết quả vào biến result_list
result_list = elementwise_greater_than(L, thresh)
print(result_list)
