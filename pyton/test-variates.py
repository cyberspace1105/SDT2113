import random
#random.seed(12345)

print('Exponential dist')
for i in range(10):
    print('%05.4f' % random.expovariate(20), end=' ')
    