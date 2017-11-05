import math

a = abs(-1.2)
b = max([1, -2, 5])
c = max(1, -2, 5)
d = max('a', 'b', 'e', '가', '1')
e = min('a', 'b', 'e', '가', '1')
f = sum([1, 2, 3], 2)
g = pow(1.1, 1.5)
print(a, b, c, d, e, f, g)

a = math.log(100)
b = math.log(100, 10)
c = math.log10(100)
d = math.pow(1.1, 1.5)
e = 2 ** 3
f = math.sqrt(15)
g = math.radians(60)
h = math.sin(f)
i = math.cos(f)
print(a, b, c, d, e, f, g, h, i)

a = math.ceil(3.14)
b = math.ceil(-3.14)
c = math.floor(3.14)
d = math.floor(-3.14)
e = math.trunc(3.14)
f = math.trunc(-3.14)
print(a, b, c, d, e, f)

print(math.pi, math.e)