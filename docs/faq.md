# Frequently Asked Questions

*Calm, audit-oriented answers about the current manuscript state.*

---

## "Are you claiming that the Riemann Hypothesis is solved?"

No. This repository presents a **proposed proof framework** and **manuscript under review**.
It is not presented as an established proof.

The central unresolved bridges are tracked in [notes/known-gaps.md](../notes/known-gaps.md),
including the zero/balance correspondence and the off-line exclusion step.

---

## "Is this a proof or a framework?"

It is a **framework**.

- A **proof framework** organizes definitions, claimed correspondences, and a strategy.
- A **proof** requires all key steps to be established with complete hypotheses and dependencies.

This repository is currently in the first category.

---

## "What is the core claim map in one paragraph?"

The framework starts from the functional-equation symmetry of the completed zeta
function and attempts to add a spectral/coherence balance criterion. The intended
endpoint is: nontrivial zeros correspond to balance states, and balance is possible
only on \(\Re(s)=\tfrac12\). In the current state, this endpoint is proposed rather
than proved; see [docs/claim-map.md](./claim-map.md) for dependency-level status.

---

## "What role do spectral coherence and symmetry play?"

The formal input is the symmetry
\[
\xi(s)=\xi(1-s),
\]
with symmetry axis \(\Re(s)=\tfrac12\).

In this repository, “spectral coherence” names an attempted balance/cancellation
criterion on an associated spectral object. The unresolved step is proving that
this criterion is both equivalent to \(\zeta(s)=0\) and unique to the critical line.

Symmetry by itself is not enough to force RH; the framework must prove an additional
exclusion theorem.

---

## "How does this relate to Hilbert–Pólya-type programs?"

Conservatively: it is adjacent in spirit, not claimed as a replacement.

Like Hilbert–Pólya-type thinking, the framework seeks a spectral structure whose
properties constrain zero locations. The present manuscript does **not** claim a
completed Hilbert–Pólya realization. It proposes a related spectral-coherence route
that still requires substantial proof work.

---

## "What would count as verification?"

At minimum, independent mathematical review would need to confirm:

1. The spectral object and balance criterion are fully and non-circularly defined.
2. The zero \(\Leftrightarrow\) balance correspondence is proved under explicit hypotheses.
3. Off-critical-line solutions are excluded across the full critical strip.
4. No hidden assumptions or dependency gaps remain in the argument chain.

Computations and visualizations can support intuition, but they do not replace proof.

---

## "Why publish materials before proof completion?"

Because the repository is organized as **materials for mathematical audit**:
- open gaps are visible,
- assumptions are easier to challenge,
- and revisions can be tracked transparently.

This is intended to support scrutiny, not to signal completion.

---

## "How can I give mathematical feedback?"

Use the GitHub issue tracker with the appropriate template:

- [Mathematical Gap](../.github/ISSUE_TEMPLATE/mathematical-gap.md)
- [Notation Clarification](../.github/ISSUE_TEMPLATE/notation-clarification.md)
- [Referee Feedback](../.github/ISSUE_TEMPLATE/referee-feedback.md)

All substantive feedback will be addressed in `notes/objections-and-responses.md`
and, where relevant, incorporated into revisions of the manuscript.
