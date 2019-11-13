import time
import math
import matplotlib.pyplot as plt

timelist = []
icounter = 0

while icounter < 6:
    st = time.time()
    input('Input your name: ')
    et = time.time()
    tt = math.ceil(et - st)
    timelist.append(tt)
    icounter += 1

print(timelist)

x = ['1a','2a','3a','4a','5a','6a']
y = timelist
plt.plot(x,y)
plt.show()
