import collections

c = collections.Counter()
c['spam'] += 1
c[100] += 1
c[200] += 1
c[200] += 3
print(c)

c = collections.Counter(
    [1, 2, 3, 1, 2, 1, 2, 1]
)
print(c)

c1 = collections.Counter(spam=1, ham=2)
c2 = collections.Counter(ham=3, egg=4)
print(c1 + c2, c1 - c2, c1 & c2, c1 | c2)

c = c1 | c2
d1 = {'spam': 1, 'ham': 2}
d2 = {'ham': 3, 'egg': 4}
cm = collections.ChainMap(d2, d1)
print(c, cm, d2)

cm['bacon'] = 3
print(cm, d2)

d = collections.defaultdict(lambda: 'default')
print(d['ham'])

d = collections.defaultdict(int)
print(d['spam'])

d = collections.OrderedDict()
d['spam'] = 100
d['ham'] = 200
for key in d:
    print(key)

Coordinate = collections.namedtuple('Coordinate', 'X, Y, Z')
c = Coordinate(1, 2, 3)
print(c)

deq = collections.deque(['a', 'b', 'c'])
deq.append('d')
deq.appendleft(1)
deq.rotate(2)
print(deq)
