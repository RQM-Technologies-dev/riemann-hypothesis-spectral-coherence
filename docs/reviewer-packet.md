# Reviewer Packet (Fast Audit Entry)

This page is a compact entry point for expert review of the **proposed proof framework** in this repository.

## Scope in one paragraph

The manuscript under review attempts to show that all nontrivial zeros of \\(\zeta(s)\\) lie on \\(\Re(s)=1/2\\), using the functional-equation symmetry of \\(\xi(s)\\) together with a spectral/coherence balance program. This repository is organized as materials for mathematical audit, not as an established proof.

## What this is claiming (high level)

- A spectral/coherence framework is proposed to connect a balance criterion with nontrivial zeros.
- The argument attempts to use reflection symmetry and a uniqueness-of-balance mechanism to isolate the critical line.
- The current claim state is explicitly **under review** and includes unresolved proof bridges.

## What this is **not** claiming

- Not claiming a settled or independently verified proof.
- Not claiming that heuristic motivation is already theorem-level justification.
- Not claiming computational checks can substitute for formal proof.

## Read these first (fastest audit path)

1. [`docs/claim-map.md`](./claim-map.md)  
   Dependency-level map of the central claim, formal inputs, and major required proofs.
2. [`notes/known-gaps.md`](../notes/known-gaps.md)  
   Explicit gap register with status labels and resolution criteria.
3. [`manuscript/main.tex`](../manuscript/main.tex)  
   Primary formal record for definitions, claim statements, and proof flow context.
4. [`manuscript/main-results.tex`](../manuscript/main-results.tex)  
   Main result framing and where critical dependencies must be checked.
5. [`manuscript/limitations.tex`](../manuscript/limitations.tex)  
   Boundary conditions, unresolved steps, and scope limits.

## Main unresolved bridges to stress-test first

From the current gap register, highest-pressure items are:

1. Exact definition of the spectral object.
2. Zero--balance correspondence (both directions, non-circular).
3. Uniqueness of the balance axis.
4. Exclusion of off-critical-line zeros (global in the strip).
5. Operator-theoretic and analytic-control prerequisites used by the exclusion step.

For current status labels and resolution criteria, use [`notes/known-gaps.md`](../notes/known-gaps.md).

## How to give feedback

Please file focused mathematical feedback with:

- exact file/section and claim identifier,
- issue type (definition, hidden assumption, dependency gap, invalid inference, analytic control, operator-theoretic step),
- classification (formal claim / heuristic step / unresolved bridge),
- minimal correction path if known (narrowed claim, added hypothesis, replacement lemma, or counterexample target).

Concise, high-specificity objections are most useful for audit.
