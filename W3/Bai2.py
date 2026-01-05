a = float(input("Nhập chiều dài khu đất:"))
b = float(input("Nhập chiều rộng khu đất:"))
try:
    if a < b:
        raise ValueError("Chiều dài phải lớn hơn chiều rộng")
    if a <= 0 or b <= 0:
        raise ValueError("Chiều dài và chiều rộng phải là số dương")
    skhudat = a * b
    skhuvuichoi = ((b/2) ** 2) * 3.14
    print("Diện tích khu đất là:", skhudat)
    print("Diện tích khu vui chơi là:", skhuvuichoi)
    print("Diện tích trồng cây là:", skhudat - skhuvuichoi)
except ValueError as e:
    print("Lỗi:", e)