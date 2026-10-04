# Residual residue-20 ancestor selector: completed scope assessment

TARGET: Review the refined residue-20 ancestor selector to determine whether its guarded reductions supply a smaller positive residue-20 coalescing start for roots with v_3(n+7) in {3,4}, with every comparison made against the original root.
CHECKED: 2026-10-04
DECISION: IMPORT
SEARCH_EVIDENCE: Five exact-statement and stronger-result queries were executed on 2026-10-04; the direct source and its essential retained-branch reference were read, rather than treating snippets as coverage; queries and reuse limits appear below.
SOURCE_EVIDENCE: Read Sodelin's Residue20_Refined_Ancestor.md, sections 1–6, all 239 web lines, https://raw.githubusercontent.com/Sodelin/Collatz-Conjecture-Work/main/proof-search/lemmas/Residue20_Refined_Ancestor.md; read the retained construction and its proof in Residue20_Valuation_Ancestor.md, sections 1–7, and supporting inverse-word semantics, sections 1–5; inspected the public Lean statement and declaration linked below.
COMPARISON: The guarded theorem supplies smaller ancestors on a proper subfamily of L014's residual domain; the source explicitly retains uncovered cases, so it cannot be imported as a selector on every residual root.
GAP: The full residual termination claim remains open; the narrower least-root citation application and the inspected lower-row exclusions are ready, while no universal transition or return rank is covered.
REASON: Complete the essential unread-proof comparison and use its covered partial conclusion by citation; do not extend its guards or reprove general inverse-word arithmetic.
SCOPE: Positive shortcut roots, unchanged original-root comparisons, the uniform valuation-at-least-13 ancestor theorem and the source's individually guarded lower rows; IMPORT concerns their stated scope, not universal residual coverage.
COVERED_TARGET: Import by citation the refined residue-20 ancestor theorem to show that a least nonconvergent residue-20 root n satisfies v_3(4n+1)<=12, checking its positive-integer hypotheses and convergence transfer against the original root.
COVERED_TARGET: Apply the inspected branch thresholds below valuation 13 to a least nonconvergent residue-20 root, recording only the guarded exclusions and keeping every size comparison against the original root.

## Hypotheses

Use the positive shortcut map and nonconvergence conventions already
recorded in foundations/01-target-and-scope.md and L014. This review
keeps its original TARGET unchanged. It does not assume that a bad root
exists, or replace a fixed root by a larger returned value.

## Conclusion

The scope comparison is NEGATIVE evidence against whole-class use,
classified KNOWN_IMPORTED. The narrower application is ready for a
RESEARCH turn. This turn imports source coverage and qualifications;
it derives no new theorem and does not carry out that application.

## Proof

This section records what was read, not a new proof.

