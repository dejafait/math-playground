# Synchronized translation witness-cover test

TARGET: Test a synchronized quadratic-translation witness-cover mechanism for L131's fixed maps at retention threshold 1532496 per side.
CHECKED: 2026-10-26
DECISION: EXPLORE
SEARCH_EVIDENCE: The completed universal-density comparison in 2026-10-26-mixed-core-rank-supersaturation.md records eight queries and the checked local failures; no inspected theorem provides this fixed-map witness-cover test. This is a proposed finite diagnosis, not a claim that the orbit has any useful expansion.
SOURCE_EVIDENCE: Directly read https://arxiv.org/pdf/2304.09445v3 Definition 2.5/Lemma 2.7 and its proof, printed pp. 7–8, and https://arxiv.org/pdf/1911.01502v1 Lemma 4.3 and its common-root division proof, printed pp. 11–12; reuse L031's audited specialization. L030 supplies the auxiliary family and L131 the fixed maps. The companion comparison supplies no applicable finite cover bound.
COMPARISON: L131 supplies one full-rank witness at the zero translation, while L130 supplies no witness survival. The new task tests only a specifically defined enlarged witness collection for L131's maps; it does not quantify over all labelings or claim a packed counterexample from an orbit cover.
GAP: Determine whether exact Boolean deletion sets of at most 1038857 indices on each side hit every accepted synchronized witness, or obtain an exact infeasibility certificate. A merely fractional feasible point, a sampled absence claim or a failed solver is inconclusive.
REASON: This bounded rank-sensitive coverage test can reject an insufficient amplification of the known embedding before a difficult uniform supersaturation proof is attempted; success would provide only a fixed-map intermediate input.
SCOPE: Use unchanged E/F/H/k, T, q=137, p=0, r=Z-16, K,a,b,C,C',sigma,sigma' from L031/L131, and all auxiliary quadratic coefficient triples. No maps, core or field parameters may be changed during this attempt.
LITERATURE_REASON: Supervisor recovery requires a direct primary source URL in this ready assessment; repair that omission and verify the cited statements, without repeating the completed broad search or changing the research target.

## Direct-source recovery review — 2026-10-26

Both version-pinned PDFs above were accessible through the web reader.
AGL v3 (26 July 2023), Definition 2.5 specifies positive and negative
Vandermonde blocks over a finite-field rational function field. Lemma
2.7 assumes distinct scalar RS codewords agreeing with one center and
shows that their specialized reduced intersection matrix lacks full
column rank; its proof uses coefficient differences from the last
message. Theorem 2.9, printed p. 9, concerns rank over the rational
function field, not rank at our fixed labels. No translation-invariance
or finite cover conclusion is imported from it.

Shangguan–Tamo v1 (4 November 2019), Lemma 4.3 concerns three codewords
and a determinant obstruction to list decoding. Its proof divides
message differences by the polynomial with their common agreement
points as roots, then records the residual vanishing equations.
Only this common-root step supports the existing specialization; its
three-codeword theorem is not asserted to be our four-support criterion.
L031 already proves the fixed-domain, extension-field and tuple-width
qualifications. That proof, rather than an unsigned characteristic-two
matrix, remains the canonical input. No reproof is needed in the test.

The main unresolved claim remains arbitrary-center 67/68 agreement
safety. The intermediate target and downstream use are unchanged:
diagnose whether this one fixed-map orbit has enough rank-sensitive
coverage to merit a later uniform forcing argument. An exact cover
within both budgets abandons this orbit-alone amplification; exact
threshold forcing or a materially refined structural obstacle permits
continuation, with arbitrary maps and global RS transfer still open.

The companion assessment's recorded duplicate/failure comparison was
reused. A narrow reread of ATTEMPTS/031–032 confirms that their stopped
targets are single-core common-shift/five-block cap tests, not this
two-core four-support orbit. Their deletion obstructions remain relevant
warnings; this review neither overturns them nor establishes expansion.

