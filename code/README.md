# Code and Notebooks

This directory contains Python code and Jupyter notebooks that support the
manuscript through visualization and numerical exploration.

> **Note:** All code here is for illustration and exploration only. Numerical
> computations do not constitute proofs and are not used to establish any claim
> in the manuscript.

---

## Contents

### Notebooks

- **`notebooks/spectral-visualization.ipynb`** — Visualizes the Riemann zeta
  function along and near the critical line. Illustrates the reflection symmetry
  ξ(s) = ξ(1−s) and the placement of known nontrivial zeros.

- **`notebooks/critical-line-geometry.ipynb`** — Plots the geometry of the
  critical line Re(s) = 1/2 in the complex plane. Shows the reflection
  involution s ↦ 1−s and its fixed-point locus.

### Source Code

- **`src/placeholder.py`** — Utility functions for computing ζ(s) and ξ(s)
  numerically, using the `mpmath` library for high-precision arithmetic.

---

## Requirements

Python 3.9 or later is required. Install dependencies with:

```bash
pip install mpmath numpy matplotlib jupyter
```

Or, using a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install mpmath numpy matplotlib jupyter
```

---

## Running the Notebooks

```bash
cd code/notebooks
jupyter notebook
```

Then open the desired notebook in your browser.

---

## Notes on Numerical Computation

All numerical values of ζ(s) are computed using `mpmath`, which provides
arbitrary-precision arithmetic. The default precision in the notebooks is
50 decimal digits. For exploratory work, 30 digits is usually sufficient.

The known nontrivial zeros used in the notebooks are taken from the published
tables of Odlyzko (1987) and are accurate to many decimal places. No claim in
the manuscript depends on these numerical values.
