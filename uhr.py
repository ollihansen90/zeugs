import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

zeit = dt.datetime.now()
h = zeit.hour
m = zeit.minute

print(h, m)

base = np.linspace(-1,1)*np.pi
kreis = np.array([np.sin(base), np.cos(base)])
zahlen = np.arange(1,13)

t = lambda w: np.array([np.sin(w), np.cos(w)])
minute = 0.9*t(m/60*2*np.pi)
stunde = 0.7*t(((h%12)+m/60)/12*2*np.pi)

plt.figure()
plt.plot(kreis[0], kreis[1], "k")
plt.plot([0,minute[0]], [0,minute[1]])
plt.plot([0,stunde[0]], [0,stunde[1]])
for z in zahlen:
    zz = 1.1*t((z%12)/12*2*np.pi)
    #print(zz, z)
    plt.text(zz[0],zz[1], z,horizontalalignment="center", verticalalignment="center")
plt.axis("equal")
plt.axis("off")
plt.show()