

from cmath import sqrt
import math
import matplotlib.pyplot as plt
import numpy as np
from decimal import *

# b = variable damping magnitude        [0<b<sqrt(a)]
# c = variable Fext magnitude 

# b=0 , c=0  [ no damping, no Fext ]  => constant shm oscillations
# only c=0   [ no fext ]              => damping present so oscillations will decrease and type of damping will depend on b*b <> 4km

m=1
a=30
b=0
c=5
w1=math.sqrt(25)
def helper(t,y,z):
    dydt=z
    return dydt

def helper3(t,y,z):
    f=np.sin(w1*t)+2*np.cos(3.2*t)
    #print(-a*y-b*z," <> ",c*f)
    #naturalW=a*Decimal(y)
    dzdt=(-a*y-b*z+c*f)
    return dzdt

def rk4(h,t0,t1,y0,z0):
    #h=abs(t1-t0)/k

    yaxis=[]        # DISPLACEMENT
    zaxis=[]        # VELOCITY
    t=t0
    xaxis= np.arange(t0, t1, h)
    for x in xaxis:
        if x==t0:
            yaxis.append(y0)
            zaxis.append(z0)
            continue
        k1=h*helper(t,y0,z0)
        k2=h*helper(t+(0.5*h),y0+(0.5*k1),z0)
        k3=h*helper(t+(0.5*h),y0+(0.5*k2),z0)
        k4=h*helper(t+h,y0+k3,z0)
        yt=y0+(1.0/6.0)*(k1+2*k2+2*k3+k4)
        #
        k5=h*helper3(t,y0,z0)
        k6=h*helper3(t+(0.5*h),y0,z0+(0.5*k5))
        k7=h*helper3(t+(0.5*h),y0,z0+(0.5*k6))
        k8=h*helper3(t+h,y0,z0+k7)
        zt=z0+(1.0/6.0)*(k5+2*k6+2*k7+k8)
        #

        yaxis.append(yt)
        #y1axis.append(math.sqrt(yt*np.conjugate(yt)))
        zaxis.append(zt)
        y0=yt
        z0=zt
        t=x
    

    with open('time_axis.txt', 'wb') as f:
        for item in xaxis:
          itemstring=f'{item}'+'\n'  
          ascii = itemstring.encode(encoding="ascii")
          f.write(ascii)
          

    with open('displcaement_axis.txt', 'wb') as f:
        for item in yaxis:
            itemstring=f'{item}'+'\n'  
            ascii = itemstring.encode(encoding="ascii")
            f.write(ascii)
            

    with open('velocity_axis.txt', 'wb') as f:
       for item in zaxis:
           itemstring=f'{item}'+'\n'  
           ascii = itemstring.encode(encoding="ascii") 
           f.write(ascii)

    '''
    while(i<k+1):
        tt=t0+h
        k1=h*helper(t0,y0,z0)
        k2=h*helper(t0+(0.5*h),y0+(0.5*k1),z0)
        k3=h*helper(t0+(0.5*h),y0+(0.5*k2),z0)
        k4=h*helper(t0+h,y0+k3,z0)
        yt=y0+(1.0/6.0)*(k1+2*k2+2*k3+k4)
        #
        k5=h*helper3(t0,y0,z0)
        k6=h*helper3(t0+(0.5*h),y0,z0+(0.5*k5))
        k7=h*helper3(t0+(0.5*h),y0,z0+(0.5*k6))
        k8=h*helper3(t0+h,y0,z0+k7)
        zt=z0+(1.0/6.0)*(k5+2*k6+2*k7+k8)
        #
        xaxis.append(tt)
        y1axis.append(yt)
        yaxis.append(zt)
        y0=yt
        t0=tt
        z0=zt
        i=i+1
          
    '''
    
    plt.plot(xaxis,yaxis,'b-',label='y(t)')
    plt.plot(xaxis,zaxis,'r-',label='z(t)')
    plt.legend(loc='best')
    plt.show()
    

    # At what intervals time points are sampled
    samplingInterval       = h
    # How many time points are needed i,e., Sampling Frequency
    samplingFrequency   = 1/samplingInterval

    fourierTransform = np.fft.fft(zaxis)/len(zaxis)           # Normalize amplitude
    fourierTransform = fourierTransform[range(int(len(zaxis)/2))] # Exclude sampling frequency
    
    


    with open('fourire.txt', 'wb') as f:
       for item in fourierTransform:
           itemstring=f'{item}'+'\n'  
           ascii = itemstring.encode(encoding="ascii") 
           f.write(ascii)
    
    with open('fourireabsolute.txt', 'wb') as f:
       for item in fourierTransform:
           itemstring=f'{abs(item)}'+'\n'  
           ascii = itemstring.encode(encoding="ascii") 
           f.write(ascii)
 
    tpCount     = len(zaxis)
    values      = np.arange(int(tpCount/2))
    timePeriod  = tpCount/samplingFrequency
    frequencies = values/timePeriod
    plt.plot(frequencies, abs(fourierTransform))
    
    plt.show()
    
    #plt.plot(yaxis,y1axis)
    #plt.show()

print(w1)
if w1==math.sqrt(a) and c!=0 :
    print(" RESONANCE ")

if b*b==0 : 
    print(" SHM continous infinite OSCILLATIONS ")
elif b*b==4*a*m:
    print(" Critical Damping ")
elif b*b<4*a*m:
    print(" Under Damping  ")
elif b*b>4*a*m:
    print(" Over Damping ")


rk4(0.001,0,100,5,0)

