import numpy as np
import matplotlib.pyplot as plt

#1.1
#2
T = 0.01
t = np.linspace(0, 1000*T, 10000) #T=0.01 et dans une seconde je veux 10000 points
print(t)

#3
f0 = 100
s = np.sin(2*np.pi*f0*t)
print(s)

#4
plt.plot(t,s)
plt.xlim(0,0.5)
plt.show()

#5
TF = np.fft.fft(s) #transforme de fourrier
dt = t[1]-t[0] #trouver le temps entre 2 points de notre vecteur temps
#linspace calcule tout seul le dt en fonction de parametres
freq = np.fft.fftfreq(len(s), dt)

plt.plot(freq, np.abs(TF)) #car il faut le module
plt.show()

#6
TF_i = np.fft.ifft(TF) #transforme inverse de fourrier
plt.plot(t, TF_i, 'r') # = s(t)
plt.xlim(0,0.5)
plt.show()

#7
sigma = 300
t0 = 20*10**(-3)
p = (sigma*(t-t0))**2
param_exp = (-1/2)*p
s2 = np.sin(2*np.pi*f0*t)*np.exp(param_exp)
print(s2)
plt.plot(t,s2)
plt.xlim(0,0.5) 
plt.show()

TF2 = np.fft.fft(s2) #transforme de fourrier
freq2 = np.fft.fftfreq(len(s2), dt)
plt.plot(freq2, np.abs(TF2))
plt.show()

TF2_i = np.fft.ifft(TF2)
plt.plot(t, TF2_i, 'g')
plt.xlim(0,0.5)
plt.show()

#1.2
#1 on utilise s2 et TF2
d = 100*10**(-3)
V = 340
w = 2*np.pi*np.abs(freq2)
k = np.abs(w)/V
TF1 = TF2*np.exp(-1j*k*d)
TF1_i = np.fft.ifft(TF1) #transforme inverse de fourrier
plt.plot(t, TF1_i, 'y') # = s2(t) qu'on veut determiner avec la relation (2)
plt.xlim(0,0.5)
plt.show()

#2
Nsignaux = 10 #nombre de signaux a calculer
tab_s2 = np.zeros((Nsignaux,10000)) #on initialise un tableau pour representer le signal sur 5 positions
#chaque position a besoin de 10000 pas de temps
d = np.linspace(0,V/2,Nsignaux) # vecteur de position car on veut regarder le signal sur une distance de 0.5*V

for i in range(len(d)):
    tab_s2[i, :] = np.real(np.fft.ifft(TF2*np.exp(-1j*k*d[i])))


for j in range(len(d)):
    plt.plot(t, tab_s2[j, :])
    plt.xlim(0,0.5)
    plt.show()

#3
k = np.sqrt(np.abs(w))/3
d = 100*10**(-3)
TF1 = TF2*np.exp(-1j*k*d)
TF1_i = np.fft.ifft(TF1) #transforme inverse de fourrier
plt.plot(t, TF1_i, 'r') # = s2(t) qu'on veut determiner avec la relation (2)
plt.xlim(0,0.5)
plt.show()

tab_s2 = np.zeros((5,10000)) #on initialise un tableau pour representer le signal sur 5 positions
#chaque position a besoin de 10000 pas de temps
d = np.linspace(0,V/10,5) # vecteur de position car on veut regarder le signal sur 5 positions

for i in range(len(d)):
    tab_s2[i, :] = np.real(np.fft.ifft(TF2*np.exp(-1j*k*d[i])))

for j in range(len(d)):
    plt.plot(t, tab_s2[j, :], 'r')
    plt.xlim(0,0.5)
    plt.show()

#4
s3 = s2 + np.random.rand(10000)/10 #ajout du bruit de quelques pourcentages sur le pas de temps
s3 = s3 - np.mean(s3) #retrait composante continue, returns average value of the array
TF3 = np.fft.fft(s3) #transforme de fourrier
freq3 = np.fft.fftfreq(len(s3), dt)
d = 100*10**(-3)
V = 340
w = 2*np.pi*np.abs(freq3)
k = np.sqrt(np.abs(w))/3 #propagation dispersive
TF1 = TF3*np.exp(-1j*k*d)
TF1_i = np.fft.ifft(TF1) #transforme inverse de fourrier
plt.plot(t, TF1_i, 'y') # = s2(t) qu'on veut determiner avec la relation (2)
plt.xlim(0,0.5)
plt.show()

tab_s3 = np.zeros((5,10000)) #on initialise un tableau pour representer le signal sur 5 positions
#chaque position a besoin de 10000 pas de temps
d = np.linspace(0,V/9,5) # vecteur de position car on veut representer le signal
#sur plusieurs positions, dans ce cas 5

for i in range(5):
    tab_s3[i, :] = np.real(np.fft.ifft(TF3*np.exp(-1j*k*d[i])))

for j in range(5):
    plt.plot(t, tab_s3[j, :], 'g')
    plt.xlim(0,0.5)
    plt.show()