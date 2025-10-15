a = 1
b = 2 
c = 3
sum = a + b + c
print("Sum =", sum)

# Tạo hàm không có giá trị trả về
def add():
    sum = a + b + c
    print(sum)

def sub():
    sub = c - b - a
    print(sub)

def hello():
    print("Hello "+"World")
# Gọi hàm 
add()
sub()
hello()

# Bài tập 1
def greet(name):
    name = input("Enter your name: ")
    print("Hello " + name)
greet()
# Bài tập 2
def gia_tri_tuyet_doi():
    number = int(input("Nhập một số nguyên dương: "))
    if number < 0:
        abs_value = -number
    else:
        abs_value = number
    print("Giá trị tuyệt đối của ", number, " là ", abs_value) 

gia_tri_tuyet_doi()
# Bài tập 3
def sum_even_numbers():
    n = int(input("Nhập một số nguyên dương n: "))
    sum = 0
    for i in range(2, n + 1, 2):
        sum += i
    # for i in range(1, n + 1):
    #     if i % 2 == 0:
    #         sum += i
    print("Tổng các số chẵn từ 1 đến", n, "là:", sum)
sum_even_numbers()
# Ví dụ về hàm có chứa tham số
def Xinchao(name):
    print("Hello " + name)

Xinchao("Vân")
Xinchao("Đan")

name = input("Nhập tên của bạn: ")
Xinchao(name)

def greet(first_name, last_name):
    print("Hello " + first_name + " " + last_name)

greet("Nguyễn", "Vân Anh")

def add(a, b):
    print(a + b)

add(3, 5)
add(10, 20)
add(-1, 1)

def in_info(name, age, address):
    print("Tên: " + name)
    print("Tuổi: " + age)
    print("Địa chỉ: " + address)
name = input("Nhập tên: ")
age = input("Nhập tuổi: ")
address = input("Nhập địa chỉ: ")
in_info(name, age, address)

# Bài tập 5
# Biến danh_sach là kiểu mảng list
def in_danh_sach_va_tong(danh_sach):
    print("Danh sách các phần tử")
    for so in danh_sach:
        print(so)
    tong = sum(danh_sach)
    print("Tổng các phần tử trong danh sách là:", tong)
danh_sach= []
n = int(input("Nhập số lượng phần tử trong danh sách: "))
for i in range(n):
    so = int(input("Nhập phần tử thứ {}: ".format(i + 1)))
    danh_sach.append(so)
in_danh_sach_va_tong(danh_sach)



# Ví dụ về phạm vi của biến
# Biến cục bộ
# a và b là biến cục bộ chỉ được sử dụng được trong hàm sum ngoài hàm sum không sử dụng được
def sum():
    a = 5
    b = 10
    print("Trong hàm sum, a + b =", a + b)
sum()
# Biến toàn cục
# a và b là biến toàn cục có thể sử dụng được trong hàm tinhtong và ngoài hàm tinhtong
a= 10
b= 2
def tinhtong():
    print(a+b)
tinhtong()
# Nếu trong hàm khởi tạo biến cục bộ trùng tên với biến toàn cục thì khi gọi biến trong hàm sẽ lấy giá trị của biến cục bộ
a = 10
b = 2
def tinhtong():
    b = 5
    print(a + b) #15
tinhtong()
print(a + b) #12
# Nếu muốn sử dụng biến toàn cục trong hàm thì sử dụng từ khóa global
a = 10
b = 2
def tinhtong():
    global b
    b = 5
    print(a + b) #15
tinhtong()
print(a + b) #15
# Ví dụ 1
x = 5
y = 3
def calculate_result():
    global x
    y = 4
    x = x * y
x *= -1
calculate_result()
print("Giá trị của biến x:", x)
# Ví dụ 2
total = 0
num1 = 0
num2 = 10
def calculate_total():
    num1 =5
    global total
    total = 0
    sum_result = num1 + num2
    total += sum_result
    product_result = num1 * num2
    total += product_result

calculate_total()
print("Giá trị của biến total:", total)