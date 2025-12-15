chu = input("nhap chu")
if len(chu) == 1 and 'a' <= chu <= 'z':
    ma_unicode = ord(chu)
    ma_inhoa= ma_unicode - 32
    chu_inhoa = chr(ma_inhoa)
    print(f"chu in hoa la {chu_inhoa}, ma unicode la {ma_inhoa}")
else: print("nhap sai rui")