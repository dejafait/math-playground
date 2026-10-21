# Normal-closure repair — completed source comparison

TARGET: Assess whether replacing L090's literal field by its normal closure can repair (P7), accounting for the exact field prescription and IV Theorem 1.10's degree and ramification inputs (E3)–(E5).
CHECKED: 2026-10-20
DECISION: IMPORT
SEARCH_EVIDENCE: Step364 inspected L090's complete ambient group, pointwise kernels and core calculation, L091's statement/source convention, step350/360/362 source assessments and ATTEMPTS/033–035; fresh exact queries and theorem reads are recorded below. No published repair theorem was identified in the inspected results; no novelty inference.
SOURCE_EVIDENCE: Fresh reading of the April 2020 IV reproduction linked below: Proposition 1.3 pp.11–12; Proposition 1.8(v)–(vii) pp.19–21 with proof cases; Theorem 1.10 pp.22–23, proof (i)–(iii) pp.23–26, downstream (v),(viii) pp.28–31; Corollary 2.2 proof pp.44–46. Milne Fields and Galois Theory v5.10 Theorem 3.17 and Remark 3.18 pp.39–40 were freshly read.
COMPARISON: The source provides a specific field-generation condition and both degree-based and local inputs; finite Galois correspondence covers the closure/compositum method, without establishing changed-field estimates. L090 already supplies the exact finite group and core for a later degree test.
GAP: No repair theorem is imported. Exact repaired-field degrees, actual local inertia/differents, the height-selected prime and independent initial-data outputs remain untested; the original finite B>=A and essentiality gaps remain open.
REASON: The new source import identifies the numerical uses that a changed-field argument must revisit and isolates a bounded degree comparison instead of another fixed-field audit or authentication attempt.
SCOPE: Import only the qualified source requirements and comparison below; the newly proposed degree specialization has its own separate assessment. No normal-closure preservation or impossibility result is established in this literature turn.
LITERATURE_REASON: The changed-field repair needs the previously unread complete uses of (E3)–(E5), outside the ready fixed-F audit scope.

## Completed comparison — step364

The main gap is original finite B>=A. The intermediate target is the
TARGET above. Its downstream use is to distinguish a repairable field
construction from an obstruction to the numerical route. Continue only
with a source-backed test on the same fields; abandon a claimed
essential obstruction if it merely detects a changed presentation or
loss of a sufficient estimate. This turn supplies source coverage,
not a mathematical repair verdict.

### Primary input and proof-use ledger

Read the [April 2020 IV reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf).
Printed pages, not zero-based PDF indices, are used throughout:

- Theorem 1.10, p.22: initial theta-data, III Corollary 3.12, specified
  good reduction, and the exact Legendre-adjunction prescription.
- Proof (i)–(ii), pp.23–24: (E3) gives
  |GL_2(F_p)|=p(p+1)(p-1)^2; (E4) treats p=2,3,5; (E5) bounds
  adjoining i by two. The inclusion into GL_2(F_3) times GL_2(F_5)
  times Z/2 and tameness away from 2,3,5 feed the different/conductor
  increment log(2^11*3^3*5^2)<=21, then the ell-division increment.
- Proposition 1.3, pp.11–12: local finite extensions; its upper bound
  requires a Galois extension over a tame intermediate field, and
  d_i<=d_0+n_i+1/e_0, with n_i=v_p([k_i:k_0]).
- Proposition 1.8(v)–(vii), pp.19–21: prime-to-residue torsion,
  good/multiplicative cases and the Legendre quadratic-extension case.
- Proof (iii), pp.24–26: (D0) and (R1)–(R4); (v), p.28, uses (R4);
  (viii), pp.30–31, absorbs its cutoff by Proposition 1.6.
- Corollary 2.2 proof, p.44: (E3)–(E5) also support [F:Q]<=delta
  in prime selection; pp.45–46 reach (P1)–(P7).

These are all explicit (E3)–(E5) references found in that text;
the two downstream uses above were inspected, not inferred from
search snippets. No audit of the underlying volume argument is claimed.
Screenshots again returned no usable image; continuous text supplied
the readings. The April reproduction remains unauthenticated against
author/journal bytes. ATTEMPTS/035's authentication route stays parked.
The native Galois condition and definitional-reading boundary are
reused from the audited L091 assessment, without a fresh approval loop.

