try:
 canhrubik = int(input("Độ dài cạnh rubik:"))
 if canhrubik <= 0:
   print("Số không hợp lệ rùi")
 else:
  print("Số miếng dán: ", canhrubik**2 * 6)
except ValueError:
 print("Số không hợp lệ rùi") 

