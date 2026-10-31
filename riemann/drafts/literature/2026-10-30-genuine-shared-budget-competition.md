# Genuine shared-budget competition: completed source review

TARGET: Seek an exact rational symmetric two-pair block with all-real positive aggregate and individually feasible full budgets, but no conserved four-constant allocation.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the completed exact-family source comparison and scoped failure records; new decomposition, fractional-residue, individual-compensation and semi-infinite Farkas searches are listed below. No inspected result settled the strengthened comparison; no novelty inference is made.
SOURCE_EVIDENCE: Reuse Csordas https://arxiv.org/html/1309.0055v2 Proposition 2.2 (2.3)/Proposition 2.3, Tyaglov https://arxiv.org/html/0902.0413v3 Theorem 4.1 and Katkova–Tyaglov–Vishnyakova https://arxiv.org/html/2406.00686v1 Theorem 2.2/Section 6 as assessed in 2026-10-30-shared-budget-allocation-comparison.md; newly read Boyd–Vandenberghe, Convex Optimization (2004; corrected seventh printing 2009), Section 5.8.2–5.8.3 pp. 260–263, https://www.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf, and Lopez (2026), Sections 6.3–6.4 Definition 14/Theorem 15/Example 16, https://link.springer.com/article/10.1007/s11750-026-00713-w.
COMPARISON: L510 fails the added individual full-budget test. The reused identity/count theorems do not supply prescribed fractional allocations even on this subfamily; their extra derivative hypotheses are not inferred from individual compensation. Finite linear alternatives supply a certificate tool, not a decomposition or a separating block. No inspected source forces equivalence or supplies the desired example.
GAP: Produce exact all-real individual and aggregate certificates together with a joint four-constant infeasibility certificate, or obtain an informative obstruction in the single bounded slice test below; no example or structural implication is established here.
REASON: This separate literature-only review completes coverage of the saved strengthened target. One capped constraint-driven slice attempt is justified; the unchanged grid, single-pair deficit and further source-approval loops are not continuations.
SCOPE: K_c(x)=2((x-c)^2-1)/((x-c)^2+1)^2 for c=+/-h; h,r rational and positive; real x!=+/-r; four nonnegative constant allocations and the two original unit budgets. No Xi realization, infinite transfer, higher-sign theorem or simple-zero hypothesis is asserted.
LITERATURE_REASON: The added individual full-budget acceptance condition was REVIEW_REQUIRED at invocation start; the completed broader-family assessment did not separately compare this joint-only target.

## Prior nomination and acceptance requirements (preserved)

Use the definitions and qualifications of L510. In this changed target,
require H(x)>0 throughout its domain and, independently for each c,

    K_c(x)+1/(x+r)^2+1/(x-r)^2 >= 0

for every such x. These individual tests are additional acceptance
requirements, not premises already verified for any parameters.
The desired separation would exclude every four-constant allocation
with alpha_h+alpha_{-h}<=1 and beta_h+beta_{-h}<=1, using the same
nonnegative pairwise expressions as L510. No symmetry reduction of
the constants is assumed in the nomination. No new polynomial or
mathematical script for this target has been written.

Essential prospective local inputs are L510's definitions and audited
limitation, L509's exact isolated-pair benchmark (read its relevant proof
before use), and the existing shared-budget source comparison. L251/L257
are duplication contrasts, not established solutions to this target.
No cross-notebook input is proposed. Mathlib coverage remains unchecked.

The nomination requested review of the primary theorem hypotheses and applicable proof cases only
where the existing records do not cover this added requirement. Check
for a known decomposition theorem or a joint-feasibility obstruction
before choosing a finite test; reuse ready unchanged source evidence.
The preceding nomination performed no source review. The completed
review below supersedes its pending gate. If the target is known or
impossible for a structural reason, import that conclusion rather than
manufacturing a new example. Otherwise the source review should fix one
bounded nonredundant test before mathematics resumes.

Downstream use is to distinguish genuine conserved-resource loss from
L510's individual geometric deficit. Even a certified example would
leave actual-Xi geometry, unmatched-pair mass, convergent assembly and
all higher signs unresolved. Continue only with exact full-domain
individual feasibility and an essential joint-budget contradiction;
abandon any candidate with a one-pair full-budget deficit or failed
aggregate sign. Preserve informative failures; no automatic mesh
refinement or repeated approval loop is proposed.

## Completed comparison, 30 October 2026

This is a literature-only EXPLORATION, not a new mathematical result.
The main gap remains actual-Xi all-degree positivity. The intermediate
target distinguishes joint conservation from individual geometric
deficits; its downstream use is to decide whether this sufficient
pairwise assembly loses collective cancellation even after each pair
is separately compensable. Xi geometry, unmatched mass, convergent
assembly and higher signs are independent gaps.

### Reused theorem coverage and local exclusions

The [completed broad-family assessment](2026-10-30-shared-budget-allocation-comparison.md)
already inspected the three arXiv theorem statements and relevant proof
cases. Its h,r>0 scope includes the strengthened subfamily, so those
unchanged source passages were not retrieved again. Csordas supplies
the signed identity for the finite polynomial P recorded there, with
nonzero P(0) and strip hypotheses; his interval sign conclusion requires
an interval excluding nonreal centers. Tyaglov counts aggregate zeros;
Katkova–Tyaglov–Vishnyakova impose the additional real/simple derivative
zero conditions recorded there. No implication from individual
full-budget compensation to those derivative conditions is asserted.
None of these statements constructs prescribed fractional allocations.
The earlier Cardon and Tyaglov–Atia comparisons remain adequate contrasts;
their all-order or real-rooted hypotheses do not decide this problem.

