"""
placeholder.py
==============
Utility functions for numerical computation of the Riemann zeta function
and related objects, using mpmath for high-precision arithmetic.

These routines support the notebooks in code/notebooks/ and are provided for
illustration and exploration only. They do not constitute proofs and are not
used to establish any mathematical claim in the manuscript.

Dependencies: mpmath (install with: pip install mpmath)
"""

import mpmath


def set_precision(dps: int = 50) -> None:
    """Set the working precision for mpmath (in decimal places)."""
    mpmath.mp.dps = dps


def zeta(s: complex) -> mpmath.mpc:
    """
    Compute the Riemann zeta function ζ(s) to the current mpmath precision.

    Parameters
    ----------
    s : complex
        The complex argument. May be anywhere in ℂ except s = 1.

    Returns
    -------
    mpmath.mpc
        The value ζ(s).

    Notes
    -----
    Uses mpmath.zeta, which handles the analytic continuation automatically.
    """
    return mpmath.zeta(s)


def xi(s: complex) -> mpmath.mpc:
    """
    Compute the completed (xi) zeta function ξ(s).

    ξ(s) = (1/2) s(s-1) π^(-s/2) Γ(s/2) ζ(s)

    This function satisfies the functional equation ξ(s) = ξ(1-s).

    Parameters
    ----------
    s : complex
        The complex argument.

    Returns
    -------
    mpmath.mpc
        The value ξ(s).
    """
    s = mpmath.mpc(s)
    return (
        mpmath.mpf("0.5")
        * s
        * (s - 1)
        * mpmath.power(mpmath.pi, -s / 2)
        * mpmath.gamma(s / 2)
        * mpmath.zeta(s)
    )


def hardy_z(t: float) -> mpmath.mpf:
    """
    Compute the Hardy Z-function Z(t) = e^{iθ(t)} ζ(1/2 + it).

    Z(t) is real-valued on the real axis and satisfies Z(t) = 0 if and only if
    ζ(1/2 + it) = 0. It is useful for locating zeros on the critical line.

    Parameters
    ----------
    t : float
        The imaginary part of s = 1/2 + it.

    Returns
    -------
    mpmath.mpf
        The real value Z(t).
    """
    return mpmath.siegelz(t)


def riemann_siegel_theta(t: float) -> mpmath.mpf:
    """
    Compute the Riemann–Siegel theta function θ(t).

    θ(t) = Im(log Γ(1/4 + it/2)) - (t/2) log π

    Parameters
    ----------
    t : float
        Real argument.

    Returns
    -------
    mpmath.mpf
        The value θ(t).
    """
    return mpmath.siegeltheta(t)


def check_functional_equation(s: complex, tolerance: float = 1e-40) -> bool:
    """
    Numerically verify the functional equation ξ(s) = ξ(1-s).

    Parameters
    ----------
    s : complex
        The point at which to test the equation.
    tolerance : float
        The acceptable absolute difference |ξ(s) - ξ(1-s)|.

    Returns
    -------
    bool
        True if the equation holds within the specified tolerance.
    """
    xi_s = xi(s)
    xi_1ms = xi(1 - s)
    diff = abs(xi_s - xi_1ms)
    return float(diff) < tolerance


def zeros_on_critical_line(t_max: float = 50.0, n_points: int = 1000):
    """
    Locate zeros of ζ(1/2 + it) for 0 < t < t_max by scanning Z(t) for sign changes.

    This is a basic exploratory routine. For rigorous zero location, use dedicated
    software (e.g., PARI/GP or the LMFDB database).

    Parameters
    ----------
    t_max : float
        The maximum imaginary part to scan.
    n_points : int
        The number of evaluation points.

    Returns
    -------
    list of float
        Approximate t-values where Z(t) changes sign (approximate zero locations).
    """
    import numpy as np

    t_values = np.linspace(0.1, t_max, n_points)
    z_values = [float(hardy_z(t)) for t in t_values]

    zero_locations = []
    for i in range(len(z_values) - 1):
        if z_values[i] * z_values[i + 1] < 0:
            # Sign change detected: approximate zero between t_values[i] and t_values[i+1]
            t_approx = (t_values[i] + t_values[i + 1]) / 2.0
            zero_locations.append(t_approx)

    return zero_locations


# Known nontrivial zeros (imaginary parts) from the literature (Odlyzko 1987)
# These are accurate to approximately 9 decimal places.
KNOWN_ZEROS_IMAGINARY_PARTS = [
    14.134725142,
    21.022039639,
    25.010857580,
    30.424876126,
    32.935061588,
    37.586178159,
    40.918719012,
    43.327073281,
    48.005150881,
    49.773832478,
]


if __name__ == "__main__":
    set_precision(50)

    print("Checking functional equation ξ(s) = ξ(1−s) at several test points:")
    test_points = [
        0.5 + 14.134725j,   # first nontrivial zero
        0.5 + 21.022039j,   # second nontrivial zero
        0.3 + 10.0j,        # off-line point
        0.7 + 10.0j,        # symmetric off-line point
    ]
    for s in test_points:
        ok = check_functional_equation(s)
        print(f"  ξ({s}) = ξ({1-s}): {'✓' if ok else '✗'}")

    print("\nFirst few nontrivial zeros (scanning Z(t) for sign changes, t ∈ [0, 50]):")
    approx_zeros = zeros_on_critical_line(t_max=50.0, n_points=5000)
    for t in approx_zeros[:10]:
        print(f"  t ≈ {t:.6f}")
