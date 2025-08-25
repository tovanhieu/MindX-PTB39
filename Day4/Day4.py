#Bắt đầu
# a = input("Nhập vào giá trị của a: ")
# b = input("Nhập vào giá trị của b: ")
# if a == b:
#     print("a và b bằng nhau")
# else:
#     print("a và b không bằng nhau")

# Kiểm tra số chăn lẻ 
# n = int(input("Nhập vào một số nguyên: "))  
# if n % 2 == 0:
#     print("n là số chẵn")
# else:
#     print("n là số lẻ")
# Kiểm tra một số có chia hết cho 2 và 3 hay không
# n = int(input("Nhập vào một số nguyên: "))
# if n % 2 == 0:
#     print("n chia hết cho 2")
# elif n % 3 == 0:
#     print("n chia hết cho 3")
# else:
#     print("n không chia hết cho 2 và 3")

# An = float(input("Nhập vào giá trị chiều cao của An (đơn vị là mét): "))
# Minh = float(input("Nhập vào giá trị chiều cao của Minh (đơn vị là mét): "))
# Lan = float(input("Nhập vào giá trị chiều cao của Làn (đơn vị là mét): "))

# if An >= Minh and An >= Lan:
#     cao_nhat = An
#     nguoi_cao_nhat = "An"
# elif Minh >= An and Minh >= Lan:
#     cao_nhat = Minh
#     nguoi_cao_nhat = "Minh"
# else:
#     cao_nhat = Lan
#     nguoi_cao_nhat = "Lan"
# print(f"Người cao nhất là {nguoi_cao_nhat} với chiều cao {cao_nhat} mét.")


#nhập số kWh tiêu thụ
kwh = int(input("nhập số kwh:"))
if kwh <= 50:
    tien = kwh * 1700
elif kwh <= 100:
    tien = 50 * 1700 + (kwh - 50) * 1900
elif kwh <= 200:
    tien = 50 * 1700 + 50 * 1900 + (kwh - 100) * 2100
else:
    tien = 50 * 1700 + 50 * 1900 + 100 * 2100 + (kwh - 200) * 3000

# In kết quả
print("Số tiền điện cần phải trả:", f"{tien:,}", "đồng")


