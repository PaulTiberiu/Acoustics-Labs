import numpy as np
import matplotlib.pyplot as plt

#1
N = 3
c0 = 343
rho0 = 1
S0 = 0.1
Sf = 0.1
S = np.array([5,10,5]) * S0
h = np.array([0.05,0.1,0.05])
f = np.linspace(1, 10000, 1000)

#2
def Tn(f0,rho0,c0,S,h):
    Z0 = rho0*c0
    k0 = 2*np.pi*f0/c0
    tn = np.zeros((2,2),dtype=complex) #matrice 2,2 complexe init a 0
    tn[0,0] = np.cos(k0*h)
    tn[0,1] = -1j*Z0/S*np.sin(k0*h)
    tn[1,0] = -1j*S/Z0*np.sin(k0*h)
    tn[1,1] = np.cos(k0*h)
    return tn

#3

D0 = np.zeros((2,2))
Z0 = rho0*c0
D0[0,0] = 1
D0[0,1] = 1
D0[1,0] = S0/Z0
D0[1,1] = -S0/Z0
D0_inv = np.linalg.inv(D0)
#M = np.zeros((2,2),dtype=complex)
M = D0_inv

for i in range(N):
    M = np.dot(M,Tn(f[0],rho0,c0,S[i],h[i]))

Df = np.zeros((2,2))
Df[0,0] = 1
Df[0,1] = 1
Df[1,0] = Sf/Z0
Df[1,1] = -Sf/Z0

M = np.dot(M,Df)

#4
t = 1/M[0,0]
r = M[1,0]*t
print("le coefficient t est: ",t)
print("le coefficient r est: ",r)


#5
def Mn(f):
    D0 = np.zeros((2,2))
    Z0 = rho0*c0
    D0[0,0] = 1
    D0[0,1] = 1
    D0[1,0] = S[0]/Z0
    D0[1,1] = -S[0]/Z0
    D0_inv = np.linalg.inv(D0)
    M = D0_inv

    for i in range(N):
        M = np.dot(M,Tn(f,rho0,c0,S[i],h[i]))

    Df = np.zeros((2,2))
    Df[0,0] = 1
    Df[0,1] = 1
    Df[1,0] = Sf/Z0
    Df[1,1] = -Sf/Z0

    M = np.dot(M,Df)
    return M

t = np.zeros(1000,dtype=complex) #tableau de coef transmission
for i in range(1000):
    M = Mn(f[i])
    t[i] = 1/M[0,0]

#6
#tracer facteur de perte en fonction de la frequence
facteur_perte = 10*np.log10(1/(np.abs(t)**2))
plt.plot(f,facteur_perte)
plt.show()