Sodelin, *Refined tail certificates lower the uniform ancestor cutoff to
valuation 13*, node `B-RESIDUE20-VALUATION13-ANCESTOR-2026-09-05`,
[sections 1–3](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Residue20_Refined_Ancestor.md#1-common-prefix-and-the-retained-five-branches),
states: if r>0, r=20 modulo 27 and v_3(4r+1)>=13, some positive
m=20 modulo 27 has m<r and T^b(m)=r. Its variable prefix and five
refined guards were read in full. The guards on z are 38 or 65 modulo
81, or 11, 92 or 173 modulo 243. The proof checks every odd inverse,
reverses the inverse word for the forward identity, and bounds the
slope by 192(2/3)^v with a negative intercept. Its exact threshold
comparison is 192*2^13<3^13, with no unit-size cutoff.

[Sections 4–5](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Residue20_Refined_Ancestor.md#4-sharpness-and-boundaries)
give the selector's v=12,u=13 failure: r=1,727,183 and its selected
m=2,555,840>r, although T^18(m)=r. Sharpness concerns that selector.
The source's conditional least-root restriction is v_3(4r+1)<=12;
it supplies no termination theorem for the remaining roots.

The five retained rows were not accepted on cross-reference alone.
Read *An explicit smaller residue-20 ancestor for every sufficiently
deep 3-adic root*, node `B-RESIDUE20-VALUATION-ANCESTOR-2026-09-05`,
[sections 1–4](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Residue20_Valuation_Ancestor.md#1-definitions-and-exact-construction).
Its t=1,2,5,7,8 rows have thresholds 13,7,11,4,11 respectively.
The proof checks positive intermediate integers, the exact variable
prefix, target membership and strict order for arbitrary units. Its
[sections 5–7](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Residue20_Valuation_Ancestor.md#5-relation-to-the-previous-normalizer-and-its-self-loop)
identify covered roots as v_3(r+7)=3 and expressly leave root 425
uncertified. Thus this mechanism differs from L014's internal
predecessor, but does not remove the whole residual class.

Supporting semantics were read in *L4 — General inverse-word coalescence
semantics*, dated 2026-08-23,
[sections 1–5](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/L4_General_Inverse_Word_Coalescence.md#1-accelerated-collatz-map).
Every intermediate odd inverse requires its own admissibility guard;
an integral final affine formula alone does not certify the trajectory.
This supporting theorem does not supply universal selector coverage.
Reuse the adequate Rozier and Monks coverage in the
[prior assessment](2026-10-03-residue20-first-return-descent.md);
neither result replaces the size comparison sought here.

### Provenance and formal scope

The three prose notes were read from live `main` on 2026-10-04, with
239, 285 and 291 web lines respectively. Their node dates identify the
notes, not immutable revisions. No current commit hash was obtained.
The proof of the relevant prose statement and its essential reference
are accessible; there is no source blocker.

Read [ResidueAncestorStatement.lean](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/lean/CollatzWork/ResidueAncestorStatement.lean),
definitions `ResidueAncestorStatement` and
`ResidueAncestorDivisibilityStatement`, and
[ResidueAncestor.lean](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/lean/CollatzWork/ResidueAncestor.lean),
including `CollatzWork.residueAncestor` and
`CollatzWork.residueAncestor_of_divisibility`. The latter public statement
requires only 3^13 dividing 4r+1 and concludes a smaller positive
residue-20 ancestor with its actual forward identity. Read the relevant
prefix declaration
[`CollatzWork.rootDescentAncestor`](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/lean/CollatzWork/RootDescent.lean#L132)
and the formal-scope paragraphs in
[LEAN_TARGETS.md](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/LEAN_TARGETS.md#complete-residue20-ancestor-theorem).
The named prefix result is supporting; the public ancestor declaration
matches the uniform guarded conclusion. No local Lean build or audit of
all formal imports was performed. The future informal application can
cite the fully read prose proof; it does not depend on independently
validating the repository's kernel-check claim. The sharper lower rows
are outside that public formal statement.

### Search, reuse and relevance test

Queries executed:

- `"Collatz" "refined ancestor" "residue" 20`
- `"Collatz" "v_3" "n+7" ancestor`
- `Collatz "20 modulo 27" "smaller" ancestor theorem`
- `Collatz "3^13" "4*r+1"`
- `"Residue20_Refined_Ancestor" valuation proof`

Search hits also identify complementary-cylinder and later return
results. Their theorem proofs remain unread and are not inputs or
essential dependencies of this selected application. General claimed
Collatz resolutions in other hits were not assessed. A failed broader
search does not imply novelty. This is a bounded exact-source review,
not an exhaustive literature audit.

The downstream use is a further conditional restriction on a least
bad root. The next application needs only a precise citation, matching
positive-integer hypotheses, and convergence transfer from the smaller
allowed start. A mismatched map, guard or original-root comparison
would reject that application. Do not reconstruct the entire selector
or run larger replays without a concrete discrepancy. Even success
would leave an infinite complementary class; reaching or descending
from that class remains an unresolved later step.

The existing two stopped mechanisms in Attempt 010 and the exhausted
paired batch in Attempt 009 are unchanged. Literature spends no
mathematical exploration turn and resets no counter. No new lemma,
mathematical script or candidate argument was produced.

## Mathlib

Full selector and supporting coalescence/congruence coverage in Mathlib:
**not checked**. The external Lean declarations named above are not
Mathlib coverage claims. No library absence is inferred.
