This page exists to make mathematical scrutiny easier.

# Known Gaps (Audit-Facing)

This register lists the most vulnerable bridges in the proposed proof framework.
It is written for reviewers who want a fast map of what is not yet proved.

Conventions used below:
- **Status labels:** Open / Partial / Blocked.
- **Resolution criterion:** what would count as a mathematically adequate closure of the gap.
- **Evidence rule:** numerical checks or analogy can support direction, but do not close a proof gap.

Core bridge names synchronized with manuscript text:
1. exact spectral object
2. zero--balance correspondence
3. uniqueness of the balance axis
4. exclusion of off-critical-line zeros
5. operator-theoretic gaps
6. analytic-control gaps

---

## 1) Exact definition of the spectral object

**Gap:** The argument depends on a spectral object (operator/system) often denoted by \(H\), but a complete construction is not yet fixed.

**Why it matters:**
- Without a precise object, later statements (symmetry, spectrum, balance criterion, correspondence with zeros) are not formal claims.
- Domain choices, operator closure, and functional setting can change the truth value of downstream statements.

**Current status:** **Open (foundational).** Candidate constructions are discussed, but no single fully specified object has been adopted and verified.

**What would count as resolution:**
- A full definition of the ambient space, domain, operator action, and regularity assumptions.
- Proof that the object is well-defined (e.g., densely defined/closed where required).
- A lemma map showing which later claims depend on which operator properties.

---

## 2) Zero--balance correspondence

**Gap:** The framework attempts to show that a cancellation/balance criterion is equivalent to the nontrivial zero condition for \(\zeta(s)\), but exact equivalence is not yet proved.

**Why it matters:**
- If the criterion is only approximate, the framework does not prove RH.
- If the criterion is one-way only, it leaves false positives or misses zeros.
- If the criterion is defined using zeros, circularity can invalidate the claim.

**Current status:** **Open (critical).** The correspondence is a central intended theorem, not yet established.

**What would count as resolution:**
- A non-circular definition of the cancellation criterion independent of zero locations.
- A two-direction theorem with explicit hypotheses:
  1. zero \(\Rightarrow\) cancellation,
  2. cancellation \(\Rightarrow\) zero.
- Proof that the theorem applies on the whole critical strip where needed.

---

## 3) Uniqueness of the balance axis

**Gap:** The argument attempts to show that exact balance is possible only on \(\Re(s)=1/2\), but the theorem target is not yet closed with explicit local regime, assumptions, and non-spuriousness controls.

**Why it matters:**
- RH requires excluding any valid balance mechanism off the critical line.
- Symmetry alone does not force all zeros onto a symmetry axis.

**Current status:** **Open (central bridge).** Motivating geometry exists; a theorem-level uniqueness argument does not.

**What would count as resolution:**
- A theorem stating precise assumptions and explicit validity regime for
  \[
  \Phi_H(s)=0 \Rightarrow \Re(s)=1/2.
  \]
- A proof that no alternative axis/curve can satisfy the same criterion under the same assumptions.
- Explicit non-spuriousness conditions on the balance predicate and clear dependency on previously proved structural properties of the spectral object.

---

## 4) Exclusion of off-critical-line zeros

**Gap:** The framework does not yet provide a complete proof excluding all off-line zeros in the critical strip, and the local-to-global transfer burden is still open.

**Why it matters:**
- RH is an exclusion statement over all nontrivial zeros.
- A local or asymptotic argument that leaves edge regimes untreated is insufficient.

**Current status:** **Open (completeness).** A candidate exclusion-mechanism template is now stated in the manuscript, but no theorem-level instantiation has been proved.
The current manuscript strategy prioritizes one route under audit:
local Stage-5 uniqueness \(\Rightarrow\) transfer to full-strip \(\Rightarrow\) no-alternative-locus closure for \(\mathcal{B}\) \(\Rightarrow\) global exclusion.
This route is now written against a named minimum synchronized assumption scaffold \(\mathcal{H}_{\mathrm{S6}}^{\min}\), used to state the theorem target cleanly while keeping proof status open.
Other mechanism classes (coercive/positivity/rigidity, reflection-incompatibility, contradiction templates) remain active as supporting or fallback components, not equal-status endpoints.

