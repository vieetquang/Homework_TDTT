tenchuho = input("Ten chu ho:")
lastmonth = int(input("Chi so thang truoc:"))
thismonth = int(input("Chi so thang nay:"))
sodien = thismonth - lastmonth
bac = {"bac1": (50, 1984), "bac2": (100, 2050), "bac3": (200, 2380), "bac4": (300, 2998), "bac5": (400, 3350), "bac6": (float('inf'), 3460)}
def tinhtiendien(a):
  conlai = a
  if conlai < 0:
    return("Số điện không hợp lệ")
  cost = 0
  for name, (limit, price) in bac.items():
   sodu = min(conlai, limit)
   cost += sodu * price
   conlai -=  sodu
   if conlai == 0:
    break
  return cost

print("Ho va ten:", tenchuho, "\nTien phai tra la:", tinhtiendien(sodien) )

