tenchuho = input("Ten chu ho:")
lastmonth = int(input("Chi so thang truoc:"))
thismonth = int(input("Chi so thang nay:"))
sodien = thismonth - lastmonth
def tinhtiendien(a):
 if 0 <= a <= 50:
  return a * 1984
 elif 51 <= a <= 100:
  return 50*1984 + (a-50)*2050
 elif 101 <= a <= 200:
  return 50*1984 + 50*2050 + (a-100)*2380
 elif 201 <= a <= 300:
  return 50*1984 + 50*2050 + 100*2380 + (a - 200)*2998
 elif 301 <= a <= 400:
  return 50*1984 + 50*2050 + 100*2380 + 100*2998 + (a - 300)*3350
 elif a >= 401:
  return 50*1984 + 50*2050 + 100*2380 + 100*2998 + 100*3350 + (a - 400)*3460
 else: 
  return "Số điện không hợp lệ"
print("Ho va ten:", tenchuho, "\nTien phai tra la:", tinhtiendien(sodien) )