**What would count as resolution:**
- A global contradiction or global structural theorem that covers every \(s\) with \(0<\Re(s)<1\), \(\Re(s)\neq 1/2\), under one synchronized hypothesis package, with the mechanism class stated explicitly (e.g., coercive gap, positivity/monotonicity, rigidity, or reflection-incompatibility).
- An explicit local-to-global transfer theorem target for the balanced set \(\mathcal{B}\): local Stage-5 uniqueness on a declared \(\mathcal{R}_{\mathrm{loc}}\) extends to the full admissible strip class \(\mathcal{A}_{\mathrm{strip}}\) under synchronized hypotheses.
- The transfer target should be stated as a distinct closure bridge between local Target B control and global exclusion (not merged with either statement), with theorem-shape implication
  \[
  \big(\forall s\in\mathcal{B}\cap\mathcal{R}_{\mathrm{loc}},\ \Re(s)=1/2\big)\Rightarrow
  \big(\forall s\in\mathcal{B}\cap\mathcal{A}_{\mathrm{strip}},\ \Re(s)=1/2\big).
  \]
- The transfer target must state concrete closure hypotheses: admissibility stability across regimes, compatibility of local estimates with the full admissible class, continuation/compactness/uniformity control, no-loss symmetry compatibility, and prevention of hidden off-line branches outside the local regime.
- Explicit treatment of parameter ranges where hidden assumptions often occur (large imaginary part, boundary-near behavior).
- A proof that does not rely on unproved regularity assumptions.

---

## 5) Dependence on analogy versus theorem (cross-cutting)

**Gap:** Parts of the framework are motivated by geometric/physical analogy (balance, resonance, coherence) that have not yet been fully translated into formal theorems.

**Why it matters:**
- Analogy can guide definitions but cannot certify truth.
- Reviewers need to separate motivational language from proved implications.

**Current status:** **Partial.** The manuscript marks open steps, but several key transitions from intuition to theorem remain unresolved. This item is cross-cutting and does not replace any of the six core bridges listed above.

**What would count as resolution:**
- For each analogy-backed step, replace with explicit definitions and theorem statements.
- Keep intuition sections clearly labeled as heuristic.
- Remove dependence of core logical steps on heuristic interpretation.

---

## 6) Operator-theoretic gaps

**Gap:** The operator-theoretic support package needed by the manuscript (OP1--OP8 in `manuscript/spectral-framework.tex`) is not yet discharged under one finalized operator model.
This includes ambient-space/domain typing, closure/closability control, symmetry-domain invariance, intertwining/covariance identities, spectral-legitimacy conditions, compatibility with \(\Phi_H\), admissibility stability under operator-side transforms, and dependency-locked usage.

**Why it matters:**
- Spectral conclusions are only as strong as the operator foundations.
- Small domain or closability errors can invalidate purported spectral correspondences.

**Current status:** **Open (technical core).** Requirements are recognized, but proofs are not complete.

**What would count as resolution:**
- A theorem-level OP1--OP8 package proved (or explicitly imported as synchronized assumptions) for one chosen operator realization.
- Verification that each operator property is invoked only where hypotheses are met in Target A, Target B, and Stage-6 transfer/exclusion.
- A dependency table linking each RH-relevant claim to specific operator lemmas, with no hidden operator assumptions.

---

## 7) Analytic-control gaps

**Gap:** The Stage-6 analytic-control support package remains unproved. In current manuscript notation this package includes AC1--AC6: strip-wide growth/defect bounds, uniform convergence by regime, interchange legitimacy, continuation/extension control, no-hidden-branch closure for $\mathcal{B}$, and compatibility of local estimates with strip-wide admissibility.

**Why it matters:**
- RH arguments often fail at precisely these global analytic steps.
- Unjustified exchanges or hidden regularity assumptions can create false proofs.

**Current status:** **Open (high risk).** Some intended pathways are sketched, but full analytic verification is pending.

