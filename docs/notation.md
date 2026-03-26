# Notation Reference

*This file defines all symbols, conventions, and terminology used in the manuscript.*

When notation is introduced in the manuscript, it will be cross-referenced here.
If you encounter a symbol that is undefined or ambiguous, please open a
[Notation Clarification issue](../.github/ISSUE_TEMPLATE/notation-clarification.md).

---

## General Conventions

| Convention | Description |
|---|---|
| `s = σ + it` | Standard decomposition of a complex variable s into real part σ and imaginary part t |
| `s̄` | Complex conjugate of s |
| `Re(s)` | Real part of s (also written σ when s = σ + it) |
| `Im(s)` | Imaginary part of s (also written t when s = σ + it) |
| `ℂ` | The field of complex numbers |
| `ℝ` | The field of real numbers |
| `ℕ` | The natural numbers {1, 2, 3, ...} |
| `ℍ` | The quaternions (if used; see §Quaternionic Variables below) |

---

## Zeta Function Notation

| Symbol | Definition |
|---|---|
| `ζ(s)` | The Riemann zeta function, defined for Re(s) > 1 by ζ(s) = Σ n^(−s), extended by analytic continuation to ℂ \ {1} |
| `ξ(s)` | The completed (or "xi") zeta function: ξ(s) = (1/2) s(s−1) π^(−s/2) Γ(s/2) ζ(s) |
| `Λ(s)` | *[Placeholder — define if used for a different completed L-function]* |
| `Z(t)` | Hardy's Z-function: Z(t) = e^(iθ(t)) ζ(1/2 + it), where θ(t) is the Riemann–Siegel theta function |
| `θ(t)` | The Riemann–Siegel theta function: θ(t) = Im(log Γ(1/4 + it/2)) − (t/2) log π |

**Functional equation:** ξ(s) = ξ(1 − s) for all s ∈ ℂ.

---

## Gamma Function and Reflection Notation

| Symbol | Definition |
|---|---|
| `Γ(s)` | The gamma function, the standard analytic continuation of the factorial |
| `Γ(s) Γ(1−s) = π / sin(πs)` | The reflection formula for Γ |
| `B(x,y)` | Beta function: B(x,y) = Γ(x)Γ(y)/Γ(x+y), used if needed |

---

## Spectral Operators

*The following notation is reserved for the spectral-coherence construction.
Precise definitions are given in `manuscript/spectral-framework.tex` and
`manuscript/definitions.tex`.*

| Symbol | Intended Role | Status |
|---|---|---|
| `H` | The proposed spectral operator associated with ζ | Placeholder — definition in progress |
| `𝒟(H)` | Domain of the operator H | Placeholder |
| `σ(H)` | Spectrum of H | Placeholder |
| `σ_p(H)` | Point spectrum (eigenvalues) of H | Placeholder |
| `⟨ · , · ⟩` | Inner product on the relevant Hilbert/Banach space | Placeholder — space to be defined |
| `‖ · ‖` | Norm on the relevant space | Placeholder |
| `T_s` | Spectral evaluation operator at s | Placeholder |
| `Φ(s)` | Coherence functional evaluated at s | Placeholder — may coincide with ξ or be a derived object |

---

## Coherence and Resonance Language

The following informal terms are used in the motivating sections and appendices.
They are *not* formal mathematical objects until given precise definitions in the manuscript.

| Term | Informal Meaning | Formal Analog (if defined) |
|---|---|---|
| Balance point | A value of s where the spectral object achieves a prescribed equilibrium condition | Balance criterion (see definitions.tex) |
| Cancellation state | A configuration where contributions from symmetric pairs cancel | To be formalized |
| Spectral coherence | The property of the operator H relevant to zero placement | Definition in spectral-framework.tex |
| Resonance | Informal: a state of constructive or destructive self-reinforcement | To be formalized |
| Balance axis | The critical line Re(s) = 1/2, viewed as the axis of the reflection symmetry | Definition 1 in definitions.tex |

---

## Quaternionic or Lifted Variables

*If the manuscript employs a quaternionic extension or a lift of the complex variable s,
the notation for those objects will be defined here.*

| Symbol | Intended Role | Status |
|---|---|---|
| `q` | Quaternionic variable corresponding to the lifting of s ∈ ℂ into ℍ | Placeholder |
| `q = a + bi + cj + dk` | Standard quaternion decomposition | Standard |
| `𝒞_q` | Lifted critical surface in quaternionic space | Placeholder |
| `π_ℂ` | Projection from quaternionic space back to ℂ | Placeholder |

*Note: The use of quaternionic variables is currently exploratory. If the construction
does not require them, this section will be removed.*

---

## Proof Status Labels

The manuscript uses the following labels to distinguish the epistemic status of statements:

| Label | Meaning |
|---|---|
| **Theorem** | Proved rigorously within the manuscript |
| **Proposition** | A result used in the argument; either proved here or cited from the literature |
| **Lemma** | A technical auxiliary result, proved here |
| **Conjecture** | Believed to be true; not yet proved |
| **Heuristic** | An informal claim intended to motivate the formal development |
| **Bridge (requires proof)** | A step that is identified as necessary but not yet established |
| **Open** | Explicitly unresolved |
