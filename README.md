# Riemann Hypothesis via Spectral Coherence

**Proposed proof framework and audit materials for a spectral-coherence approach to the critical line.**

> [!IMPORTANT]
> **Disclaimer (read first):** This repository is a **proposed proof framework under review**. It is provided as material for mathematical audit and should not be treated as an established proof unless independently verified.

## What this repository contains

This repository is organized for skeptical, technical review.

- `manuscript/`: Primary formal record (LaTeX source), including definitions, claims, proof architecture, and limitations.
- `docs/`: Reviewer-oriented navigation documents (claim map, notation, roadmap, and audience-specific overviews).
- `notes/`: Research-state tracking (known gaps, open questions, objections, and review log).
- `code/`: Supporting computational experiments and visualizations; these are evidence aids, not substitutes for proof.
- `media/`: Figures and diagrams used by the manuscript and documentation.

The argument attempts to show that the critical line arises as the unique balance axis in a reflection-symmetric spectral framework. The materials separate formal statements, heuristic motivation, and unresolved bridges where possible.

## Fastest path for reviewers

If you have one minute to orient and 30–60 minutes for first-pass audit, start here:

1. [`docs/claim-map.md`](docs/claim-map.md) — dependency-level map of major claims and what still requires justification.
2. [`manuscript/main.tex`](manuscript/main.tex) — primary manuscript source and formal claim context.
3. [`notes/known-gaps.md`](notes/known-gaps.md) — explicit list of unresolved bridges and vulnerability points.

Suggested first-pass workflow:

- Read the claim map to identify the highest-dependency steps.
- Check each corresponding statement in `manuscript/` for hypotheses, scope, and dependency clarity.
- Cross-check unresolved steps against `notes/known-gaps.md` to confirm that open bridges remain visible.

## Repository structure

```text
.
├── README.md
├── CITATION.cff
├── docs/
│   ├── claim-map.md
│   ├── index.md
│   ├── notation.md
│   ├── overview-for-mathematicians.md
│   ├── overview-general-audience.md
│   ├── roadmap.md
│   └── ...
├── manuscript/
│   ├── main.tex
│   ├── definitions.tex
│   ├── main-results.tex
│   ├── limitations.tex
│   └── ...
├── notes/
│   ├── known-gaps.md
│   ├── open-questions.md
│   ├── objections-and-responses.md
│   └── review-log.md
├── code/
└── media/
```

## Current status

- [x] Repository organized as materials for mathematical audit.
- [x] Core manuscript structure and supporting reviewer documents are present.
- [x] Known gaps are tracked explicitly in `notes/known-gaps.md`.
- [ ] Key bridges remain to be converted from heuristic or partial arguments into fully formal proofs.
- [ ] External expert review is still needed before any claim of independent verification.
- [ ] Archival and publication steps remain contingent on review outcomes.

## How to give mathematical feedback

Focused mathematical criticism is welcome.

- Use GitHub issues and select the most relevant template in `.github/ISSUE_TEMPLATE/`.
- For a specific gap, include:
  - exact file/section and claim identifier,
  - whether the issue is definitional, logical dependency, hidden assumption, or invalid inference,
  - whether the concern is formal, heuristic, or computational.
- If possible, propose a minimal correction path (revised lemma, narrowed claim, or explicit added assumption).

High-value feedback targets:

- implicit assumptions,
- nontrivial reduction steps,
- equivalence claims requiring proof,
- places where computational evidence may be over-interpreted.

## Citation / archival plan

- `CITATION.cff` provides machine-readable citation metadata for this repository.
- Versioned archival snapshots are intended for DOI registration (e.g., Zenodo) once milestones are reached.
- Any preprint or submission-stage release should reflect the then-current manuscript state and explicitly preserve unresolved bridges.

Until independent verification exists, please cite this project as a **manuscript under review / proposed proof framework**.

## License

Released under the [MIT License](LICENSE).
