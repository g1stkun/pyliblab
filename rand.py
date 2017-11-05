import random

a = random.random()
b = random.randint(1, 5)
c = random.uniform(1, 5)
d = random.randrange(1, 20, 2)
print(a, b, c, d)

ns = [1, '가', 3, 4, 'A']
a = random.choice(ns)
b = random.sample(ns, 3)
random.shuffle(ns)
print(a, b, c, ns)
