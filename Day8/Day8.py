
# Chương trình kiểm tra một số có phải là số nguyên tố hay không
while True:
    n = int(input("Nhập vào một số nguyên dương n: "))
    if n == 2:
        print(f"{n} là số nguyên tố")
        continue   
    elif n < 2:
        print(f"{n} không phải là số nguyên tố")
        continue
    elif n % 2 == 0:
        print(f"{n} không phải là số nguyên tố")
        continue
    else:
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                print(f"{n} không phải là số nguyên tố")
                continue
        else:
            print(f"{n} là số nguyên tố")
            continue

# Chương trình tìm bội chung nhỏ nhất và tối giản phân số của hai số nguyên dương a và b nhập vào từ bàn phím
while True:
    a = int(input("Nhập vào một số nguyên dương a: "))
    b = int(input("Nhập vào một số nguyên dương b: "))
    for i in range(1, (a*b)+1):
        if i % a == 0 and i % b == 0:
            print(f"Bội chung nhỏ nhất của {a} và {b} là: {i}")
            x  = int(i/b)
            y = int(i/a)
            print(f"Tối giản phân số {a}/{b} là: {x}/{y}")
            break
    continue
