


import math
from tkinter import W
import matplotlib.pyplot as plt
a=10
b=0
c=10
w1=1
def helper(t,y,z):
    dydt=z
    return dydt

def helper3(t,y,z):
    dzdt=-a*y-b*z+c*math.cos(w1*t)
    return dzdt

def rk4(k,t0,t1,y0,z0):
    h=abs(t1-t0)/k
    i=1
    ymax=y0
    zmax=z0
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
        k1=h*helper3(t0,y0,z0)
        k2=h*helper3(t0+(0.5*h),y0,z0+(0.5*k1))
        k3=h*helper3(t0+(0.5*h),y0,z0+(0.5*k2))
        k4=h*helper3(t0+h,y0,z0+k3)
        zt=z0+(1.0/6.0)*(k1+2*k2+2*k3+k4)
        #
        xaxis.append(tt)
        y1axis.append(yt)
        yaxis.append(zt)
        ymax=max(ymax,yt)
        zmax=max(zmax,zt)
        y0=yt
        t0=tt
        z0=zt
        i=i+1
    
   # with open('t_atis', 'w') as f:
    #    for item in tatis:
     #       f.write("%s\n" % item)

   # with open('y_atis', 'w') as f:
    #    for item in y1atis:
    #        f.write("%s\n" % item)

   ## with open('z_atis', 'w') as f:
   #     for item in yatis:
     #       f.write("%s\n" % item)
    
    print(ymax," <> ",zmax)
    print(-ymax*a-zmax*b)
    
    plt.plot(xaxis,y1axis,'b-',label='y(t)')
    plt.plot(xaxis,yaxis,'r-',label='z(t)')
    plt.legend(loc='best')
    plt.show()
    #plt.plot(yaxis,y1axis)
    #plt.show()

if b*b==4*a*1:
    print("critical damping") 
rk4(1000000,0,50,5,0)
print(b*b)
print(4*a*1)