Read L510's hypotheses, limitation and complete infeasibility argument:
its one-pair full-budget deficit is disallowed here. Read L509's
statement and relevant single-pair reduction/domain proof; it places
real charges symmetrically about one center, unlike the shifted pairs
here, and cannot be substituted as this family's feasibility test.
The earlier L251/L257 masking comparison is reused; it is not a joint
allocation result. The shared-budget recovery stop and grid working
record retain the single-pair mechanism, 341 exact-test points and 158
unresolved earlier points. None of those unresolved cases is evidence
of feasibility. L354/L471 failures remain as assessed previously.

### New primary certificate source

Boyd and Vandenberghe, *Convex Optimization*, Cambridge UP, 2004,
corrected seventh printing 2009, [Section 5.8.3, pp. 261–262](https://www.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf#page=275),
give strong alternatives for finite real A,b: Av<=b is infeasible iff
there exists lambda>=0 with A^T lambda=0 and b^T lambda<0. Read the
preceding Section 5.8.2 attainment qualifications and the finite-linear
case, plus the homogeneous Farkas proof on p. 263. For a future fixed
rational parameter and finite rational evaluation set avoiding poles,
the two pair inequalities, both budgets and nonnegativity constraints
are finite affine inequalities in four real constants. This is the
intended applicability of the cited finite theorem. An exact witness
must give the actual matrix, vector and multipliers. No certificate or
existence conclusion is derived now. No reproof is needed, and no
finite-sample feasibility conclusion will certify an all-real sign.

Marco A. Lopez, *A brief tutorial on semi-infinite optimization: the
model, applications and basic mathematical constructions*, TOP,
published 2 April 2026, [Sections 6.3–6.4](https://link.springer.com/article/10.1007/s11750-026-00713-w),
defines the characteristic cone in (22)–(23). Definition 14 requires
its closedness for the Farkas–Minkowski property. Theorem 15 assumes
a consistent system with that property to obtain finite-subsystem
consequences; Example 16 exhibits a consistent non-FM system with a
linear consequence absent from every finite subsystem. Read these
statements and the closure-sensitive formulas/proof in Theorem 12 and
Corollary 13. No FM hypothesis or semi-infinite duality theorem is
imported for our block. The tutorial's referenced original FM literature
remains unread and nonessential: the proposed certificate uses only
the finite theorem above, without claiming a complete reduction.

The Stanford web-host PDF initially timed out; its www-host copy
provided the complete relevant text. Screenshot requests timed out;
the formulas above were available in the text. The DOI redirect failed
but the direct Springer article provided the relevant full text. These
are resolved retrieval issues, not persistent essential source blockers.

### New bounded search evidence

Queries actually issued, in addition to reusing the earlier exact-family
searches, were:

- `"Laguerre inequality" "decomposition" "real zeros"`
- `"logarithmic derivative" "fractional" "allocation" zeros`
- `"nonnegative rational functions" "prescribed poles" decomposition`
- `"Laguerre" "inequality" "individual" "pairs" zeros`
- `"Laguerre inequality" "decomposition" fractional zeros`
- `"logarithmic concavity" "rational" "residues" decomposition`
- `"semi-infinite linear" "Farkas" finite infeasibility certificate compact`
- `Boyd Vandenberghe convex optimization Farkas lemma 5.8.3 alternative`

Results included the previous Laguerre literature, unrelated allocation
and orthogonal-polynomial material, and finite/semi-infinite optimization
sources. No exact-match theorem was inspected. Search snippets, informal
RH posts and secondary copies are not theorem evidence. The additional
generalized conic/infinite-duality leads were not read and are not
essential to this finite-certificate attempt. Failure to find a match
does not certify originality. Mathlib coverage remains unchecked.

### One bounded test for the same target

Keep h=11/16 from L510 and vary only rational r in [1,21/16), starting
with r=5/4. The proposed new discriminator is whether repairing the
individual full-budget deficit leaves an independently certifiable
joint-budget obstruction. No ordering of these transitions is assumed.
This is a constraint-driven slice test, not another two-dimensional
mesh or a claim that this slice must contain a separation.

Cap the attempt at eight rational r candidates (reduced denominator
at most 4096), at most 32 added rational pair-evaluation rows per
candidate, and stop on the first fully certified example. Choose later
candidates from observed constraint conflicts/individual-sign failures,
recording the reason for each choice; do not enumerate a finer grid.
Numerical minimization or LP may nominate parameters and test points,
but every accepted claim requires exact rational algebra. No sweep was
run and even the initial candidate's signs are unverified.

For any proposed success certify H>0 and both full-budget expressions
>=0 on the entire punctured real line, by exact polynomial inequalities
with justified denominator signs, poles and both tails. Supply the
four-variable finite matrix and exact nonnegative multipliers with
strict negative dual value; include the two original budgets and all
four nonnegativity constraints. Use both pair groups essentially in
the contradiction, retaining the individual certificates to exclude
the L510 mechanism. No symmetry reduction is assumed. If used, any
reduction must be proved during research and checked against the
original four-variable inequalities.

Save full bounds, nominated/rejected candidates, exact certificates,
failures and unresolved cases in the active notebook. A numerical
preview, failed search or feasible finite LP proves neither global
feasibility nor equivalence. Report EXPLORATION without a verified
advance or informative obstruction. Stop at the cap, preserve partial
reasoning and require a materially new input before another attempt.
Changing h, reopening a mesh or proving a general decomposition theorem
is not covered by this bounded continuation.

Coverage is now EXPLORE for the unchanged saved target and this bounded
test. No lemma, mathematical script, new symmetry theorem, actual-Xi
claim or general structural implication was produced in this review.
No justified creative central-gap mechanism is currently available:
the missing actual-Xi geometry/unmatched-mass bridge remains the blocker.
