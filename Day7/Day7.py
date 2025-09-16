# # In ra màn hình các số từ 1-5
# i = 1
# while i < 6:
#     print(i)
#     i += 1

# # Kiểm tra mật khẩu password nhập vào từ người dùng
# user_password = "123456"
# input_password = input("Nhập vào mật khẩu: ")
# while input_password != user_password:
#     print("Mật khẩu không đúng, vui lòng nhập lại.")
#     input_password = input("Nhập vào mật khẩu: ")
#     print("Đăng nhập thành công!")
# # Nhập và in ra giá trị của một số nguyên dương n từ n -> 100
# n = int(input("Nhập vào một số nguyên dương n (n < 100): "))
# while n < 101:
#     if n == -1:
#         break
#     print(n)
#     n += 1

# # Nhập và in ra giá trị của một số nguyên dương n từ n -> 100 trừ số 90
# n = int(input("Nhập vào một số nguyên dương n (n < 100): "))
# while n < 101:
#     if n == -1:
#         break
#     if n == 90:
#         n += 1
#         continue
#     print(n)
#     n += 1


# Cách 1
# n = int(input("Nhập vào một số nguyên dương n: "))
# sum = 0
# for i in range(1, n):
#     sum += i
#     print(i, end = " ") 
#     if sum > n:
#         break  

# # Cách 2
# n = int(input("Nhập vào một số nguyên dương n: "))
# sum = 0
# i = 1
# while sum <= n:
#     sum += i
#     print(i, end = " ")
#     i += 1      
# a = int(input("Nhập vào một số nguyên dương a: "))
# b = int(input("Nhập vào một số nguyên dương b: "))
# for i in range(1, (a*b)+1):
#     if i % a == 0 and i % b == 0:
#         print(f"Bội chung nhỏ nhất của {a} và {b} là: {i}")
#         x  = int(i/b)
#         y = int(i/a)
#         print(f"Tối giản phân số {a}/{b} là: {x}/{y}")
#         break



# Bài tập về nhà số 1:
# Cách 1 dùng while
# n = int(input("Nhập vào một số nguyên dương n: "))
# sum = 0
# i = 1
# while sum <= n:
#     sum = sum + i
#     print(i, end = " ")
#     i += 1
# # Cách 2 dùng for
# n = int(input("Nhập vào một số nguyên dương n: "))
# sum = 0
# for i in range(1, n):
#     sum = sum + i
#     print(i, end = " ")
#     if sum > n:
#         break

# Bài tập về nhà số 2:
password = "123456"
input_password = input("Nhập vào mật khẩu: ")
while input_password != password:
    print("Mật khẩu không chính xác, vui lòng nhập lại.")
    input_password = input("Nhập vào mật khẩu: ")
print("Đăng nhập thành công!")