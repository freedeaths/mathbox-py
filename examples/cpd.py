import matplotlib.pyplot as plt
import random

from mathbox.app.signal.change_point import e_divisive

def one_time():
    return e_divisive(data,jump=3,pvalue=0.05,permutations=100)
    
    
if __name__ == "__main__":
    data_1 = [0 for _ in range(10)] + [100 for _ in range(10)] + [50 for _ in range(10)] + [100 for _ in range(10)] + [0 for _ in range(10)] + [100 for _ in range(10)] + [0 for _ in range(10)]
    data_1 = [x + random.randint(-1, 1) for x in data_1]

    data_2 = [0 for _ in range(10)] + [100 for _ in range(10)] + [50 for _ in range(10)] + [50+5*x for x in range(10)] + [100 for _ in range(10)] + [100-10*x for x in range(10)] + [0 for _ in range(10)]
    data_2 = [x + random.randint(-1, 1) for x in data_2]

    data_3 = [0,0,0,0,0,0,1,1,1,1,1,5,5,5,5,5]

    data = data_1
    
    #'''
    cp = one_time()
    print("x:",cp)
    plt.plot(data)
    plt.plot([x for x in cp],[data[x] for x in cp],'ro')
    plt.show()
    '''
    for i in range(100):
        print("i:",i)
        cp = one_time()
        print("x:",cp)
    '''