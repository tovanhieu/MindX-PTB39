# Khởi tạo mảng danh sách name 
name = ["Đan","Thắng","Hòa","Vân"]
length = len(name)
print("Độ dài của mảng name là:",length)
# In các phần tử trong mảng name theo thứ tự từ đầu đến cuối với chỉ số index i
for i in range(len(name)):
    print(f"Tên bạn ở vị trí số {i+1} trong dánh sách name là {name[i]}")
# In các phần tử trong mảng name theo thứ tự từ đầu đến cuối
for i in name:
    print(i)

age = [12,10,7,21,5]
count = 0
for i in age:
    if i > 10:
        count += 1
print("Tổng số phần tử trong mảng age có số tuổi lớn hơn 10 là:",count)

for i in range(len(age)):
    if age[i] > 10:
        count += 1
print("Tổng số phần tử trong mảng age có số tuổi lớn hơn 10 là:",count)

# Thêm một phần tử vào cuối mảng trong danh sách name sử dụng hàm append()
print("Mảng name ban đầu:",name)
name.append("Tuấn")
print("Mảng name sau khi thêm phần tử Tuấn vào cuối mảng:",name)
name.append("Đan")
print("Mảng name sau khi thêm phần tử Đan vào cuối mảng:",name)
# Thêm một phần tử vào cuối mảng trong danh sách age sử dụng hàm append()
print("Mảng age ban đầu:",age)
age.append(7)
print("Mảng age sau khi thêm phần tử  vào cuối mảng:",age)

# Thêm một phần tử vào mảng trong danh sách theo một vị trí cố định age sử dụng hàm insert()
print("Mảng name ban đầu:",name)
name.insert(1,"Huy")
print("Mảng name sau khi thêm phần tử Huy vào vị trí số 1 trong mảng:",name)
name.insert(3,"Lan")
print("Mảng name sau khi thêm phần tử Lan vào vị trí số 3 trong mảng:",name)

# Bài tập 1
# numbers= []
# num = int(input("Nhập số nguyên (nhập -1 thì kết thúc):"))
# while num != -1:
#     numbers.append(num)
#     num = int(input("Nhập số nguyên (nhập -1 thì kết thúc):"))
# print(f"Mảng numbers sau khi nhập là: {numbers}")

# Ví dụ về hàm remove()
print("Mảng name ban đầu:",name)
name.remove("Đan")
print("Mảng name sau khi xóa phần tử Đan trong mảng:",name)
name.remove("Thắng")
print("Mảng name sau khi xóa phần tử Thắng trong mảng:",name)
# Ví dụ về hàm pop()
print("Mảng name ban đầu:",name)
name.pop()
print("Mảng name sau khi xóa phần tử cuối cùng trong mảng:",name)
name.pop(2)
print("Mảng name sau khi xóa phần tử ở vị trí số 2 trong mảng:",name)
# Ví dụ về hàm clear()
print("Mảng name ban đầu:",name)
name.clear()
print("Mảng name sau khi xóa tất cả phần tử trong mảng:",name)
# Ví dụ về cập nhật giá trị trong mảng
# print("Mảng name ban đầu:",name)
# name[2] = "Hậu"
# print("Mảng name sau khi cập nhật phần tử  ở vị trí số 1 trong mảng:",name)
# Ví dụ về hàm sort() sáwp xếp mảng theo thứ tự tăng dần
print("Mảng age ban đầu:",age)
age.sort()
print("Mảng age sau khi sắp xếp theo thứ tự tăng dần:",age)
# Ví dụ về hàm sort() sáwp xếp mảng theo thứ tự giảm dần
print("Mảng age ban đầu:",age)  
age.sort(reverse=True)
print("Mảng age sau khi sắp xếp theo thứ tự giảm dần:",age)

# Bài tập 2
product_list = ["Quần", "Áo", "Rau, củ", "Thịt", "Cá", "Gạo"]
shopping_cart = []

while True:
    print("==========SHOPPING CART==========")
    print("1. Xem danh sách sản phẩm")
    print("2. Xem giỏ hàng")
    print("3. Thêm sản phẩm vào giỏ hàng")
    print("4. Xóa sản phẩm khỏi giỏ hàng")
    print("5. Thoát")
    choice = input("Nhập lựa chọn của bạn (1-5): ")
    if choice == "1":
        print("=========MENU========")
        for index, item in enumerate(product_list):
            print(f"{index + 1}. {item}")
        print("====================")
    elif choice == "2":
        if not shopping_cart:
            print("Giỏ hàng của bạn đang trống.")
        else:
            print("Các mặt hàng trong giỏ hàng của bạn:")
            for index, item in enumerate(shopping_cart):
                print(f"{index + 1}. {item}")
    elif choice == "3":
        print("Danh sách sản phẩm:")
        for index, item in enumerate(product_list):
            print(f"{index + 1}. {item}")
        item_index = int(input("Nhập chỉ mục của sản phẩm bạn muốn thêm vào giỏ hàng: ")) - 1
        if item_index >= 0 and item_index < len(product_list):
            selected_item = product_list[item_index]
            shopping_cart.append(selected_item)
            print(f"{selected_item} đã được thêm vào giỏ hàng của bạn.")
        else:
            print("Chỉ mục sản phẩm không hợp lệ.")
    elif choice == "4":
        if not shopping_cart:
            print("Giỏ hàng của bạn đang trống.")
        else:
            print("Các mặt hàng trong giỏ hàng của bạn:")
            for index, item in enumerate(shopping_cart):
                print(f"{index + 1}. {item}")
            item_index = int(input("Nhập chỉ mục của sản phẩm bạn muốn xóa khỏi giỏ hàng: ")) - 1
            if item_index >= 0 and item_index < len(shopping_cart):
                deleted_item = shopping_cart.pop(item_index)
                print(f"{deleted_item} đã được xóa khỏi giỏ hàng của bạn.")
            else:
                print("Chỉ mục sản phẩm không hợp lệ.")
    elif choice == "5":
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
