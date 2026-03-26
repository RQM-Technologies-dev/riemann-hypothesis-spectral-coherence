# Riemann Hypothesis via Spectral Coherence

**A repository for a proposed spectral-coherence approach to the critical line**

> **Disclaimer:** This repository presents a proposed proof framework and supporting materials
> for mathematical review. It should be read as a research program under active refinement
> unless and until the argument is independently verified.

---

## Summary

The central idea developed here is that the nontrivial zeros of the Riemann zeta function
can be interpreted as balance points in a reflection-symmetric spectral structure. Under the
proposed framework, the critical line Re(s) = 1/2 appears as the unique symmetry and balance
axis — the only locus at which the relevant spectral objects can achieve the cancellation
state corresponding to a zero.

This is a proposed proof framework, not a completed proof. The materials in this repository
are organized to support mathematical audit, critique, formalization, and revision.

---

## What This Repo Contains

| Directory / File | Contents |
|---|---|
| `manuscript/` | LaTeX source for the formal manuscript |
| `docs/` | Readable documentation: claim map, notation, overview, roadmap, FAQ |
| `notes/` | Informal working notes: known gaps, open questions, objections |
| `code/` | Supporting Python code and Jupyter notebooks for visualization |
| `media/` | Figures and diagrams |
| `.github/` | Issue templates and CI workflows |

---

## Fastest Path for Reviewers

If you are a mathematician who wants to assess this work efficiently:

1. **[docs/claim-map.md](docs/claim-map.md)** — concise map of the argument structure and
   what would be required to make it rigorous.
2. **[manuscript/main.tex](manuscript/main.tex)** — the formal manuscript source (compile
   with LaTeX, or see the CI-generated PDF artifact).
3. **[notes/known-gaps.md](notes/known-gaps.md)** — a candid list of unresolved steps and
   vulnerable points in the argument.

---

## Repository Structure

```
/
├─ README.md
├─ LICENSE
├─ CITATION.cff
├─ .gitignore
├─ .github/
│  ├─ ISSUE_TEMPLATE/
│  │  ├─ bug-report.md
│  │  ├─ mathematical-gap.md
│  │  ├─ notation-clarification.md
│  │  └─ referee-feedback.md
│  ├─ pull_request_template.md
│  └─ workflows/
│     ├─ build-latex.yml
│     └─ link-check.yml
├─ docs/
│  ├─ index.md
│  ├─ claim-map.md
│  ├─ overview-for-mathematicians.md
│  ├─ overview-general-audience.md
│  ├─ notation.md
│  ├─ roadmap.md
│  ├─ faq.md
│  └─ bibliography.md
├─ manuscript/
│  ├─ main.tex
│  ├─ abstract.tex
│  ├─ introduction.tex
│  ├─ definitions.tex
│  ├─ main-results.tex
│  ├─ proof-architecture.tex
│  ├─ lemmas.tex
│  ├─ symmetry-framework.tex
│  ├─ spectral-framework.tex
│  ├─ critical-line-argument.tex
│  ├─ discussion.tex
│  ├─ limitations.tex
│  ├─ appendix-a-intuition.tex
│  ├─ appendix-b-operator-setup.tex
│  ├─ appendix-c-computational-notes.tex
│  ├─ references.bib
│  └─ figures/
├─ notes/
│  ├─ review-log.md
│  ├─ open-questions.md
│  ├─ objections-and-responses.md
│  └─ known-gaps.md
├─ code/
│  ├─ README.md
│  ├─ notebooks/
│  │  ├─ spectral-visualization.ipynb
│  │  └─ critical-line-geometry.ipynb
│  └─ src/
│     └─ placeholder.py
└─ media/
   ├─ figures/
   └─ diagrams/
```

---

## Current Status

- [x] Conceptual framework assembled
- [x] Repository structure and documentation scaffolded
- [ ] Manuscript draft in progress
- [ ] Formal operator construction under development
- [ ] Formalization still under review
- [ ] External mathematical feedback invited

---

## How to Give Mathematical Feedback

Mathematical feedback is welcome and encouraged. Please use the GitHub issue tracker with the
appropriate template:

- **Mathematical gap** — use the [Mathematical Gap template](.github/ISSUE_TEMPLATE/mathematical-gap.md)
  to identify steps in the argument that are not rigorous or are not justified.
- **Notation clarification** — use the [Notation Clarification template](.github/ISSUE_TEMPLATE/notation-clarification.md)
  for undefined, ambiguous, or conflicting notation.
- **Referee feedback** — use the [Referee Feedback template](.github/ISSUE_TEMPLATE/referee-feedback.md)
  for structured review comments.

All feedback will be logged in `notes/review-log.md` and addressed in `notes/objections-and-responses.md`.

---

## Citation / Archival Plan

A `CITATION.cff` file is included for machine-readable citation metadata. The planned
archival sequence is:

1. Stable public repository (current stage)
2. Zenodo DOI assignment for version snapshots
3. arXiv preprint submission once the manuscript reaches a reviewable state
4. Journal submission following external expert review

See [docs/roadmap.md](docs/roadmap.md) for the full publication strategy.

---

## License

This repository is released under the [MIT License](LICENSE).
