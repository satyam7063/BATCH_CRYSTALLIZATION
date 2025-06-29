# Batch Crystallization Simulation

This project simulates batch crystallization of a solute from a supersaturated solution under isothermal conditions. It models how the solute concentration decreases over time and how the average crystal size increases due to crystal growth.

# Objective

- Simulate the depletion of solute concentration due to crystal growth in a batch crystallizer.
- Track and visualize the evolution of average crystal size over time.
- Understand the effect of supersaturation on crystallization kinetics.

# Background

Crystallization is a key separation and purification process in chemical industries. The simulation is based on:

- Supersaturation:  
  
  S = {C - C*}/{C*}
  

- Growth rate model:  
  
  G = k_g * S^g
  

- Concentration balance:  
  
  dC/dt = -ρ * G * A


- Crystal size evolution:  
 
  L = L_0 +  G * t

  where;
  C = concentration of solute
  C* = saturation concentration
  G = growth rate
  A = surface area of crystals per unit volume
  ρ = crystal density
  k_g = growth rate constant
  g = order of growth
  

# Features

- Models solute concentration and average crystal size over time.
- Adjustable growth kinetics parameters.
- Generates clear plots for visualization.

# Requirements

- Python 3.x
- NumPy
- Matplotlib

Install required packages with:

```bash
pip install numpy matplotlib
