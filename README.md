# Monte Carlo & Statistical Physics

Simulation project covering a hard-sphere gas, an interacting Lennard–Jones fluid and a three-level Metropolis model.

## Full report

**[Open the complete report in GitHub's PDF viewer](report/Statistical_Physics_Simulation_Report.pdf)**

The public PDF preserves the submitted report and figures, with personal identifiers privacy-masked.

## Code

The repository is organized question by question. For the first three questions, the files are the original source files supplied for the coursework; the remaining code is reconstructed from the submitted report and appendix, without inventing unavailable raw simulation trajectories.

| Question | File | Status |
|---|---|---|
| Baseline | [`code/HardSphereGas_Original.py`](code/HardSphereGas_Original.py) | Original supplied file |
| Q1 | [`code/HardSphereGas_Q1.py`](code/HardSphereGas_Q1.py) | Original supplied file |
| Q2 | [`code/HardSphereGas_Q2.py`](code/HardSphereGas_Q2.py) | Original supplied file |
| Q3 | [`code/HardSphereGas_Q3.py`](code/HardSphereGas_Q3.py) | Original supplied file |
| Q4 | [`code/Q4_lennard_jones_stationary_states.py`](code/Q4_lennard_jones_stationary_states.py) | Reconstructed from the report's equations and reported state data |
| Q5 | [`code/Q5_isothermal_compressibility.py`](code/Q5_isothermal_compressibility.py) | Reconstructed from the report's V(P) tables and analysis |
| Q6 | [`code/Q6_three_level_metropolis_core.py`](code/Q6_three_level_metropolis_core.py) | Reconstructed Metropolis core from Section 3.2 and Appendix A |
| Q7 | [`code/Q7_level_occupations.py`](code/Q7_level_occupations.py) | Reconstructed level-occupation analysis from Section 3.3 and Appendix A |
| Q8 | [`code/Q8_energy_fluctuations.py`](code/Q8_energy_fluctuations.py) | Reconstructed finite-size fluctuation analysis from Section 3.4 and Appendix A |

For Q4–Q5 the original source files were not available separately, so the reconstruction is deliberately limited to the methods, equations and numerical data that are actually documented in the report.

## Figures from the submitted report

The images below are direct crops from the original PDF rather than regenerated approximations.

### Andersen thermostat — energy distribution

![Andersen thermostat](assets/stat_fig7_andersen_thermostat.jpg)

### Lennard–Jones: supercooled liquid at T = 0.2

![Lennard Jones](assets/stat_fig15_lennard_jones.jpg)

### NPT isotherms and isothermal compressibility

![Isotherms](assets/stat_fig17_isotherms.jpg)

### Three-level probabilities

![Level probabilities](assets/stat_fig27_level_probabilities.jpg)

### Finite-size energy-fluctuation scaling

![Energy fluctuation scaling](assets/stat_fig28_fluctuation_scaling.jpg)

## Main methods

Metropolis Monte Carlo, canonical and isothermal–isobaric ensembles, Andersen thermostat, Maxwell–Boltzmann statistics, radial distribution functions, Widom insertion, Lennard–Jones interactions, finite-size scaling and equilibrium statistical mechanics.

---
<sub>Public portfolio copy: original coursework completed collaboratively; collaborator names are anonymized and the student identifier is masked.</sub>
