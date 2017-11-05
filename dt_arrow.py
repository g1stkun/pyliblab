import arrow

print(arrow.now('Asia/Seoul'))

utc = arrow.utcnow()
print(utc)

utc = utc.shift(hours=-1)
print(utc)

local = utc.to('Asia/Seoul')
print(local)

print(arrow.get('2013-05-11T21:23:58.970460+00:00'))

print(local.timestamp)

print(local.format())

print(local.format('YYYY-MM-DD HH:mm:ss ZZ'))

print(local.humanize())

print(utc.humanize(locale='ko_kr'), local.humanize(locale='ko_kr'))
