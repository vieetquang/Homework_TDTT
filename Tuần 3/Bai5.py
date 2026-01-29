kitu = input("Nhập ký tự: ")
if ord(kitu) == 65:
  print("z")
else:
  print((chr(ord(kitu)-1)).lower())