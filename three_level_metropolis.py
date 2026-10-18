import os
import numpy as np
import matplotlib.pyplot as plt

# Three-level independent-particle system simulated with Metropolis dynamics.
# Public portfolio reconstruction from the code appendix of the submitted report.
# Adrià Saz Guerra

EPSILON = 1.0e-21
KB = 1.380649e-23
ENERGIES = np.array([0.0, EPSILON, 10.0 * EPSILON])
N_STEPS = 120_000
BURN_IN = 20_000
SAMPLE_EVERY = 50
OUTPUT_DIR = "figures_simulation"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def critical_temperature(n, epsilon=EPSILON, kb=KB):
    return 10.0 * epsilon / (kb * np.log(n))


def initialise_states(n):
    return np.random.choice([0, 1, 2], size=n, p=[1 / 3, 1 / 3, 1 / 3])


def metropolis_step(states, beta):
    i = np.random.randint(len(states))
    current = states[i]
    candidates = [0, 1, 2]
    candidates.remove(current)
    proposal = np.random.choice(candidates)
    delta_e = ENERGIES[proposal] - ENERGIES[current]
    if delta_e <= 0 or np.random.rand() < np.exp(-beta * delta_e):
        states[i] = proposal


def observables(states):
    total_energy = np.sum(ENERGIES[states])
    counts = np.bincount(states, minlength=3)
    populations = counts / len(states)
    return total_energy, populations


def theoretical_populations(beta):
    weights = np.exp(-beta * ENERGIES)
    return weights / weights.sum()


def simulate(n, temperature, n_steps=N_STEPS, burn_in=BURN_IN, sample_every=SAMPLE_EVERY):
    beta = 1.0 / (KB * temperature)
    states = initialise_states(n)
    energies = []
    populations = []
    for step in range(n_steps):
        metropolis_step(states, beta)
        if step >= burn_in and step % sample_every == 0:
            energy, population = observables(states)
            energies.append(energy)
            populations.append(population)
    return np.asarray(energies), np.asarray(populations)


def fluctuation_scaling(temperatures, n_values=(50, 100, 300, 1000)):
    results = {}
    n_values = np.asarray(n_values)
    for temperature in temperatures:
        relative = []
        for n in n_values:
            energy, _ = simulate(int(n), temperature)
            relative.append(np.std(energy, ddof=1) / np.mean(energy))
        relative = np.asarray(relative)
        slope, intercept = np.polyfit(np.log(n_values), np.log(relative), 1)
        fitted = intercept + slope * np.log(n_values)
        ss_res = np.sum((np.log(relative) - fitted) ** 2)
        ss_tot = np.sum((np.log(relative) - np.mean(np.log(relative))) ** 2)
        r2 = 1 - ss_res / ss_tot
        results[temperature] = {
            "relative_fluctuations": relative,
            "slope": slope,
            "r2": r2,
        }
    return results


def main():
    n = 1000
    tc = critical_temperature(n)
    temperatures = [20.0, float(int(tc)), 300.0, 20_000.0]
    print(f"Critical temperature for N={n}: {tc:.3f} K")

    all_results = {}
    for temperature in temperatures:
        energy, populations = simulate(n, temperature)
        all_results[temperature] = (energy, populations)
        p_mean = populations.mean(axis=0)
        p_theory = theoretical_populations(1.0 / (KB * temperature))
        print(
            f"T={temperature:8.1f} K | "
            f"simulated populations={p_mean} | theory={p_theory}"
        )

    # Equilibrium populations: theory vs simulation
    t_grid = np.logspace(0, 4.5, 500)
    theory = np.array(
        [theoretical_populations(1.0 / (KB * temperature)) for temperature in t_grid]
    )
    plt.figure(figsize=(9, 5))
    for i, label in enumerate(["p1", "p2", "p3"]):
        plt.semilogx(t_grid, theory[:, i], label=f"{label} theory")
        points = [all_results[t][1][:, i].mean() for t in temperatures]
        plt.scatter(temperatures, points, s=40, edgecolor="black")
    plt.axvline(tc, linestyle=":", label=f"Tc = {tc:.1f} K")
    plt.xlabel("Temperature (K)")
    plt.ylabel("Population probability")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(
        os.path.join(OUTPUT_DIR, "populations_theory_vs_simulation.png"), dpi=300
    )
    plt.close()

    # Relative energy-fluctuation scaling
    n_values = np.array([50, 100, 300, 1000])
    scaling = fluctuation_scaling(temperatures, n_values)
    plt.figure(figsize=(8.5, 5))
    for temperature, result in scaling.items():
        relative = result["relative_fluctuations"]
        plt.loglog(
            n_values,
            relative,
            "o-",
            label=f"T={temperature:g} K, b={result['slope']:.3f}",
        )
        print(
            f"T={temperature:g} K: "
            f"slope={result['slope']:.4f}, R^2={result['r2']:.4f}"
        )

    reference = next(iter(scaling.values()))["relative_fluctuations"]
    plt.loglog(
        n_values,
        reference[0] * np.sqrt(n_values[0] / n_values),
        "--",
        label="N^(-1/2) reference",
    )
    plt.xlabel("N")
    plt.ylabel("std(E) / <E>")
    plt.grid(True, which="both")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "relative_fluctuations.png"), dpi=300)
    plt.close()


if __name__ == "__main__":
    main()
