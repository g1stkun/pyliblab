from decimal import Decimal, ROUND_HALF_UP

a = Decimal(11111.56711)
b = 1.1
c = Decimal((0, (0,), -2))
c = a.quantize(c, ROUND_HALF_UP)
d = round(a, 3)
print(a * a, b * b, c, d)

