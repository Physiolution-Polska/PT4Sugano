# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 03:32:34 2017

@author: MayaK
"""

print ('Physiolution MAS funkcja do optymizacji')
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import differential_evolution

#k_e=0.0888
#k_a1=7.6226
#frac = 0.5147
#X0 = 1.0
#V_val = 86.7
#T_lag = 2.2862
#T_lag = 10
#k_a2 = 1.0588

time_exp= np.array([0.06, 0.125, 0.25, 0.42, 0.6, 0.75, 0.95, 1.125, 1.45, 2., 3., 4., 5., 6., 7., 12., 24.])
con_exp2= np.array([25., 36., 42., 48, 46.2, 47., 46., 44.5, 45., 42., 63., 70., 72., 65., 55., 39., 14.])

Xst= np.array([1.2, 0.9, 0.1, 1.5, 2. ,3.,4.])

def SSEcon (Xop):
    const_theor1 = (Xop[0] * Xop[1] * Xop[5] )/(Xop[6] * (Xop[0] - Xop[2]))
    con_theor1 = const_theor1 * (np.exp(-Xop[2]*time_exp) - np.exp(-Xop[0]*time_exp))
    const_theor2 = (Xop[4] * (1-Xop[1]) * Xop[5])/(Xop[6] * (Xop[4] - Xop[2]))
    con_theor2 = con_theor1 + (time_exp>Xop[3])* (const_theor2 * (np.exp(-Xop[2]*(time_exp - Xop[3])) - np.exp(-Xop[4]*(time_exp - Xop[3]))))
    #print('xxx ',time_exp, T_lag)
    return sum((con_exp2-con_theor2)**2)
    
    #print("SSEcon=", SSEcon)
    #print('xxxxxxxxxxxxxx',end='\n')
    #print('k_a1=', Xop[0])
    #print('frac=', Xop[1])
    #print('k_e=', Xop[2])
    #print('T_lag=', Xop[3])
    #print('k_a2=', Xop[4])
    # print('X0=', Xop[5])
    # print('V_val', Xop[6])
    

SSEcon(Xst)
bounds=[(0.1, 15.0), (0.0, 2.0), (0.0, 2.0), (0.0, 5.), (2.0, 5.),(0.,100.),(0.,100.)]
result = differential_evolution(SSEcon, bounds)
Xop=result.x

const_theor3 = (Xop[0] * Xop[1] * Xop[5] )/(Xop[6] * (Xop[0] - Xop[2]))
con_theor3 = const_theor3 * (np.exp(-Xop[2]*time_exp) - np.exp(-Xop[0]*time_exp))
const_theor4 = (Xop[4] * (1-Xop[1]) * Xop[5])/(Xop[6] * (Xop[4] - Xop[2]))
con_theor4 = con_theor3 + (time_exp>Xop[3])* (const_theor4 * (np.exp(-Xop[2]*(time_exp - Xop[3])) - np.exp(-Xop[4]*(time_exp - Xop[3]))))

plt.plot(time_exp, con_exp2,'-o')
plt.plot(time_exp, con_theor4)

print("SSEcon=", SSEcon(Xop))
print('xxxxxxxxxxxxxx',end='\n')
print('k_a1=', Xop[0])
print('frac=', Xop[1])
print('k_e=', Xop[2])
print('T_lag=', Xop[3])
print('k_a2=', Xop[4])
print('X0=', Xop[5])
print('V_val', Xop[6])