import numpy as np
import json
import csv
import matplotlib.pyplot as plt

print("Hallo, im first PhysioCode")

input_file = open('input.dat')
input_str = input_file.read()
Parameter = json.loads(input_str)

print(Parameter)
#Parameter = {"k_e":0.0888,"k_a1":7.6226,"frac":0.5147,"X0":1.0,"V_val":1.0,"T_lag":10,"k_a2":1.0588}


k_e = Parameter['k_e']
k_a1=Parameter['k_a1']
frac = Parameter['frac']
X0 = Parameter['X0']
V_val = Parameter['V_val']
T_lag = Parameter['T_lag']
#T_lag = 10
k_a2 = Parameter['k_a2']

time_exp=np.arange(50, dtype=float)
print(time_exp)
#for i in time_exp:
#    if time_exp[i] < T_lag:
const_exp1 = (k_a1 * frac * X0 )/(V_val * (k_a1 - k_e))
con_exp1 = const_exp1 * (np.exp(-k_e*time_exp) - np.exp(-k_a1*time_exp))
#        print(i,time_exp[i], T_lag)

#   else:
con_exp2 = con_exp1
const_exp2 = (k_a2 * (1-frac) * X0)/(V_val * (k_a2 - k_e))
#con_exp2[time_exp > T_lag] = const_exp2 * (np.exp(-k_e*(time_exp - T_lag)) - np.exp(-k_a2*(time_exp - T_lag)))
for i in range(T_lag, 50):
    con_exp2[i] = con_exp2[i] + const_exp2 * (np.exp(-k_e*(time_exp[i] - T_lag)) - np.exp(-k_a2*(time_exp[i] - T_lag)))
#        print('xxx ',i,time_exp[i], T_lag)


plt.plot(time_exp, con_exp1)
plt.plot(time_exp, con_exp2)

with open("data.csv", "wb") as output_file:
    writer = csv.writer(output_file, delimiter=';', lineterminator='\n')
with open("data.csv", "r") as output_file:
    for line in output_file:
        print(time_exp[line])
#    writer.writerows(time_exp) 
#    writer.writerows(con_exp2) 
#    writer.writerows(con_exp1) 


# print(con_exp1)
# print(con_exp2)


