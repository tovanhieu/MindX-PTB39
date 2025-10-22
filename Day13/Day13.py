
# Ví dụ về hàm trả về giá trị trong Python
def tinh_tong(a,b):
    sum = 0
    sum = a + b
    return sum
ket_qua = tinh_tong(5,10)
print("Kết quả là:",ket_qua)
# BT1 Viết hàm truyền vào hai số nguyên a và b, trả về a lũy thừa b
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
def luy_thua(a,b):
    return a ** b
print(f"{a} lũy thừa {b} là:", luy_thua(a,b))
# BT2 Viết hàm truyền vào một số nguyên trả về giá trị tuyệt đối của số nguyên đó
n = int(input("Nhập một số nguyên: "))
def gia_tri_tuyet_doi(n):
    if n < 0:
        return -n
    else:
        return n
print(f"Giá trị tuyệt đối của {n} là:", gia_tri_tuyet_doi(n))
# BT3 Viết hàm truyền vào một danh sách, trả về tổng các phần tử trong danh sách đó
ds = [1,2,3,4,5]
def tong_cac_phan_tu(ds):
    tong = 0
    for i in ds:
        tong += i
    return tong
print("Tổng các phần tử trong danh sách là:", tong_cac_phan_tu(ds))
# Ví dụ về hàm trả về kiểu số thực
def avg(x,y):
    return (x + y) / 2
x = float(input("Nhập số thứ nhất: "))
y = float(input("Nhập số thứ hai: "))
print(f"Trung bình cộng của {x} và {y} là: {avg(x,y)}")
# Ví dụ về hàm trả về kiểu boolean True or False
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
n = int(input("Nhập một số nguyên: "))
result = is_even(n)
print(result)
# Ví dụ về hàm trả về kiểu chuỗi str
def chao_hoi(name):
    return "Xin chào " + name + "!"
name = input("Nhập tên của bạn: ")
chao = chao_hoi(name)
print(chao)
# Ví dụ về hàm trả về kiểu danh sách list
def get_even_numbers(n):
    even_numbers = []
    for i in range(2, n+1,2):
        even_numbers.append(i)
    return even_numbers
n = int(input("Nhập một số nguyên dương: "))
even_nums = get_even_numbers(n)
print(f"Các số chẵn từ 1 đến {n} là:", even_nums)
# BT4 Tính số viên gạch cần để lát phòng hình vuông
def tinh_dien_tich_phong(canh):
    return canh * canh
def tinh_so_vien_gach(dien_tich_can_phong, dien_tich_mot_vien_gach):
    so_vien_gach = dien_tich_can_phong / dien_tich_mot_vien_gach
    return so_vien_gach
canh_can_phong = 80 # đơn vị m
dien_tich_mot_vien_gach = 0.2 * 0.2 # đơn vị m2
so_tam_gach = tinh_so_vien_gach(tinh_dien_tich_phong(canh_can_phong), dien_tich_mot_vien_gach)
print(f"Số viên gạch cần để lát phòng là: {round(so_tam_gach)} viên")
#  Ví dụ về việc sử dụng các hàm có sẵn trong Python
import math 
print(math.pi)
print(math.sqrt(16))
print(max(5,10))
print(min(5,10))
print(math.pow(2,3))
from math import sqrt, pi
print(sqrt(25))

text = "MindX PTB39"
print(text.upper())
print(text.lower())
print(text.replace("PTB39","PTB40"))
print(text.split(" "))

print(round(3.14159,2))

import random
print(random.randint(1,100))
print(random.random())