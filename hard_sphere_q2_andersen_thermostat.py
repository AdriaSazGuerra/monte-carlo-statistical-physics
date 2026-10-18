"""Q2 — hard-sphere gas with an Andersen thermostat.

Adrià Saz Guerra
Public portfolio refactor of the coursework implementation.
The collision engine follows the VPython HardSphereGas demonstration by
Bruce Sherwood; the thermostat, diagnostics and analysis were added for
the statistical-mechanics project.
"""

from math import exp, pi, sqrt
import random
import numpy as np

N_ATOMS = 500
L = 1.0
R_ATOM = 0.025
MASS = 4e-3 / 6e23
KB = 1.4e-23
T = 300.0
DT = 1e-5
NU = 5e2
THERMOSTAT_PROBABILITY = 1.0 - exp(-NU * DT)
SIGMA_P = sqrt(MASS * KB * T)


def draw_thermal_momentum(rng=random):
    """Draw p=(px,py,pz) from the canonical Maxwell distribution."""
    return np.array(
        [
            rng.gauss(0.0, SIGMA_P),
            rng.gauss(0.0, SIGMA_P),
            rng.gauss(0.0, SIGMA_P),
        ],
        dtype=float,
    )


def andersen_step(momentum, rng=random):
    """Apply one Andersen-thermostat decision to each particle."""
    updated = momentum.copy()
    for i in range(len(updated)):
        if rng.random() < THERMOSTAT_PROBABILITY:
            updated[i] = draw_thermal_momentum(rng)
    return updated


def speed(momentum):
    return np.linalg.norm(momentum, axis=1) / MASS


def kinetic_energy(momentum):
    return np.sum(momentum**2, axis=1) / (2.0 * MASS)


def maxwell_speed_pdf(v):
    prefactor = 4.0 * pi * (MASS / (2.0 * pi * KB * T)) ** 1.5
    return prefactor * v**2 * np.exp(-MASS * v**2 / (2.0 * KB * T))


def reduced_energy_pdf(epsilon):
    """PDF of epsilon=E/(kT) for one particle in 3D."""
    return 2.0 / sqrt(pi) * np.sqrt(epsilon) * np.exp(-epsilon)


def initialise_equal_speed(rng=np.random.default_rng()):
    """Original initial condition: identical speed, random direction."""
    p0 = sqrt(3.0 * MASS * KB * T)
    directions = rng.normal(size=(N_ATOMS, 3))
    directions /= np.linalg.norm(directions, axis=1)[:, None]
    return p0 * directions


def demo_thermostat_relaxation(n_steps=5000, sample_every=20, seed=7):
    """Isolate the Andersen sampler for a reproducible validation run.

    The full coursework simulation additionally includes hard-sphere collisions
    and VPython animation. This compact public version isolates the thermostat
    so that convergence to the canonical distributions can be checked quickly.
    """
    rng_np = np.random.default_rng(seed)
    rng = random.Random(seed)
    momentum = initialise_equal_speed(rng_np)
    sampled_speeds = []
    sampled_energies = []

    for step in range(n_steps):
        momentum = andersen_step(momentum, rng)
        if step % sample_every == 0:
            sampled_speeds.extend(speed(momentum))
            sampled_energies.extend(kinetic_energy(momentum) / (KB * T))

    return np.asarray(sampled_speeds), np.asarray(sampled_energies)


def main():
    speeds, eps = demo_thermostat_relaxation()
    print(f"N={N_ATOMS}, T={T:g} K, Ratom={R_ATOM}")
    print(f"Andersen frequency nu={NU:g} s^-1, p(step)={THERMOSTAT_PROBABILITY:.6f}")
    print(f"mean speed from sampled bath dynamics = {speeds.mean():.2f} m/s")
    print(f"mean E/(kT) = {eps.mean():.4f} (canonical expectation: 1.5)")


if __name__ == "__main__":
    main()
