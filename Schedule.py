import matplotlib as mpl
import matplotlib.pyplot as plt
import math

dpi = 80
fig = plt.figure(dpi=dpi, figsize=(600 / dpi, 450 / dpi))
mpl.rcParams.update({'font.size': 10})

plt.axis([994106500000895, 994106500500000, 899000, 903000])

plt.title('PROD_CODE & BASKET_ID')
plt.xlabel('PROD_CODE')
plt.ylabel('BASKET_ID')


def res(string1, ints1):
    print(len(str(ints1)))
    plt.plot(ints1, string1 , color='blue', linestyle='solid',
             label='PROD_CODE')

    plt.legend(loc='upper right')
    fig.savefig('trigan.png')


file = open('C:\\Users\\Никита\\Desktop\\Interview\\transactions.csv')
string = []
ints = []
j = 0
for line in file:
    s = line.split(';')
    o = []
    o1 = []
    i = 0
    for s1 in s:
        if i % 2 == 0:
            o.append(int(s1[4:]))
            j += 1
        elif i % 2 == 1:
            o1.append(int(s1))
        i += 1
    ints.append(o1)
    string.append(o)
res(string, ints)
