# Claim Map

*A concise, reviewer-oriented map of the argument structure.*

---

## Central Claim

The manuscript proposes that the nontrivial zeros of the Riemann zeta function
ζ(s) are forced onto the critical line Re(s) = 1/2 by a balance condition arising
from the reflection symmetry of the functional equation. The proposed argument
attempts to show that this balance condition cannot be satisfied at any s with
Re(s) ≠ 1/2.

**Status:** Proposed. The framework is conceptually assembled; formal rigour is
in progress. See [notes/known-gaps.md](../notes/known-gaps.md).

---

## Main Symmetry Principle

The functional equation of the Riemann zeta function,

```
ξ(s) = ξ(1 − s),    where ξ(s) = (1/2)s(s−1)π^(−s/2)Γ(s/2)ζ(s),
```

establishes a reflection symmetry of the completed zeta function ξ(s) about
the line Re(s) = 1/2. Any zero of ξ (equivalently, of ζ in the critical strip)
must lie in a configuration compatible with this symmetry.

**The manuscript proposes:** that this symmetry is not merely a constraint on
where zeros *can* occur, but, together with the spectral-coherence structure,
a mechanism that *forces* all zeros to lie on Re(s) = 1/2.

**What remains to be shown:** that the symmetry alone, or the symmetry combined
with the spectral construction, is sufficient to rule out off-line zeros.

---

## Spectral / Coherence Interpretation

The proposed framework interprets nontrivial zeros as *balance points* in a
spectral object associated with ζ. Informally:

- A zero of ζ(s) is treated as a state at which certain spectral contributions
  cancel — a destructive interference or equilibrium condition.
- The reflection symmetry of ξ constrains which states can achieve this
  cancellation.
- The claim is that cancellation is only achievable when the state lies on
  Re(s) = 1/2.

**What must be made rigorous:** The spectral object must be defined precisely
as a mathematical operator or functional. The correspondence between its
"cancellation states" and zeros of ζ must be proved, not assumed. See
[manuscript/spectral-framework.tex](../manuscript/spectral-framework.tex) and
[manuscript/definitions.tex](../manuscript/definitions.tex).

---

## Why the Critical Line Is Privileged

The manuscript argues that Re(s) = 1/2 is the unique axis of the reflection
symmetry s ↔ 1 − s. Therefore:

1. Any zero paired with its symmetric counterpart under this reflection must,
   if the balance criterion is symmetric itself, lie on the symmetry axis.
2. Off-axis zeros would necessarily come in symmetric pairs (s, 1−s) unless they
   are already on the axis — but the manuscript attempts to show that off-axis
   pairs cannot satisfy the proposed balance criterion simultaneously.

**Caveat:** This argument currently relies on an analogy between balance in the
proposed spectral object and the classical functional equation. The analogy must
be converted into a theorem. This is the primary open step.

---

## What Remains to Be Formalized

The following items are required to complete the argument:

| Step | Description | Status |
|------|-------------|--------|
| 1 | Precise definition of the spectral/coherence operator | Open |
| 2 | Proof that zeros of ζ correspond exactly to cancellation states of the operator | Open |
| 3 | Proof that the balance criterion is symmetric under s ↔ 1−s | Partial |
| 4 | Proof that only Re(s) = 1/2 supports the balance criterion | Open (central gap) |
| 5 | Ruling out all off-line zero configurations | Open |

See [notes/known-gaps.md](../notes/known-gaps.md) for the full gap register.

---

## What a Skeptical Mathematician Should Test First

If you want to identify the weakest point in the current argument as efficiently
as possible, focus on the following questions:

1. **Is the spectral object well-defined?**
   Does [manuscript/spectral-framework.tex](../manuscript/spectral-framework.tex)
   give a mathematically precise definition of the operator or functional? If not,
   the argument cannot proceed.

2. **Is the correspondence between zeros and cancellation states proved?**
   Or is it assumed by analogy? Check
   [manuscript/definitions.tex](../manuscript/definitions.tex) and
   [manuscript/lemmas.tex](../manuscript/lemmas.tex).

3. **Does the symmetry argument actually rule out off-line zeros, or does it merely
   make them seem implausible?**
   Check [manuscript/critical-line-argument.tex](../manuscript/critical-line-argument.tex).

4. **Are there hidden assumptions?**
   Check [manuscript/limitations.tex](../manuscript/limitations.tex) and
   [notes/objections-and-responses.md](../notes/objections-and-responses.md).

5. **Does the argument apply only to ζ, or could it be adapted to functions that
   violate RH?**
   If the argument does not distinguish ζ from functions with off-line zeros, it
   cannot be sufficient.
