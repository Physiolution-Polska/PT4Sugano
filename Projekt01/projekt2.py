import numpy as np
import json
#import csv
import matplotlib.pyplot as plt

print("Hallo, im first PhysioCode")

input_file = open('input.dat')
input_str = input_file.read()
Parameter = json.loads(input_str)

print(Parameter)

k_e = Parameter['k_e']
k_a1= Parameter['k_a1']
frac = Parameter['frac']
X0 = Parameter['X0']
V_val = Parameter['V_val']
T_lag = Parameter['T_lag']
k_a2 = Parameter['k_a2']

time_exp=np.linspace(0, 48, 100)

const_exp1 = (k_a1 * frac * X0 )/(V_val * (k_a1 - k_e))
con_exp1 = const_exp1 * (np.exp(-k_e*time_exp) - np.exp(-k_a1*time_exp))
# print(time_exp, con_exp1)

const_exp2 = (k_a2 * (1-frac) * X0)/(V_val * (k_a2 - k_e))
con_exp2 = np.piecewise(time_exp,[time_exp < T_lag, time_exp >= T_lag], [lambda time_exp: const_exp1 * (np.exp(-k_e*time_exp) - np.exp(-k_a1*time_exp)), lambda time_exp: const_exp1 * (np.exp(-k_e*time_exp) - np.exp(-k_a1*time_exp))+ const_exp2 * (np.exp(-k_e*(time_exp - T_lag)) - np.exp(-k_a2*(time_exp - T_lag)))])
# print(time_exp, con_exp2)


plt.plot(time_exp, con_exp1, '-o')
plt.plot(time_exp, con_exp2, '-x')

#druk = np.asarray([time_exp, con_exp1, con_exp2])
#np.savetxt("newdata.csv", druk, delimiter=",")
np.savetxt('data.csv', np.transpose([time_exp, con_exp1, con_exp2]), fmt='%4.2g', delimiter=';  ')

#with open("data.csv", "w") as output_file:
#     twriter = csv.writer(output_file, dialect='excel', delimiter=';', lineterminator='\n')
#     twriter.writerows(zip(time_exp, con_exp1, con_exp2)) 

