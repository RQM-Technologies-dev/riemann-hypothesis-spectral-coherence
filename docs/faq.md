# Frequently Asked Questions

*Calm, honest answers to common questions about this repository and its claims.*

---

## "Are you claiming that the Riemann Hypothesis is solved?"

No. This repository presents a **proposed proof framework** — a structured attempt
to develop an argument that, if made fully rigorous, would constitute a proof of
the Riemann Hypothesis. That argument is not complete. Several key steps remain
unproved, and they are documented candidly in [notes/known-gaps.md](../notes/known-gaps.md).

The appropriate language is: *proposed proof*, *proof framework*, *spectral-coherence
approach*, or *manuscript under review*. The words "solved," "final proof," or
"complete proof" do not appear in this repository because they are not accurate.

---

## "What is new here?"

The proposed contribution is a specific interpretation of the functional equation's
reflection symmetry as a *balance mechanism* operating on a spectral object
associated with the Riemann zeta function. The manuscript attempts to formalize
the claim that zeros of ζ correspond exactly to balance states of this spectral
object, and that such balance states are only achievable on the critical line
Re(s) = 1/2.

Whether this constitutes a genuinely new approach, an extension of known ideas,
or an inadvertent reformulation of something already in the literature is itself
a question the authors cannot answer unilaterally. External mathematical review
is needed for that assessment.

---

## "Is this a proof or a framework?"

It is a **framework**. The manuscript assembles a conceptual architecture — a
set of definitions, claimed correspondences, and a proof strategy — that would,
if fully justified, constitute a proof. The framework is not yet a proof because
several of the steps within it are not yet proved.

The distinction is important. A framework can be correct in its overall strategy
while containing gaps that prevent it from functioning as a proof. Conversely,
a framework can seem compelling while containing fundamental errors. External
scrutiny is the only reliable way to distinguish these cases.

---

## "What role do spectral coherence and symmetry play?"

The functional equation of the Riemann zeta function,

```
ξ(s) = ξ(1 − s),
```

establishes a precise reflection symmetry of the completed zeta function ξ(s).
The critical line Re(s) = 1/2 is the axis of this symmetry.

The proposed framework treats zeros of ζ as *balance points* in a spectral
object that inherits this symmetry. The *coherence* condition is an informal
name for the balance or cancellation criterion that a zero must satisfy.

The claim is that this criterion can only be satisfied on Re(s) = 1/2. Whether
that claim is correct, and whether it can be proved from the definitions, is
the central open question.

*Symmetry alone does not force zeros to the critical line.* Many functions with
the same symmetry do not have all their zeros on the symmetry axis. The argument
requires showing that ζ (or more precisely, the associated spectral object)
has an additional property that makes off-line zeros impossible.

---

## "What would count as genuine verification?"

A genuine verification of this work would require an independent mathematician
to:

1. Accept the definitions of the spectral object and the balance criterion as
   mathematically well-posed.
2. Verify that the claimed correspondence between zeros of ζ and balance states
   is correct (either by checking the proof given in the manuscript, or by
   providing an independent proof).
3. Verify that balance states can only occur on Re(s) = 1/2 (either by checking
   the argument, or independently).
4. Confirm that no logical gap or hidden assumption has been introduced.

This is the standard of proof in mathematics. No amount of numerical evidence,
visual intuition, or informal argument is a substitute for this.

---

## "Why make this public before it's proved?"

Open development serves several purposes:

- **Accountability:** Making the gaps explicit publicly prevents accidental
  overclaiming.
- **Feedback:** Expert reviewers can identify errors or gaps more quickly than
  the authors can alone.
- **Transparency:** The development history is preserved and auditable.
- **Precedent:** In an area where false claims are common, honest open development
  is itself valuable.

The repository is not being presented as a finished proof. It is being presented
as a structured research program in progress.

---

## "How can I give mathematical feedback?"

Use the GitHub issue tracker with the appropriate template:

- [Mathematical Gap](../.github/ISSUE_TEMPLATE/mathematical-gap.md)
- [Notation Clarification](../.github/ISSUE_TEMPLATE/notation-clarification.md)
- [Referee Feedback](../.github/ISSUE_TEMPLATE/referee-feedback.md)

All substantive feedback will be addressed in `notes/objections-and-responses.md`
and, where relevant, incorporated into revisions of the manuscript.
