import numpy as np
import matplotlib.pyplot as plt

a = 60
c = 2
m = 2**(31) - 1
x = 0.1

index = []
randvalue = []
for i in range(1, 500):
    x = np.mod((a * x + c), m)
    u = x / m
    print(u)
    index.append(i)
    randvalue.append(u)

plt.scatter(randvalue, index)
plt.title('LCG-Lewis-Learmonth Algorithm')
plt.ylabel('Counts')
plt.xlabel('Random value between 0 and 1')
plt.show()
