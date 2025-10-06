score = input("điền điểm:").split()
a1, b1, c1, d2, e2, f3 = map(float, score)
tb = ((a1 + b1 + c1) + (d2 + e2) * 2 + f3 * 3) / 10
print(tb)