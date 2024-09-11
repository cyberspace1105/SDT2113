import time
import matplotlib.pyplot as plt

def rand_bit():
    a = 918273645210143527345039683
    b = 1564376381919238011039485760361
    n = 817219445776617222361364238353
    x = int((time.time() * (10 ** 7)) % 1000000)  # Corrected the time calculation
    l = []  # Corrected the list name
    index = []
    for i in range(500):
        x = ((a * x) + b) % n
        y = x / n  # for random number between [0,1]
        l.append(y)  # Append the random number to the list
        index.append(i)
    plt.scatter(l, index)
    plt.title('LCG')
    plt.ylabel('Counts')
    plt.xlabel('Random value between 0 and 1')
    plt.show()

rand_bit()
