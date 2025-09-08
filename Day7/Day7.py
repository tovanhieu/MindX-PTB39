# In ra màn hình các số từ 1-5
i = 1
while i < 6:
    print(i)
    i += 1

# Kiểm tra mật khẩu password nhập vào từ người dùng
user_password = "123456"
input_password = input("Nhập vào mật khẩu: ")
while input_password != user_password:
    print("Mật khẩu không đúng, vui lòng nhập lại.")
    input_password = input("Nhập vào mật khẩu: ")
    print("Đăng nhập thành công!")
# Nhập và in ra giá trị của một số nguyên dương n từ n -> 100
n = int(input("Nhập vào một số nguyên dương n (n < 100): "))
while n < 101:
    if n == -1:
        break
    print(n)
    n += 1

# Nhập và in ra giá trị của một số nguyên dương n từ n -> 100 trừ số 90
n = int(input("Nhập vào một số nguyên dương n (n < 100): "))
while n < 101:
    if n == -1:
        break
    if n == 90:
        n += 1
        continue
    print(n)
    n += 1
