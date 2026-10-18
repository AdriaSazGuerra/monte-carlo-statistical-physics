"""Q3 — canonical hard-sphere gas in a vertical gravitational field.

Adrià Saz Guerra
Public portfolio refactor of the coursework implementation.
The coursework uses an Andersen thermostat at T=300 K and compares the
simulated vertical velocity and height distributions with theory.
"""

from math import exp, pi, sqrt
import numpy as np

N_ATOMS = 500
L = 1.0
MASS = 4e-3 / 6e23
KB = 1.4e-23
T = 300.0

# Physical g produces a visually negligible barometric gradient for helium in
# a 1 m box at room temperature, so the coursework also used an amplified
# effective field to make the distributional test clearly resolvable.
EFFECTIVE_GRAVITY = 9.8e7  # m/s^2


def vertical_velocity_pdf(vz):
    """One-dimensional Maxwell distribution for v_z."""
    prefactor = sqrt(MASS / (2.0 * pi * KB * T))
    return prefactor * np.exp(-MASS * vz**2 / (2.0 * KB * T))


def height_pdf(z, gravity=EFFECTIVE_GRAVITY):
    """Normalised barometric distribution on z in [-L/2, L/2]."""
    a = MASS * gravity / (KB * T)
    z = np.asarray(z)
    if abs(a * L) < 1e-12:
        return np.ones_like(z, dtype=float) / L
    return a * np.exp(-a * (z + L / 2.0)) / (1.0 - exp(-a * L))


def sample_equilibrium(n=N_ATOMS, gravity=EFFECTIVE_GRAVITY, seed=7):
    """Direct canonical samples used as a distribution-level cross-check."""
    rng = np.random.default_rng(seed)
    sigma_v = sqrt(KB * T / MASS)
    vz = rng.normal(0.0, sigma_v, size=n)

    a = MASS * gravity / (KB * T)
    u = rng.random(n)
    if abs(a * L) < 1e-12:
        z = rng.uniform(-L / 2.0, L / 2.0, size=n)
    else:
        # Inverse CDF of exp[-a(z+L/2)] on the finite box.
        z = -L / 2.0 - np.log(1.0 - u * (1.0 - np.exp(-a * L))) / a
    return vz, z


def main():
    vz, z = sample_equilibrium()
    z_grid = np.linspace(-L / 2, L / 2, 4000)
    expected_mean_z = np.trapezoid(z_grid * height_pdf(z_grid), z_grid)
    print(f"T={T:g} K, effective g={EFFECTIVE_GRAVITY:.2e} m/s^2")
    print(f"sample <v_z>={vz.mean():.2f} m/s (theory: 0)")
    print(f"sample <z>={z.mean():.4f} m; theoretical <z>={expected_mean_z:.4f} m")


if __name__ == "__main__":
    main()
