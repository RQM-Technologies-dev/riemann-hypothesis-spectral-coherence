# Notation and Terminology Control Sheet

This document is a controlled notation reference for the proposed proof framework.
It is aligned to the current manuscript state and is intended for mathematical audit.

Scope:
- Record symbols already used in the manuscript.
- Distinguish committed notation from exploratory notation.
- Mark unresolved notation explicitly as placeholders.

Primary manuscript anchors:
- `manuscript/definitions.tex`
- `manuscript/spectral-framework.tex`

---

## 1) Standard notation (classical zeta-function context)

These symbols are standard and used in the manuscript without novelty claims.

| Symbol | Meaning | Manuscript alignment |
|---|---|---|
| `s = \sigma + it` | Complex variable decomposition (`\sigma, t \in \mathbb{R}`) | Standard analytic-number-theory convention |
| `\RePart(s)`, `\ImPart(s)` | Real and imaginary parts of `s` | Uses manuscript macros (`\RePart`, `\ImPart`) |
| `\mathbb{C}`, `\mathbb{R}`, `\mathbb{N}` | Complex numbers, real numbers, positive integers | Standard |
| `\zeta(s)` | Riemann zeta function (Dirichlet series for `\Re(s)>1`, meromorphic continuation elsewhere) | Standard |
| `\Gamma(s)` | Gamma function | Standard |
| `\xi(s)` | Completed zeta function `\xi(s)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)` | Defined in `definitions.tex` |
| `\sigma(s)=1-s` | Reflection involution | Defined in `definitions.tex` |
| Critical strip | `\{s\in\mathbb{C}:0<\RePart(s)<1\}` | Defined in `definitions.tex` |
| Critical line | `\{s\in\mathbb{C}:\RePart(s)=\tfrac12\}` | Defined in `definitions.tex` |

Note: This file does not re-prove standard facts (e.g., functional equation symmetry). It only records notation.

---

## 2) Reserved notation for the proposed spectral/coherence framework

These symbols are part of the manuscript program but are not yet fully formalized.
Use them only with explicit status qualifiers.

| Symbol | Intended role | Current status |
|---|---|---|
| `H` | Proposed spectral object associated with the balance program | **[Placeholder — unresolved formal definition]** |
| `\Phi(s)` | Proposed balance/coherence functional | **[Placeholder — unresolved formal definition]** |
| “balanced point” | A point `s` satisfying the manuscript’s balance criterion | **[Placeholder — criterion not yet fully specified]** |

Cross-reference guidance:
- `H` and balanced-point language are introduced as placeholders in `manuscript/definitions.tex`.
- Formalization tasks for `H` and `\Phi` are listed in `manuscript/spectral-framework.tex`.

Control note:
- Do **not** treat `H`, `\Phi`, or “balanced point” as settled objects until their domain/codomain, well-posedness, and logical role are proved.

---

## 3) Exploratory / not committed notation

The following notation is intentionally non-committal and should not be used in theorem-level claims unless promoted into the manuscript body with precise definitions.

| Symbol / term | Exploratory intent | Status |
|---|---|---|
| Quaternionic lift symbols (e.g., `q`, lifted critical-surface notation) | Possible higher-dimensional reformulation ideas | **Exploratory only; not part of the core formal pipeline** |
| “resonance” terminology | Heuristic intuition for cancellation/balance behavior | **Heuristic vocabulary only** |
| Additional operator-theoretic notation not explicitly defined in core sections | Candidate scaffolding for future formalization | **Use only with explicit placeholder marking** |

Manuscript posture:
- Higher-dimensional/quaternionic language currently appears as exploratory discussion, not as a required core mechanism.
- Reviewer-facing text should present this as optional intuition unless and until formal dependencies are added.

---

## 4) Placeholder discipline

When a symbol is not fully defined, mark it visibly as one of:
- **[Placeholder — definition required]**
- **[Placeholder — proof obligation pending]**
- **[Exploratory — not committed to core manuscript]**

Do not leave implicit placeholders.

---

## 5) Terminology status labels (audit control)

Use the following labels consistently when describing statements.

| Label | Use |
|---|---|
| **Theorem** | Fully proved in the manuscript under stated hypotheses |
| **Proposition** | Intermediate formal result, proved or cited with clear dependency |
| **Lemma** | Auxiliary formal result, proved in context |
| **Conjecture** | Explicitly unproved claim |
| **Heuristic** | Informal motivation; not proof |
| **Bridge (requires proof)** | Identified necessary step not yet established |
| **Open** | Unresolved item tracked for audit |

Audit rule:
- Computational or numerical evidence may support intuition but does not replace a theorem-level proof.

---

## 6) De-scoped notation (removed from active control list)

The following symbols are intentionally not active in this file unless they are reintroduced in core manuscript sections with precise roles:
- Ad hoc placeholders for unrelated completed `L`-function symbols.
- Extra operator symbols that are not used in `definitions.tex` or `spectral-framework.tex`.

If reintroduced, add them with status and manuscript cross-reference in the relevant section above.
