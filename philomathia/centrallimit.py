import random as random
import numpy as np 
import matplotlib.pyplot as plt 

results1 = []
results2 = []
results3 = []

mean1 = []
mean2 = []
mean3 = [] 

var1 = []
var2 = []
var3 = [] 

#fonction de génération de nombre aléatoire entre 0 et 50000
def random1():
    for i in range(20000):
        x = random.randint(0,50000)
        results1.append(x)
        mean1.append(np.mean(results1))
        var1.append(np.var(results1))

def random2():
    for i in range(10000):
        x = random.randint(0,50000)
        results2.append(x)
        mean2.append(np.mean(results2))
        var2.append(np.var(results2))

def random3():
    for i in range(1000):
        x = random.randint(0,50000)
        results3.append(x)
        mean3.append(np.mean(results3))
        var3.append(np.var(results3))

def plot():
    plt.figure(figsize=(12, 6))

    plt.subplot(2, 3, 1)
    plt.boxplot(mean1, labels=['20 000'])
    plt.title("Distribution des moyennes pour 20 000")
    
    plt.subplot(2, 3, 2)
    plt.boxplot(mean2, labels=['10 000'])
    plt.title("Distribution des moyennes pour 10 000")

    plt.subplot(2, 3, 3)
    plt.boxplot(mean3, labels=['1 000'])
    plt.title("Distribution des moyennes pour 1 000")

    plt.subplot(2, 3, 4)
    plt.plot(var1, label='20 000', color='blue')
    plt.legend(loc='upper right')

    plt.subplot(2, 3, 5)
    plt.plot(var2, label='10 000', color='green')
    plt.legend(loc='upper right')

    plt.subplot(2, 3, 6)
    plt.plot(var3, label='1 000', color='red')
    plt.legend(loc='upper right')

    plt.suptitle("Distribution des moyennes et écart type de 20 000, 10 000 et 1 000 nombres aléatoires générés entre 0 et 50 000")
    plt.show()

