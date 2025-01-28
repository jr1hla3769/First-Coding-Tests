import matplotlib.pyplot as plt
import numpy as np

# Basic simulation properties
dt  = 10E-6;  # 10 us timestep

# Basic cell properties
Cm = 100E-12; # Membrane capacitance = 100 pF
v_init = -70E-3; # Initial membrane potential = -70 mV
Gk = 5E-9 # 5nS conductance
Ek = -90E-3 # Reversal potential = -90 mV

current_magnitude = 100E-12; # 100 pA

i_inj = np.concatenate((np.zeros([round(0.2/dt), 1]),
                         current_magnitude * np.ones([round(0.3/dt), 1]),
                         np.zeros([round(0.5/dt), 1])) )

v_out = np.zeros(np.size(i_inj))

for t in range(np.size(v_out)):
    if t == 1:
        v_out[t] = v_init;
    else:
      i_ion = Gk * (v_out[t-1] - Ek)
      i_cap = i_inj[t] - i_ion
      dv = i_cap/Cm * dt;
      v_out[t] = v_out[t-1] + dv;

# Now to chart this neuron, by creating a graph
t_vec = np.linspace(0, 1, np.size(v_out))
plt.plot(t_vec, v_out)
plt.xlabel('Time (s)')
plt.ylabel(' Membrane potential (V)')
plt.title('First Neuronal Model')
plt.show()

