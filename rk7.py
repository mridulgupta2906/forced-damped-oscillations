

from cmath import sqrt
import math
import matplotlib.pyplot as plt
import numpy as np


# b = variable damping magnitude        [0<b<sqrt(a)]
# c = variable Fext magnitude 

# b=0 , c=0  [ no damping, no Fext ]  => constant shm oscillations
# only c=0   [ no fext ]              => damping present so oscillations will decrease and type of damping will depend on b*b <> 4km

m=1
a=10
b=0.01
c=1
w1=math.sqrt(100)
def helper(t,y,z):
    dydt=z
    return dydt

def helper3(t,y,z):
    f=math.cos(w1*t)
    #print(-a*y-b*z," <> ",c*f)
    dzdt=(-a*y-b*z+c*f)/m
    return dzdt

def rk4(k,t0,t1,y0,z0):
    h=abs(t1-t0)/k
    i=1
    xaxis=[]
    yaxis=[]
    y1axis=[]
    xaxis.append(t0)
    y1axis.append(y0)
    yaxis.append(z0)
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
    
    with open('t_axis.txt', 'wb') as f:
        for item in xaxis:
          itemstring=f'{item}'+'\n'  
          ascii = itemstring.encode(encoding="ascii")
          f.write(ascii)
          

    with open('y1_axis.txt', 'wb') as f:
        for item in y1axis:
            itemstring=f'{item}'+'\n'  
            ascii = itemstring.encode(encoding="ascii")
            f.write(ascii)
            

    with open('y_axis.txt', 'wb') as f:
       for item in yaxis:
           itemstring=f'{item}'+'\n'  
           ascii = itemstring.encode(encoding="ascii") 
           f.write(ascii)
          

    
    plt.plot(xaxis,y1axis,'b-',label='y(t)')
    plt.plot(xaxis,yaxis,'r-',label='z(t)')
    plt.legend(loc='best')
    plt.show()
    
    fourierTransform = np.fft.fft(y1axis)/len(y1axis)           # Normalize amplitude
    fourierTransform = fourierTransform[range(int(len(y1axis)/2))] # Exclude sampling frequency

 
    tpCount     = len(y1axis)
    values      = np.arange(int(tpCount/2))
    timePeriod  = tpCount/k
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


rk4(1000000,0,30,5,0)

