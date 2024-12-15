import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq

Fs = 800.0   # sampling frequency
N = 600      # Number of samplepoints
Ts = 1.0 / Fs # sample spacing
#x = np.linspace(0.0, N*Ts, N)
#x = np.linspace(0.0, N,num=N,endpoint=0)
x=np.arange(N)
#s=np.array([np.sin((50/Fs) * 2.0*np.pi*x), np.sin((80/Fs) * 2.0*np.pi*x), np.sin((160/Fs) * 2.0*np.pi*x)])
s=np.array([np.exp(2.0j*(20/Fs)*np.pi*x), np.exp(2.0j*(80/Fs)*np.pi*x),
    np.exp(2.0j*(160/Fs)*np.pi*x)])
s=np.array([np.sin(2.0*np.pi*(20/Fs)*x), np.sin(2.0*np.pi*(80/Fs)*x),
    np.sin(2.0*np.pi*(160/Fs)*x)])
y = np.sum(s, axis=0)
#y = np.sin(50.0 * 2.0*np.pi*x) + 0.7*np.sin(80.0 * 2.0*np.pi*x)
#y = np.exp(1j*2.0*np.pi*(50/Fs)*x) + 0.7*np.exp(1j*2.0*np.pi*(80/Fs)*x)
yf = fft(y)
#xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
xf = fftfreq(N,d=1/Fs)

fig,axs = plt.subplots(4,1,sharey=True, sharex=True)
fig.set_size_inches((10,5))
fig.suptitle('Señales',fontsize=18)

for n in range(3):
    ax=axs[n]
    ax.plot(x,s[n].real)
    #ax.legend(loc=0,fontsize=16)
    #ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    #ax.set_ylabel(r'dB',fontsize=22)
    #ax.set_ylabel('ch{}[mV?]'.format(n+1),fontsize=14)
    ax.set_ylabel(r'$s_{}$[V]'.format(n+1))
    ax.grid()

ax=axs[3]
ax.plot(x,y.real)
ax.set_ylabel('y[V]')
ax.grid()
plt.show()

#fig, ax = plt.subplots(4,1)
#ax.plot(x,y)
##ax.plot(xf[:int(N/2)], np.abs(yf[0:int(N/2)])/N)
#plt.grid(True)
#plt.show()

fig, ax = plt.subplots()
ax.plot(xf[:int(N/2)], 2.0/N * np.abs(yf[0:int(N/2)]))
#ax.plot(xf[:int(N/2)], 1.0/N * np.abs(yf[0:int(N/2)]))
#ax.plot(xf[:int(N/2)], np.abs(yf[0:int(N/2)])/N)
plt.grid(True)
plt.show()
