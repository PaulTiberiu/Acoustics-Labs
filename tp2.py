import numpy as np
import matplotlib.pyplot as plt
import h5py as h5
data_file = h5.File('Data_Signaux.h5','r')
t = data_file['t'][:]
h = data_file['h'][()]
Signal = data_file['Signal'][:]
Signal_ref = data_file['Signal_ref'][:]
data_file.close()
#Signal est une matrice 3D donc Signal[x,y,t] ou t=temps

#2.1
rho1 = 1000
c1 = 1500
#rho2, c2 inconnues

#3
plt.plot(t, Signal_ref)
plt.show()

#4
i_Aref = np.argmax(Signal_ref, axis = 0)
print("L'indice de l'amplitude Aref du maximum du signal est: ", i_Aref)
Aref = Signal_ref[i_Aref]
print("L'amplitude Aref du maximum du signal est: ", Aref)

tref = t[i_Aref]
print("Le temps d'arrivee du signal est" ,tref)

#5
print(np.shape(Signal))
s = Signal[3, 3] #signal quelconque du tableau Signal
A1 = s[i_Aref]
print("L'amplitude du Signal[3,3] est: ",A1)

#6
r1 = A1/Aref
print("Le coefficient de reflexion est: ", r1)

#7
i=0
j=0
print(len(Signal))
Z1 = rho1*c1
print("L'impedance du millieu 1 est: " , Z1)
Z2 = np.zeros((98,98))

#ou bien i<len(Signal)
while i<Signal.shape[0]:
    while j<Signal.shape[1]:
        s = Signal[i, j]
        A = s[i_Aref]
        r = A/Aref
        Z2[i,j] = Z1*(1+r)/(1-r) #formule cours
        print("L'impedance du signal i=",i," j=",j," est: ",Z2[i][j])
        j+=1
    i+=1
    j=0

plt.pcolormesh(Z2)
plt.colorbar()
plt.show()

#2.2
#1
s = Signal[4, 4] #signal quelconque du tableau Signal
plt.plot(t,s)
plt.show()
plt.plot(s) #on observe que 100 c'est l'indice entre les 2 echos
plt.show()

s1 = s[ : 100]
s2 = s[100 : ]

t1 = t[ : 100]
t2 = t[100 : ]

plt.plot(t1, s1)
plt.show()

plt.plot(t2, s2)
plt.show()

#2
i_Aref1 = np.argmax(s1, axis = 0)
print("L'indice de l'amplitude Aref du maximum du signal s1 est: ", i_Aref1)
Aref1 = s1[i_Aref1]
print("L'amplitude Aref du maximum du signal est: ", Aref1)

t1 = t1[i_Aref1]
print("Le temps d'arrivee du signal est" ,t1)

i_Aref2 = np.argmax(s2, axis = 0)
print("L'indice de l'amplitude Aref du maximum du signal s2 est: ", i_Aref2)
Aref2 = s2[i_Aref2]
print("L'amplitude Aref du maximum du signal est: ", Aref2)

t2 = t2[i_Aref2]
print("Le temps d'arrivee du signal est" ,t2)

#3 et 4
dt = np.zeros((98,98))
c2 = np.zeros((98,98))
rho2 = np.zeros((98,98))
xi2 = np.zeros((98,98))
h = 1*10**(-3)

i=0
j=0

while i<Signal.shape[0]:
    while j<Signal.shape[1]:
        s = Signal[i,j]
        s1 = s[ : 100]
        s2 = s[100 : ]
        t1 = t[ : 100]
        t2 = t[100 : ]
        i_Aref1 = np.argmax(s1)
        i_Aref2 = np.argmax(s2)
        dt[i,j] = t2[i_Aref2] - t1[i_Aref1]
        c2[i,j] = 2*h/dt[i,j] #aller retour, donc 2*h/dt
        rho2[i,j] = Z2[i,j]/c2[i,j]
        xi2[i,j] = 1/(rho2[i,j]*c2[i,j]**2)
        j+=1
    i+=1
    j=0

plt.pcolormesh(rho2)
plt.colorbar()
plt.show()

plt.pcolormesh(xi2)
plt.colorbar()
plt.show()