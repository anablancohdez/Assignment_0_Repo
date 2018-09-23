# -*- coding: utf-8 -*-
h=0.8 #glass window high (m)
w=1.5 #glass window wide (m)
L=0.008 #glass window long (m)
h1=10 #convention coef (W/m2ºC)
h2=40 #convention coef (W/m2ºC)
k=0.78 #thermal conductivity (W/mºC)
Tinf1=20 #temperature (ºC)
Tinf2=-10 #temperature (ºC)
A=h*w #glass window area (m2)
R_cond=L/(k*A)
R_conv1=1/(h1*A)
R_conv2=1/(h2*A)
R_total=R_cond+R_conv1+R_conv2
Q=(Tinf1-Tinf2)/R_total #steady rate of heat transfer (W)
T1=Tinf1-Q/(h1*A) #temperature inner surface (ºC)
print("The internal convection resistance is " +str(R_conv1))
print("The external convection resistance is " +str(R_conv2))
print("The glasse's conductive resistance is " +str(R_cond))
print("The steady rate of heat transfer through the glass, in Watts, is Q= " +str(Q))
print("The temperature of the glass' inner surface, in ºC, is T= " +str(T1))