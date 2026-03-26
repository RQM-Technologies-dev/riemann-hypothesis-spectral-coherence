# Open Questions

*A working list of mathematical questions that have arisen during the development
of the framework and have not yet been resolved.*

This file records questions that are either:
- Prerequisites for completing the argument (marked ⛔),
- Related questions that would strengthen the framework (marked 🔷), or
- Interesting side questions not essential to the main argument (marked ○).

---

## On the Spectral Construction

**Q1** ⛔ What is the correct Hilbert space for the operator H? Candidates include
$L^2(\R)$, $L^2(\R, e^{-|t|} dt)$, Hardy space $H^2(\C^+)$, or a weighted Sobolev space.
What properties does the space need to support the symmetry and the correspondence claim?

**Q2** ⛔ What is the explicit action of H on its domain? How is the functional equation
$\xi(s) = \xi(1-s)$ encoded in the action of H?

**Q3** ⛔ Is H self-adjoint, symmetric, or neither? If H is self-adjoint, its spectrum
is real, which would immediately connect the framework to the Hilbert–Pólya conjecture.

**Q4** 🔷 If H is not self-adjoint, can a self-adjoint modification or partner
operator be defined? Is there a natural self-adjoint operator whose eigenvalues
are the imaginary parts of the nontrivial zeros?

**Q5** ⛔ How is the coherence functional Φ(s) derived from H? Is Φ a matrix
element, a trace, a spectral measure evaluated at a point, or something else?

---

## On the Correspondence Claim

**Q6** ⛔ Can the correspondence between zeros of ζ and balance points of H be
established via a trace formula? If so, which trace formula, and does the
required trace converge?

**Q7** ⛔ Is the correspondence bijective (every zero corresponds to exactly one
balance point, and vice versa), or could there be balance points that are not zeros?

**Q8** 🔷 Does the framework extend to L-functions? The generalized Riemann
Hypothesis asserts that all nontrivial zeros of Dirichlet L-functions lie on
the critical line. If the framework works for ζ, does it generalize?

---

## On the Critical Line Argument

**Q9** ⛔ What property of H, specifically, makes balance impossible off the critical line?
Is it a spectral gap, a positivity argument, an inequality derived from the functional
equation, or something else?

**Q10** ⛔ Can the impossibility of off-line balance be derived from a known inequality
for ζ or ξ (e.g., convexity bounds, moment estimates, zero-free regions)?

**Q11** 🔷 If a zero at $s_0$ with Re(s₀) ≠ 1/2 is assumed to exist, what
specific contradiction does the framework derive? Is the contradiction quantitative
(leading to an inequality that fails) or structural (leading to an inconsistency
in the definition)?

---

## On Higher-Dimensional Extensions

**Q12** ○ Is there a natural quaternionic or higher-dimensional setting in which
the argument becomes cleaner? If so, does the projection back to ℂ recover the
critical line condition?

**Q13** ○ Are there connections to the theory of automorphic forms or the
Selberg trace formula that would provide a natural spectral setting?

---

## On Computational Investigation

**Q14** 🔷 Can the coherence functional Φ(s) be approximated numerically for a
finite truncation of H? Would such an approximation show a clear signal at the
known zeros of ζ and a clear absence of signal off the critical line?

**Q15** ○ Are there alternative functions (not ζ, but having similar symmetries)
to which the framework might be applied as a test case? Does it predict their
zero locations correctly?

---

*This list is updated as new questions arise. Questions that are answered are
removed from this file and their resolutions are noted in the manuscript or
in `notes/review-log.md`.*

*Last updated: 2026-03-26*
