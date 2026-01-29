try: 
 n = int(input("Nhập số nguyên dương n: "))
 if n <=  0:
    print("Số không hợp lệ rùi")
 else:
    sosao = 1 + (n-1)*6
    print("Số sao thứ với số nguyên n là:", sosao)
except ValueError:
 print("Số không hợp lệ rùi")