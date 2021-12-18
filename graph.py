import time
import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, Button, RadioButtons





def minY(arr):
    minY = arr[0]
    for a in arr:
        if (a < minY):
            minY = a
    return minY

def maxY(arr):
    maxY = arr[0]
    for a in arr:
        if (a > maxY):
            maxY = a
    return maxY


arr = []                                #Энергия
Ne = 0
with open("energy.txt") as f:
    for line in f:
        arr.append(line.split())
        Ne = Ne + 1
E = []
K = []
U = []
for i in range(Ne):
    E.append(float(arr[i][0]))
    U.append(float(arr[i][1]))
    K.append(float(arr[i][2]))




P = []                                   #Импульс
Np = 0
with open("momentum.txt") as f:
    for line in f:
        P.append(line.split())
        Np = Np + 1
Px = []
Py = []
Pz = []
for i in range(Np):
    Px.append(float(P[i][0]))
    Py.append(float(P[i][1]))
    Pz.append(float(P[i][2]))      
    
    
    
AveDev = []                              #Среднеквадратичное отклонение
Nd = 0
with open("deviation.txt") as f:
    for line in f:
        AveDev.append(line.split())
        Nd = Nd + 1
ADx = []
ADy = []
ADz = []
for i in range(Nd):
    ADx.append(float(AveDev[i][0]))
    ADy.append(float(AveDev[i][1]))
    ADz.append(float(AveDev[i][2])) 



V = []                                   #АКФС 
Nak = 0
with open("akfs.txt") as f:
    for line in f:
        V.append(line.split())
        Nak = Nak + 1
AK = []
for i in range(Nak):
    AK.append(float(V[i][0]))




fig, (ax, bx, cx) = plt.subplots(1, 3)

ax.plot(range(Ne), E)
ax.set_xlabel('timesteps')
ax.set_ylabel('energy') 
ax.set_title("Full Energy")
plt.ylim(minY(E),maxY(E))

bx.plot(range(Ne), U)
bx.set_xlabel('timesteps')
bx.set_ylabel('energy')
bx.set_title("Potential Energy")
plt.ylim(minY(U),maxY(U))

cx.plot(range(Ne),K)
cx.set_xlabel('timesteps')
cx.set_ylabel('energy')
cx.set_title("Kinetic Energy")
plt.ylim(minY(K),maxY(K))




fig1, (px, py, pz) = plt.subplots(1, 3)

px.plot(range(Np), Px)
px.set_xlabel('timesteps')
px.set_ylabel('momentum') 
px.set_title("Momentum for X")
plt.ylim(minY(Px),maxY(Px))

py.plot(range(Np), Py)
py.set_xlabel('timesteps')
py.set_ylabel('momentum')
py.set_title("Momentum for Y")
plt.ylim(minY(Py),maxY(Py))

pz.plot(range(Np), Pz)
pz.set_xlabel('timesteps')
pz.set_ylabel('momentum')
pz.set_title("Momentum for z")
plt.ylim(minY(Pz),maxY(Pz))



fig2, (dx, dy, dz) = plt.subplots(1, 3)

dx.plot(range(Nd), ADx)
dx.set_xlabel('time')
dx.set_ylabel('destination') 
dx.set_title("Destination X")
plt.ylim(minY(ADx),maxY(ADx))

dy.plot(range(Nd), ADy)
dy.set_xlabel('time')
dy.set_ylabel('destination')
dy.set_title("Destination Y")
plt.ylim(minY(ADy),maxY(ADy))

dz.plot(range(Nd),ADz)
dz.set_xlabel('time')
dz.set_ylabel('destination')
dz.set_title("Destination Z")
plt.ylim(minY(ADz),maxY(ADz))


"""fig3, (ak) = plt.subplots()

ak.plot(range(Nak), AK)
ak.set_xlabel('time')
ak.set_ylabel('akfs') 
ak.set_title("AKFS")
plt.ylim(minY(AK),maxY(AK))"""



print(np.polyfit(range(Nd), ADx, 1))
D = 0
for i in range(Nak - 1):
    D = D + (AK[i] + AK[i+1])/2
print('D = ' + str(D/3))

plt.show()
