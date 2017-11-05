from datetime import date, datetime, time, timedelta

a = date(2017, 8, 9)
b = datetime(2017, 8, 9)
c = b.today() - b
d = time(12, 34, 56)
e = b.today() + timedelta(days=7, hours=1)
print(a, b, c, d, d.tzname(), e)

import time

a = time.gmtime()
b = time.localtime()
c = time.time()
print(a, b, c)

for i in range(10):
    print(i)
    time.sleep(1)
