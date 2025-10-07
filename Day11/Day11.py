a = "MindX PTB39"
print(len(a))
print(a[0])
# Duyệt và in ra các phần tử trong xâu chuỗi a
# Cách 1
print("Duyệt và in ra các phần tử trong xâu chuỗi a cách 1:")
for i in a:
    print(i)
# Cách 2
print("Duyệt và in ra các phần tử trong xâu chuỗi a cách 2:")
for i in range(len(a)):
    print(a[i])
# Bài tập 1
print("Bài tập 1:")
A = "MindX Technology School"
for i in A:
    if i != " ":
        print(i)
print("=============================")
for i in range(len(A)):
    if A[i] != " ":
        print(A[i])
# Kiên thức liên quan xâu chuỗi
print("=============================")
xau1 = "Hello"
xau2 = "hello"
xau3 = "Hello, world!"
if xau1 in xau3:
    print("Xâu 1 nằm trong xâu 3")
else:
    print("Xâu 1 không nằm trong xâu 3")

if xau2 in xau3:
    print("Xâu 2 nằm trong xâu 3")
else:
    print("Xâu 2 không nằm trong xâu 3")

b = xau1 in xau3
c = xau2 in xau3
print(b)
print(c)
print("=============================")
# Vi dụ về hàm find()
a = "abcd1234"
b = "abc"
c = "d123"
d = "xyz"
print(a.find(b))  # Kết quả trả về là vị trí xuất hiện đầu tiên của chuỗi b trong chuỗi a
print(a.find(c))  # Kết quả trả về là vị trí xuất hiện đầu tiên
print(a.find(d))  # Kết quả trả về là -1 vì chuỗi d không nằm trong chuỗi a
print("=============================")
e = "cd1"
print(a.find(e)) 
f = "1234"
print(a.find(f)) 
print("=============================")
# Ví dụ về hàm find() với 3 tham số start và stop
print(a.find(b,2,7))
# Phương thức split() trong xâu chuỗi Python
print("=============================")
s = "1 2 4 d1 s12"
s1 = s.split()
print(s1)
s = "a,b,c,d1,s12"
s1 = s.split(',')
print(s1)
s = "a-b-c-d1-s12"
s1 = s.split('-')
print(s1)
info = "Nguyễn Văn A,20 tuổi,Hà Nội"
info_list = info.split(',')
print(info_list)
# Ví dụ về hàm replace()
print("=============================")
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)
txt = "I like bananas, bananas are my favorite fruit"
x = txt.replace("bananas", "apples")
print(x)
# Bài tập 2
print("Bài tập 2:")
ho = input("Nhập họ: ")
ten_dem = input("Nhập tên đệm: ")
ten = input("Nhập tên: ")
print(f"Họ và tên đầy đủ là: {ho} {ten_dem} {ten}")
# Bài tập 3
print("Bài tập 3:")
s = input("Nhập vào ngày tháng năm dd/mm/yyyy: ")  #ví dụ: 25/12/2023
# date_format = s.split('/')
# ngay = date_format[0]
# thang = date_format[1]
# nam = date_format[2]
ngay, thang, nam = s.split('/')
# print(f"Ngày {ngay} tháng {thang} năm {nam}")
# Bài tập 4
print("Bài tập 4:")
# Chuẩn bị thông tin tài khoản (định dạng "<username>:<password>")
account = "MindX:12345"
# Tách username và password từ chuỗi account
username_expected, password_expected = account.split(":")

# Vòng lặp yêu cầu đăng nhập tới khi đúng
while True:
    username_input = input("Nhập username: ").strip()
    password_input = input("Nhập password: ").strip()

    if username_input == username_expected and password_input == password_expected:
        print("Đăng nhập thành công!")
        break
    else:
        print("Thông tin đăng nhập chưa chính xác, vui lòng thử lại\n")