This is a process repair, not a new mathematical result or fresh broad
literature comparison. DECISION remains EXPLORE with the exact same
scope and certificate requirements. No lemma or mathematical script was
written. Full/supporting Mathlib coverage remains not checked. The
missing direct-URL issue is repaired; the next action is mathematical,
subject to the supervisor's gate.

## Proposed finite experiment — no conclusion established

Let Q be the q^3 auxiliary polynomials of degree at most two. For every
f in Q consider the four candidate supports, in order,

    C union sigma(B_f), C union sigma(B_(f+r)),
    C' union sigma'(B_f), C' union sigma'(B_(f+r)).

This defines the proposed synchronized orbit; it does not assert that
translation preserves actual intersections or rank. The actual maps
are the complete fixed L131 maps, not field homomorphisms. Enumerate
each f once in coefficient order. Keep a candidate only after checking
L031's complete hypotheses at the original actual labels: the common
60-core is K, all six pair-only sets have size two, all four private
sets have size two, and these eleven sets are mutually disjoint.
Build its signed 12-by-12 matrix over E exactly as in L031; keep a
witness only when its rank is twelve. Do not infer rank from incidence
or from the zero-translation example. Singular candidates are not
asserted realizable and are simply outside this selected mechanism.
The zero-translation witness is the imported L131 consistency check.

Use separate left and right copies of Q as the vertex sets. Each
accepted f supplies the constraint that the four vertices
L_f,L_(f+r),R_f,R_(f+r) may not all be retained. Test whether deletion
sets D_L,D_R can hit every such witness with

    |D_L| <= 1038857, |D_R| <= 1038857.

These are L130's recorded per-side deletion budgets relative to
q^3=2571353 and required retention 1532496. A success must exhibit
exact sets (or complete finite rules) with all witness hits verified.
This rejects only forcing by this synchronized orbit without further
constraints. It is not a pair of packed families: pairwise packing
across sides is not imposed in this preliminary cover test. No
counterexample to the reviewed universal assertion follows unless
all its packing conditions and all its possible witnesses are checked
in a separately assessed task.

An exact infeasibility certificate would show that every two retained
index sets at threshold contain a witness from this orbit, for these
maps, even without adding cross-packing assumptions. A rational dual
may certify that claim if its full inequality is verified. Solver
status or floating-point infeasibility alone cannot. This would still
leave arbitrary maps, quantitative global transfer and RS safety open.

## Bounded work and continuation test

One research step may enumerate the q^3 candidates, with fast exact
incidence rejection before rank, and attempt a direct cover construction
or a verifiable finite certificate. If a structural argument settles
the cover before enumeration, write that proof instead. Do not expand
to independently translated left/right parameters, new maps, other
orbits or general rank-free families within this scope. Save partial
reasoning and any certificate before lengthy work; a resource limit
is not mathematical evidence.

Continue this synchronized mechanism only if threshold-forcing is
certified, or a concrete structural obstacle yields a materially refined
test. An exact cover within both budgets abandons this orbit-alone
amplification. It leaves the broader rank-sensitive mechanism open and
requires a different, separately reviewed amplification rather than
repeating the same calculation. Inconclusive output remains EXPLORATION
or STALLED as appropriate; do not create a lemma to count the attempt.

Any later script must save full accepted witnesses, exact ranks and
verification data, rejection counts by reason, complete deletion sets
or dual weights, actual/required sizes, failures and input linkage under
scripts/finite-support/. Print only bounded summaries and paths. Use
the shared JSON inspector for selected complete load-bearing evidence;
a preview never verifies the cover. L131's maps and L031's original
rank certificates remain read-only inputs. New ranks need their own
exact evidence and cannot be imported from L131.

Full/supporting Mathlib coverage: not checked. Classification for the
future attempt: POTENTIALLY_NEW only in the limited assessed-search
sense, not certified originality. Appropriate initial routing is
calculation/standard/high; this finite specialization is not a protected
creative proof attempt. Separate supervisor approval is required for
this newly written ready continuation, without rejecting the completed
source review. No lemma or mathematical script is written this turn.
