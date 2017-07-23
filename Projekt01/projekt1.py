import numpy as np
import matplotlib.pyplot as plt

print("Hallo, im first PhysioCode")

Parameters = {"k_e":"0.0888","k_a1":"7.6226","frac":"0.5147","X0":"1.0","V_val":"1.0","T_lag":"10","k_a2":"1.0588"}


#k_e=0.0888
#k_a1=7.6226
#frac = 0.5147
#X0 = 1.0
#V_val = 1.0
#T_lag = 2.2862
#T_lag = 10
#k_a2 = 1.0588

time_exp=np.arange(24, dtype=float)

for i in time_exp:
    if time_exp[i] < T_lag:
        const_exp1 = (k_a1 * frac * X0 )/(V_val * (k_a1 - k_e))
        con_exp1 = const_exp1 * (np.exp(-k_e*time_exp) - np.exp(-k_a1*time_exp))
#        print(i,time_exp[i], T_lag)

    else:
        const_exp2 = (k_a2 * (1-frac) * X0)/(V_val * (k_a2 - k_e))
        con_exp2 = con_exp1 + const_exp2 * (np.exp(-k_e*(time_exp - T_lag)) - np.exp(-k_a2*(time_exp - T_lag)))
#        print('xxx ',i,time_exp[i], T_lag)


plt.plot(time_exp, con_exp1)
plt.plot(time_exp, con_exp2)

print(con_exp1)
print(con_exp2)


