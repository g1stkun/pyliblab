a = '123abc'.isalnum()
b = '123abc#'.isalnum()
print(a, b)

a = 'abcd'.isalpha()
b = '가나다라'.isalpha()
c = 'abc123'.isalpha()
print(a, b, c)

a = 'UPPERCASE'.isupper()
b = 'lowerccase'.isupper()
c = 'lowerccase'.islower()
print(a, b, c)

a = 'Title String'.istitle()
b = 'TitleString'.istitle()
c = 'titleString'.istitle()
d = 'titlestring'.istitle()
print(a, b, c, d)

n = '123456789①'
a = n.isdecimal()
b = n.isdigit()
c = n.isnumeric()
print(a, b, c)

a = 'HELLO world!'.upper()
b = 'HELLO world!'.lower()
c = 'HELLO world!'.swapcase()
d = 'HELLO world!'.capitalize()
e = 'HELLO world!'.title()
print(a, b, c, d, e)

a = 'HELLO world!'.replace('world', 'python')
b = 'HELLO world!'.replace('L', 'l', 1)
print(a, b)

a = 'python'.find('th')
b = 'python'.find('TH')
print(a, b)

a = 'aa bbb cccc'.split()
print(a)

a = '-'.join(a)
print(a)

a = 'python'.startswith('py')
print(a)

a = 'image.png'.endswith(('jpg', 'png'))
b = 'image.txt'.endswith(('jpg', 'png'))
print(a, b)

a = '가abcd나'.encode('ascii', 'ignore')
b = '가abcd나'.encode('ascii', 'replace')
print(a, b)

a = 'abc가나⊙'.isprintable()
print(a)