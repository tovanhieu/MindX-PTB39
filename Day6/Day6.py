# Demo vòng lặp for 1 tham số trong python
for i in  range(9):
    print(i, end=" ")
print("\n")

for i in range(10):
    print("Hello world " + "lần thứ ",i+1, end=" ")
    print("\n")
# Demo vòng lặp for 2 tham số trong python
for i in range(0,5):
    print(i, end=" ")
# Demo vòng lặp for 3 tham số chứa step trong python
print("\n")
print("ví dụ về step trong hàm range")
for i in range(0,10,2):
    print(i, end=" ")
print("\n")

# sử dụng vòng lặp và in ra giá trị trong khảng từ 1 đến 20 với số bước nhảy step là 3 -> in ra có tổng bao nhiêu số được in trên màn hình
dem = 0
for i in range(1,20,3):
    print(i, end=" ")
    # dem += 1
    dem = dem + 1
    print("\n")
print("Tông số các số được in ra trong khoảng 1 đến 20 với số bước nhảy step = 3 là: ", dem)

# Bài tập tính tổng các số từ  0 đến n
n = int(input("Nhập vào số n: "))
tong = 0
for i in range(0,n):
    print(i)
    tong += i
print("Tổng các số từ 0 đến n là: ", tong)
# In ra màn hình bảng cửu chương từ 2 đến 9
print("Bảng cửu chương từ 2 đến 9")
for i in range(2,10):
    # print(f"Bảng cửu chương của {i}: ")
    # for j in range(1,11):
    #     print(f"{i} x {j} = {i*j}")
    # print("\n")

    print("Bảng cửu chương của ",i ," : ")
    for j in range(1,11):
        print(i, "x", j, " = ", i*j)
    print("\n")
    
# In ra màn hình bảng cửu chương các sô chẵn từ 2 đến 9
print("Bảng cửu chương từ các số chắn 2 đến 9")
for i in range(2,10,2):
    # print(f"Bảng cửu chương của {i}: ")
    # for j in range(1,11):
    #     print(f"{i} x {j} = {i*j}")
    # print("\n")

    print("Bảng cửu chương của ",i ," : ")
    for j in range(1,11):
        print(i, "x", j, " = ", i*j)
    print("\n")