**What would count as resolution:**
- A theorem-level AC1--AC6 package, with each item either proved or explicitly imported as a hypothesis in one synchronized Stage-6 assumption set.
- Explicit hypotheses for every analytic transformation used in transfer/exclusion, including sector-by-sector validity ranges and constants where required.
- Proofs of convergence and uniformity strong enough for local-to-global transfer (not only pointwise statements).
- Proof-level justification of every interchange step (limit/integral, derivative/integral, summation/integration, contour deformation).
- A no-hidden-branch closure argument excluding off-line components of $\mathcal{B}$ that could appear only outside $\mathcal{R}_{\mathrm{loc}}$.
- Independent checking that no step smuggles in the target conclusion.

**Current Stage-6 first-subtheorem audit focus (single highest-risk step):**
- The most likely failure point in the present contradiction-style first subtheorem is the no-drift transport bridge from local Stage-5 hypotheses on $\mathcal{R}_{\mathrm{loc}}$ to transfer-reachable endpoints in $\mathcal{A}_{\mathrm{strip}}$.
- If this bridge is not theorem-level, the contradiction step can invoke local uniqueness at an endpoint without proving that the same hypothesis tuple still holds there under $\mathcal{H}_{\mathrm{S6}}^{\min}$.
- The current best candidate neutralizing result is the open theorem target `thm:stage6-neutralizing-transport-uniformity` (transport-uniformity contradiction enabler) in `manuscript/critical-line-argument.tex`.
- Current classification of that neutralizing target: **genuinely mixed**, with **analytic dominant burden** and **operator-theoretic supporting burden** in the present first proving attempt.
- Best current candidate structural property for why the first defect quantity might be controllable: non-increase of \(\Delta_{\mathrm{nd}}\) under synchronized transport extension on the transfer class \(\mathfrak{C}_{\mathrm{tr}}\) under \(\mathcal{H}_{\mathrm{S6}}^{\min}\), i.e. \(C_1\preceq C_2 \Rightarrow \Delta_{\mathrm{nd}}(C_2;\Theta_{\mathrm{S5}},\delta)\le \Delta_{\mathrm{nd}}(C_1;\Theta_{\mathrm{S5}},\delta)\), with analytic uniformity/continuation control as dominant support and operator-side transport stability as supporting control.
- Status of that reason: **open strategic rationale under audit** (not a proved theorem, not sufficient by itself).
- Resolution of this highest-risk step requires controlling the first provisional defect quantity now named in the manuscript, $\Delta_{\mathrm{nd}}(C;\Theta_{\mathrm{S5}},\delta)=\sup_{u\in U(C)}d_{\Theta}^{(C)}(u)$ (tuple-drift along $C\in\mathfrak{C}_{\mathrm{tr}}$), and proving its first control target (classwise vanishing on the contradiction-relevant transfer subclass) under explicit OP7--OP8 and AC1--AC6 dependency control in one synchronized package.
- Even if that repair target is proved, downstream burdens remain open: no-new-off-line-branch closure, no-alternative-locus closure for all of $\mathcal{B}$, and the master Stage-6 exclusion theorem.

---

## At-a-glance risk board

| Gap | Why it matters (short) | Status | Resolution signal |
|---|---|---|---|
| Exact spectral object | Foundational definitions missing | Open | Full operator construction + well-posedness proofs |
| Zero--balance correspondence | Central equivalence claim | Open | Two-direction non-circular theorem |
| Unique balance axis | Needed to isolate \(\Re(s)=1/2\) | Open | Uniqueness theorem under explicit hypotheses |
| Off-line exclusion | RH requires global exclusion | Open | Global theorem for entire strip |
| Analogy vs theorem | Heuristics cannot close proof | Partial | Formal replacement of heuristic dependencies |
| Operator-theoretic core | Spectral claims depend on it | Open | Domain/symmetry/spectral lemmas proved |
| Analytic-control gaps | Common failure point in RH attempts | Open | Verified convergence/uniformity and contour steps |

---

## Reviewer use

If you are auditing the manuscript, this file is intended to answer three questions quickly:
1. **Where is the argument most vulnerable?** (sections above)
2. **Is vulnerability acknowledged explicitly?** (status fields)
3. **What exact milestone would close each gap?** (resolution criteria)

If you identify an additional unresolved bridge, add it here with the same four fields: **gap, why it matters, current status, resolution criterion**.

*Last updated: 2026-03-27.*
