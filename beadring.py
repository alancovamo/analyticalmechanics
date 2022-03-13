# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 19:39:06 2022

@author: alan
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from vpython import *




def F(Y,t,m,g,r,omega):
    x1=Y[0]
    x2=Y[1]
    dx1=x2
    dx2=np.sin(x1)*(omega**2*np.cos(x1)-g/(r))
    return [dx1,dx2]

############parametros
m=1
g=9.81
r=0.1
omega=40*2*np.pi

###############
Y0=[np.pi/4,0]

t=np.linspace(0,10,100000)

Y=odeint(F,Y0,t,args=(m,g,r,omega))

beta=Y[:,0] #beta=beta(t)

R=[r*np.cos(omega*t)*np.sin(beta),r*np.sin(omega*t)*np.sin(beta),r*np.cos(beta)] #vector posicion

##############################################


bead=sphere(pos=vector(R[0][0],R[1][0],R[2][0]),radius=0.001,color=color.green,
            make_trail=True,trail_type="curve",interval=1, retain=50)

esfera=sphere(pos=vector(0,0,0),radius=r,color=color.blue,opacity=0.1)
anillo=ring(pos=vector(0,0,0),axis=vector(0,1,0),radius=r, color=color.red,thickness=0.001)
z=arrow(pos=vector(0,0,0), axis=vector(0,0,2*r),shaftwidth=0.01)

graf=graph(xtitle='t',ytitle="beta")
bt=gcurve(color=color.blue,dot=True)

for i in range(1,len(t)):
    #calculos por segundo
    rate(2000)
    anillo.rotate(angle=omega*10/len(t),axis=vec(0,0,1))
    bead.pos=vector(R[0][i],R[1][i],R[2][i])
    bt.plot(t[i],beta[i])
    


    

