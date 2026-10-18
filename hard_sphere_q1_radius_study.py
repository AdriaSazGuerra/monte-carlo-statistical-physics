"""Q1 — hard-sphere radius study.

Public portfolio version of the coursework analysis by Adrià Saz Guerra.
The collision model is based on the VPython HardSphereGas demonstration
by Bruce Sherwood.

For the coursework, N=500 particles were used throughout. Radius values
that are too small make collisions rare and slow equilibration; values
that are too large make non-overlapping initialisation increasingly hard
and exaggerate excluded-volume effects. The working value selected for
subsequent simulations was Ratom=0.025 (box side L=1).
"""

N_ATOMS = 500
BOX_LENGTH = 1.0
SELECTED_RADIUS = 0.025
CANDIDATE_RADII = [0.01, 0.02, 0.025, 0.03, 0.04]


def packing_fraction(n_atoms, radius, box_length=BOX_LENGTH):
    """Geometric occupied-volume fraction for N equal spheres."""
    sphere_volume = (4.0 / 3.0) * 3.141592653589793 * radius**3
    return n_atoms * sphere_volume / box_length**3


def main():
    print(f"N = {N_ATOMS}, L = {BOX_LENGTH}")
    for radius in CANDIDATE_RADII:
        phi = packing_fraction(N_ATOMS, radius)
        marker = "  <-- selected" if radius == SELECTED_RADIUS else ""
        print(f"Ratom={radius:0.3f}  geometric packing fraction={phi:0.4f}{marker}")


if __name__ == "__main__":
    main()
