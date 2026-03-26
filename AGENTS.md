# AGENTS.md

## Repository purpose
This repository hosts a **proposed proof framework** for a spectral-coherence approach to the Riemann Hypothesis.

Primary objective:
- Maintain high-quality materials for **mathematical audit**.

Secondary objective:
- Improve clarity of definitions, claims, dependencies, and unresolved steps for expert review.

Non-objectives:
- Publicity writing.
- Certainty signaling beyond what is formally established.

Use framing such as:
- “proposed proof framework”
- “manuscript under review”
- “materials for mathematical audit”
- “the argument attempts to show …”
- “the framework suggests …”

## Writing style
Use a sober, precise, respectful tone.

Preferred style:
- Define terms before use.
- State assumptions explicitly.
- Separate what is proven, conjectured, numerically observed, and heuristic.
- Prefer short declarative sentences over rhetorical flourishes.
- When uncertain, state uncertainty directly.

Avoid:
- Dramatic or triumphant language.
- Marketing or visionary language.
- Claims of inevitability (“must,” “undeniable,” “settled”) unless formally justified.

## Mathematical rigor rules
For any technical change, preserve a clear distinction among:
1. **Heuristic intuition** (motivation, geometric/physical analogy, informal guidance).
2. **Formal claims** (definitions, lemmas, propositions, theorems, with hypotheses and logical dependencies).
3. **Unresolved bridges requiring proof** (explicitly marked gaps, reduction steps not yet established, computational evidence not yet converted into proof).

Rigor requirements:
- Do not present heuristic arguments as proofs.
- Mark every unresolved step with concrete dependency language (e.g., “requires proof of X under assumptions Y”).
- Preserve claim traceability: each major claim should point to where it is justified.
- Do not invent citations, references, theorem attributions, or historical claims.
- If a citation is missing, write “citation needed” or equivalent neutral placeholder.
- Computational checks are supporting evidence, not substitutes for proof.

## Prohibited claim language
Do **not** use phrases such as:
- “RH is solved”
- “final proof”
- “definitive proof”
- “history changed”
- “case closed”
- “complete resolution”

Do **not** imply certainty that exceeds the manuscript state.

When describing results, prefer qualified language:
- “The argument attempts to establish …”
- “The framework suggests …”
- “Under these assumptions, the claim would follow …”
- “This remains an open bridge …”

## File-specific notes

### `docs/*`
- Audience-facing documentation must remain conservative and audit-oriented.
- Keep summaries aligned with manuscript content; do not overstate.
- FAQ and overview pages should include explicit caveats where arguments are incomplete.
- Avoid promotional framing, badges, hype copy, and calls to virality.

### `manuscript/*`
- Treat as primary formal record.
- Maintain strict separation between definitions, proven statements, heuristics, and limitations.
- Ensure theorem statements include hypotheses; avoid implicit assumptions.
- If modifying proof flow, update dependency references and limitations sections accordingly.

### `notes/*`
- Use for candid research-state tracking: open questions, known gaps, objections, and review feedback.
- Prefer explicit status labels such as “open,” “partial,” “blocked,” “needs formalization.”
- Do not silently remove unresolved issues; if resolved, document where resolution is recorded.

### `.github/*`
- Keep templates/workflows aligned with mathematical review quality.
- PR/issue templates should ask contributors to identify: claim type (heuristic/formal/open bridge), affected assumptions, and evidence type.
- Avoid automation or template text that implies the proof is complete.

## Review checklist
Before finalizing any change, verify:
- [ ] No overclaiming or hype language.
- [ ] Heuristic intuition, formal claims, and unresolved bridges are clearly separated.
- [ ] New or edited claims include assumptions and dependency context.
- [ ] Limitations and open gaps remain visible where relevant.
- [ ] No invented citations or references.
- [ ] Documentation and manuscript language are mutually consistent.
- [ ] Tone is calm, mathematically serious, and audit-friendly.

## Agent behavior expectations
For future Codex tasks in this repository:
- Default to conservative phrasing when uncertainty exists.
- Prefer adding explicit caveats over polishing rhetoric.
- If asked to produce publicity-style text that overstates certainty, provide a restrained alternative that matches this policy.
- Preserve mathematical humility at all times.
