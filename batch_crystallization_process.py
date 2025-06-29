import numpy as np
import matplotlib.pyplot as plt

# Constants
kg = 0.1           # Growth rate constant (1/hr)
g = 1.5            # Growth order
C_sat = 100        # Saturation concentration (g/L)
C0 = 150           # Initial concentration (g/L)
rho = 1.2          # Density of crystal (g/cm³)
A = 50             # Specific surface area (cm²/L)
L0 = 10            # Initial average crystal size (microns)

# Time settings
t_final = 10       # Final time (hours)
dt = 0.01          # Time step (hours)
time = np.arange(0, t_final + dt, dt)

# Arrays for storing results
C = [C0]
L = [L0]

# Simulation loop
for t in time[:-1]:
    # Supersaturation
    S = (C[-1] - C_sat) / C_sat
    G = kg * S**g if S > 0 else 0

    # Update concentration
    dCdt = -rho * G * A
    C_next = C[-1] + dCdt * dt
    C.append(C_next)

    # Update crystal size
    L_next = L[-1] + G * dt
    L.append(L_next)

# Plot 1: Solute concentration vs time
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(time, C, color='blue', label='Concentration (g/L)')
plt.xlabel('Time (hr)')
plt.ylabel('Concentration (g/L)')
plt.title('Solute Concentration vs Time')
plt.grid(True)
plt.legend()

# Plot 2: Crystal size vs time
plt.subplot(1, 2, 2)
plt.plot(time, L, color='green', label='Crystal Size (μm)')
plt.xlabel('Time (hr)')
plt.ylabel('Crystal Size (μm)')
plt.title('Crystal Growth vs Time')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