### Standard results, duplicates and remaining difference

[Milne, Fields and Galois Theory v5.10, September 2022](https://www.jmilne.org/math/CourseNotes/FT.pdf),
Theorem 3.17(b)–(d) and Remark 3.18(a),(b), pp.39–40, apply to a
finite Galois ambient extension. They identify degrees with subgroup
indices, conjugate fields with conjugate subgroups, composita with
intersections, and normal closure with the fixed field of the core.
L090 supplies exactly this ambient setting, including the full joint
image and all conjugates. These results should be cited, not reproved;
only their specified degree specialization remains. They do not give
local decomposition/inertia groups or local different exponents.

L090 already establishes the strict field change, with closure index
four. L091 establishes the qualified fixed-field obstruction. Neither
evaluates the closure's degree against the source's distinct bounds.
No duplicate such evaluation was found in the narrowly checked local
records. ATTEMPTS/034's cyclic Frobenius failure and ATTEMPTS/033's
unnecessary classification retrieval are unrelated mechanisms and
remain stopped.

Queries: `Mochizuki "Legendre" "normal closure"`;
`"inter-universal" "Galois closure" "torsion"`;
`"IUT" "normal closure" field Legendre`;
`"Mochizuki" "Legendre" "normal" "closure"`;
`"Theorem 1.10" "Galois" "Legendre"`;
`"IUT" "Legendre" "nonnormal"`.
Results included alternate IV copies and an uninspected formalization
plan. These are leads only; no source beyond the inspected primary
text and Milne is used as a repair theorem. Search failure does not
certify originality. Reuse step350/356/358 for unchanged native-field,
torsion and moduli coverage.

### Bounded continuation and limits

The proposed degree test is in
`drafts/literature/2026-10-20-normal-closure-degree-test.md`.
Keep T=F_tpd distinct from the source's ell-division field. Compare
both the relative torsion-group cardinality and the corollary's
absolute delta: loss of the former need not exceed the latter.
Do not multiply every printed constant by four without a new proof,
and do not deduce a local ramification failure from a global degree.
The degree test can decide whether the original group-size argument
is available, leaving genuine local preservation and all-image/pilot
questions independent. It does not require a new occurrence theorem
or replacement of the height-selected prime by seven.

Full matching/supporting Mathlib coverage remains unchecked; no absence
or formal verification is asserted. No lemma, mathematical script or
new proof dependency was written. PROOF and DAG are unchanged by this
step. STATUS remains IN_PROGRESS, without a complete-solution candidate.

## Invocation-start proposal — historical; completed above

This is a continuation proposal, not a ready assessment. The next turn
is literature-only. No repair theorem or source-scope approval is
derived in step363.

The main gap is still original finite B>=A. This intermediate comparison
could distinguish a repairable construction error from an obstruction
that affects the numerical argument. Keep audited L089, L090 and L091,
the same survivor and closure, all six literal equations, and each
literal G_o distinct from G_o^nor. Preserve c,h,d_*,e_*, both domains,
d=6 and epsilon_d=1. The original Q-curves' images do not supply the
height-selected prime's image.

Read the exact relevant statements and proof uses of (E3)–(E5) before
larger passages, and compare the required degree/ramification controls
with standard Galois-closure and compositum results. Do not assume
that merely taking a normal closure preserves the exact generation
equality, the original constants, local behavior or all initial data.
Conversely, failure of the original equality alone does not prove
that a modified theorem or argument cannot work. No changed-field
estimates or preservation claims have been established here.

Continue only with a source-backed, independently testable later target
on the same specified fields. If the full repair depends on unread
input, name the precise missing claim and select a bounded comparison;
do not start calculations during the approval turn. A persistent source
blocker requires a different independently testable target rather than
another authentication retry. ATTEMPTS/033–035 remain intact.

Reproduction authentication/current-version applicability, alternate
models, independent initial-data outputs, actual native input/action/
factorization/pilot transport and essentiality remain unresolved. Full
matching and supporting Mathlib coverage for this repair is unchecked.
STATUS remains IN_PROGRESS and there is no complete-solution candidate.
