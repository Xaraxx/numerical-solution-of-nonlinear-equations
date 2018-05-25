#this code is for solve a set to non-linear equations for find the optimal longitude 

import numpy as np
import math
from scipy.optimize import fsolve

#this are constant values in the equations 
#I must to write a help for this program!!! some indication for the use 

d  = 0.05;
h  = 20.0;
Tb = 473.0;
Tl = 273.1;
Tinf = 298;


k_Al = 237.0;
k_Cr = 93.7; 
k_Cu = 401.0; 
k_ss = 15.1; 
k_Fe = 80.2;
k_Ni = 90.7; 
k_Ag = 429.0;
k_Zn = 116.0;


Ac = (1.0/4.0)*np.pi*d**2;
p  = np.pi*d;


m_Al  = np.sqrt((h*p)/(k_Al*Ac))
m_Cr  = np.sqrt((h*p)/(k_Cr*Ac))
m_Cu  = np.sqrt((h*p)/(k_Cu*Ac))
m_ss  = np.sqrt((h*p)/(k_ss*Ac))
m_Fe  = np.sqrt((h*p)/(k_Fe*Ac))
m_Ni  = np.sqrt((h*p)/(k_Ni*Ac))
m_Ag  = np.sqrt((h*p)/(k_Ag*Ac))
m_Zn  = np.sqrt((h*p)/(k_Zn*Ac))



#General function : ((np.cosh(m_**L)-((Tl - Tinf)/(Tb - Tinf)))/np.sinh(m_**L)) - 1

L1 = 1
L2 = 1
L3 = 1
L4 = 1
L5 = 1
L6 = 1
L7 = 1
L8 = 1


L1_guess = 1
L2_guess = 1
L3_guess = 1
L4_guess = 1
L5_guess = 1
L6_guess = 1
L7_guess = 1
L8_guess = 1

p = (L1, L2, L3, L4, L5, L6, L7, L8)


def equations(p):
    L1, L2, L3, L4, L5, L6, L7, L8 = p
    f1 = ((np.cosh(m_Al*L1)-((Tl - Tinf)/(Tb - Tinf)))/np.sinh(m_Al*L1)) - 1 
    f2 = ((np.cosh(m_Cr*L2)-((Tl - Tinf)/(Tb - Tinf)))/np.sinh(m_Cr*L2)) - 1
    f3 = ((np.cosh(m_Cu*L3)-((Tl - Tinf)/(Tb - Tinf)))/np.sinh(m_Cu*L3)) - 1
    f4 = ((np.cosh(m_ss*L4)-((Tl - Tinf)/(Tb - Tinf)))/np.sinh(m_ss*L4)) - 1
    f5 = ((np.cosh(m_Fe*L5)-((Tl - Tinf)/(Tb - Tinf)))/np.sinh(m_Fe*L5)) - 1
    f6 = ((np.cosh(m_Ni*L6)-((Tl - Tinf)/(Tb - Tinf)))/np.sinh(m_Ni*L6)) - 1
    f7 = ((np.cosh(m_Ag*L7)-((Tl - Tinf)/(Tb - Tinf)))/np.sinh(m_Ag*L7)) - 1
    f8 = ((np.cosh(m_Zn*L8)-((Tl - Tinf)/(Tb - Tinf)))/np.sinh(m_Zn*L8)) - 1
    return(f1, f2, f3, f4, f5, f6, f7, f8) 

L1,L2,L3,L4,L5,L6,L7,L8 = fsolve (equations, (L1_guess, L2_guess, L3_guess, L4_guess, L5_guess, L6_guess, L7_guess, L8_guess)) 

print("L1 = ", L1, "L2 = ", L2, "L3 = ", L3, "L4 = ", L4, "L5 = ", L5, "L6 = ", L6, "L7 = ", L7, "L8 = ", L8)

L  = np.vstack((L1, L2, L3, L4, L5, L6, L7, L8))  

np.savetxt("Long.dat", L) 
