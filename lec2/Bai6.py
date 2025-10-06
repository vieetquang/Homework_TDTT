from math import sqrt
a, b, c = map(int, input("Nhập độ dài 3 cạnh(Có dấu cách giữa cách cạnh)").split())
p = (a+b+c)/2
try:
    s = sqrt(p*(p-a)*(p-b)*(p-c))
    print("Diện tích tam giác:", s)
except ValueError:
    print("Khong phai 3 canh cua tam giac")
