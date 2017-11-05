import re

a = re.match('a.c', 'abcd')
b = re.search('a.c', 'abcd')
c = re.match('b', 'abcd')
d = re.search('b.', 'abcd')
e = re.search('(b.)(d.)', 'abcdbde').group()
f = re.search('(b.)(d.)', 'abcdbde').group(1)
g = re.search('(b.)(d.)', 'abcdbde').groups()
h = re.search('(?P<first>b.)(?P<last>d.)', 'abcdbde').groupdict()
i = re.search('(?P<first>b.)(?P<last>d.)', 'abcdbde').expand(r'##\1##\2##')
j = re.sub('(?P<first>b.)(?P<last>d.)', '#\g<last>#\g<first>#', 'abcdbde')

print(a, b, c, d, e, f, g, h, i, j)
