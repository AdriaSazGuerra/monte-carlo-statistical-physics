# Monte Carlo & Statistical Physics

Python simulations developed for undergraduate thermodynamics and statistical mechanics coursework.

## 1. Hard-sphere gas

Starting from the VPython `HardSphereGas` demonstration, the model was extended and analysed for **500 particles**. The coursework modifications include:

- robust non-overlapping particle initialisation and collision handling
- an **Andersen thermostat** at **T = 300 K**
- comparison of simulated speed and kinetic-energy distributions with Maxwell–Boltzmann predictions
- an external gravitational field and tests of the expected vertical velocity and barometric position distributions

### Files

- `hard_sphere_q1_radius_study.py` — numerical stability and atom-radius study
- `hard_sphere_q2_andersen_thermostat.py` — canonical-ensemble dynamics with Andersen thermostat
- `hard_sphere_q3_gravity.py` — thermostat plus gravitational field

## 2. Three-level Metropolis model

A separate Monte Carlo model simulates **N independent particles in three energy levels** using Metropolis updates. For the main study, the simulation uses **N = 1,000**, **120,000 Metropolis steps**, a **20,000-step burn-in**, and sampling every **50 steps** (about **2,000 equilibrium samples per temperature**).

The simulation compares equilibrium populations with Boltzmann theory, identifies a characteristic temperature around **105 K**, and tests the finite-size scaling of relative energy fluctuations against the theoretical `N^(-1/2)` law.

`three_level_metropolis.py` is a cleaned reconstruction of the full code included in the submitted report appendix.

## Tools

Python, NumPy, Matplotlib, VPython, Monte Carlo / Metropolis sampling, statistical mechanics

## Attribution

The hard-sphere implementation is based on the VPython demonstration by **Bruce Sherwood** and was substantially modified for the coursework. The portfolio organisation, analysis and additional simulation code are by **Adrià Saz Guerra**.
