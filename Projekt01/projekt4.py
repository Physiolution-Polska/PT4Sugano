import numpy as np
import json
import matplotlib.pyplot as plt

input_file = open('input.dat')
input_str = input_file.read()
Param = json.loads(input_str)

time_exp=np.linspace(0, 48, 100)

const_exp1 = (Param['k_a1'] * Param['frac'] * Param['X0'] )/(Param['V_val'] * (Param['k_a1'] - Param['k_e']))
con_exp1 = const_exp1 * (np.exp(-Param['k_e']*time_exp) - np.exp(-Param['k_a1']*time_exp))
# print(time_exp, con_exp1)

const_exp2 = (Param['k_a2'] * (1-Param['frac']) * Param['X0'])/(Param['V_val'] * (Param['k_a2'] - Param['k_e']))
con_exp2 = np.piecewise(time_exp,[time_exp < Param['T_lag'], time_exp >= Param['T_lag']], [
            lambda time_exp: const_exp1 * (np.exp(-Param['k_e']*time_exp) - np.exp(-Param['k_a1']*time_exp)), 
            lambda time_exp: const_exp1 * (np.exp(-Param['k_e']*time_exp) - np.exp(-Param['k_a1']*time_exp))
            + const_exp2 * (np.exp(-Param['k_e']*(time_exp - Param['T_lag'])) - np.exp(-Param['k_a2']*(time_exp - Param['T_lag'])))])
# print(time_exp, con_exp2)


plt.plot(time_exp, con_exp1, '-o')
plt.plot(time_exp, con_exp2, '-x')

np.savetxt('data.csv', np.transpose([time_exp, con_exp1, con_exp2]), fmt='%4.2g', delimiter=';  ')

