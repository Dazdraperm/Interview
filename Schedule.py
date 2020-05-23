import matplotlib as mpl
import matplotlib.pyplot as plt
import math

import numpy as np
dpi = 100
fig = plt.figure(dpi=dpi, figsize=(600 / dpi, 450 / dpi))
mpl.rcParams.update({'font.size': 10})




def res(string1, ints1):
    x = np.arange(994106500000895, 994106500834677)
    #y = np.(string1)
   # lt.title('PROD_CODE & BASKET_ID')
    plt.xlabel('PROD_CODE')
    plt.ylabel('BASKET_ID')
   # plt.plot(y,ints1, label='PROD_CODE')
    fig.savefig('trigan.png')


def getPlot(values1, values2, title='Plot', xl='x', yl='y', imgtitle="plot"):
    fig, ax = plt.subplots()
    ax.plot(values1, values2)
    plt.tick_params(labelsize=9)
    ax.set(xlabel=xl, ylabel=yl, title=title)
    ax.grid()
    fig.savefig(imgtitle)


file = open('C:\\Users\\Никита\\Desktop\\Interview\\transactions.csv')
string = []
ints = []
for line in file:
    s = line.split(';')
    o = []
    o1 = []
    i = 0
    for s1 in s:
        if i % 2 == 0:
            o.append(int(s1[4:]))

        elif i % 2 == 1:
            o1.append(int(s1[9:]))
            print(int(s1[9:]))

        i += 1
    ints.append(o1)
    string.append(o)
getPlot(string, ints, 'title', 'x', 'y', 'trigan.png')
