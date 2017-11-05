import statistics

data = [1, 2, 2, 3, 4, 5, 6]
a = statistics.mean(data)
b = statistics.median(data)
c = statistics.mode(data)
print(a, b, c)

a = statistics.pstdev(data)
b = statistics.stdev(data)
c = statistics.pvariance(data)
d = statistics.variance(data)
print(a, b, c, d)
