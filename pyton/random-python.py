import random
import matplotlib.pyplot as plt

# Set the random seed for reproducibility
random.seed(13579)

index = []
randvalue = []
for i in range(1000):
    x = random.random()
    #print('%:05.4f' % x, end='')
    print('{:.4f}'.format(x), end='')
    index.append(i)
    randvalue.append(x)

plt.scatter(randvalue, index)
plt.title('MT-Python-random()')

plt.ylabel('Counts')
plt.xlabel('Random value between 0 and 1')
plt.show()
