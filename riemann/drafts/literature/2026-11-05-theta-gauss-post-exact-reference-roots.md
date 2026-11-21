# Actual two-node post-exact reference — completed source comparison

TARGET: Determine whether the actual two-node Gaussian reference Q_(2,5) has five simple positive zeros, with rigorous coefficient/root certification and without common interlacing.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step550 searched Gaussian-quadrature/Jensen, two-point Jensen and dilated-Laguerre root terminology; checked the named local theta assessments, L795/L805/L807, prior stops and certificate provenance. Exact queries, inspected sources and access limits are recorded below; no novelty inference.
SOURCE_EVIDENCE: Becker–Sagraloff–Sharma–Yap, arXiv:1509.06231v4 (8 November 2016), Definition1,(3)–(4),Theorem1,pp12–13 and Section3.3,pp15–18, https://arxiv.org/pdf/1509.06231v4 ; DLMF1.10(iv),1.11(ii),3.8(iii); reused Gautschi/DLMF quadrature and GORZ Theorem2 coverage.
COMPARISON: Known low-degree Jensen hyperbolicity concerns actual P_5, not its non-exact two-node reference. L805 stops common interlacing of the cubics; L807 supplies an error sign, not reference roots. Standard finite root certification covers the method, but no inspected result settles this particular weighted reference.
GAP: Construct and enclose the six coefficients from the audited actual two-node rule, then certify or refute five simple positive roots. Input enclosures exist; their quantitative sufficiency for this decision is untested. No root conclusion is claimed here.
REASON: The previously missing root-certification input is now available without a simplicity assumption or an arbitrary-precision theta oracle; one conventional finite application can test this prerequisite. Root geometry alone leaves alternating margins and degree-uniform mixed-positivity transfer unpaid.
SCOPE: Approves only the unchanged TARGET using L019/L021/L795, audited L805 and L807 definitions; one coefficient construction and bounded root certification with inherited enclosures. No new theta evaluation, degree sweep, common-interlacer retest, fitted measure or cross-notebook input. Intended research classification REPRODUCTION. Newly ready continuation remains subject to the supervisor's separate approval next turn.
LITERATURE_REASON: The invocation-start assessment was REVIEW_REQUIRED; essential finite-root certification and exact-reference overlap coverage were missing. Existing quadrature and known-Jensen coverage was reused, not researched again.

## Original nomination, retained

The following nomination predates the completed step550 comparison.
Its pending-gate language is historical; the fields above and completed
comparison below record the present source decision.

The main gap is still actual-Xi all-degree mixed positivity. This
proposed finite test asks whether the first nontrivial two-node
post-exact reference even has the root geometry needed for a possible
signed comparison. It differs from the failed common-interlacing
premise: the weighted reference itself is the object, at degree five,
and no interlacing of its individual summands is requested.

Essential local definitions and inputs are L019/L021/L795 for the law
and normalization, L805 for the actual two-node rule and its qualified
node/weight certificate, and audited L807 for the error's scope.
Recheck the provenance and adequacy of any numerical enclosures before
their mathematical use; this nomination imports no certificate value.
Reuse the existing known-Jensen comparison, but distinguish actual
P_5 from the quadrature reference, since degree five exceeds n=2's
degree-three exactness. Seek exact statements and stronger conclusions;
do not infer novelty from an unanswered search.

If a later approved certification establishes five simple positive
zeros, it supplies only reference geometry; alternating sign margins,
other n and transfer to actual mixed positivity stay open. A certified
nonpositive or nonreal zero would stop this reference-hyperbolicity
premise for the proposed family, without refuting P_5 or RH. An
inconclusive enclosure must be reported as such, with a bounded
refinement or a changed mechanism, not counted as a root conclusion.
Full matching Mathlib coverage is unchecked.

This is a conventional finite prerequisite, not a justified creative
mechanism at the central gap. No degree-uniform signed transfer or
independent alternating margins have been specified. Preserve that
blocker instead of relabeling root certification as creative work.
The next turn must conduct the missing literature comparison; no
calculation of Q_(2,5) was performed here.

## Step550 source-review checkpoint, now completed

Reused the ready Gautschi/DLMF and GORZ comparisons; read L795's
normalization, L805's complete finite construction/audit and L807's
definitions and conclusion. A targeted search of the theta assessments,
ATTEMPTS, history and scripts/theta-gauss found only this nomination
for the degree-five reference, not a prior certificate. Inspected the
complete selected independent node/weight boxes and provenance hash
map in audit-certificate-542.json, retaining its inherited evaluator
and Decimal contracts. These are usable finite input enclosures;
their sufficiency to decide roots has not been tested. No coefficients
or roots of Q_(2,5) have been computed.

The unfinished checkpoint recorded a missing root-counting source and
an unread Craven–Csordas lead. Both are resolved by the comparison
below. No coefficient/root calculation was performed during the review.

## Completed comparison — step550, 5 November 2026

### Relevant known results, exact scope and prior failures

Reuse [the completed quadrature comparison](2026-11-05-theta-gauss-compressed-interlacing-scope.md)
and [the finite audit assessment](2026-11-05-theta-gauss-two-node-audit.md).
They cover Gautschi, *Orthogonal Polynomials: Computation and
Approximation*, OUP2004, Theorems1.6/1.19/1.45/1.46,
pp1–3/7/21–23, and L795's DLMF18.5.12 normalization. No general
quadrature theorem needs reproof. L805's actual raw-v node polynomial
is determined by moments through t_3; its nodes and weights are those
used in L807's definition of Q. This identifies the available inputs,
without expanding or evaluating the degree-five reference.

Reuse [the known-Jensen comparison](2026-11-05-central-hermite-theta-gram.md),
known-degree section: Griffin–Ono–Rolen–Zagier,
[*Jensen polynomials for the Riemann zeta function and other sequences*,
1902.07321v2](https://arxiv.org/pdf/1902.07321v2), Theorem2,(1)–(2),
Section5.2, covers degrees1–8 at every nonnegative integer shift.
Its recorded factor8 normalization cancels in P_d. This already covers
actual P_5; the cited theorem does not identify P_5 with Q_(2,5).
Degree five exceeds the two-node rule's degree-three exactness.
No fresh audit of GORZ's computation or manuscript is claimed.

A new search lead was inspected: Thomas Craven and George Csordas,
[*The Wright functions and Laguerre multiplier sequences*, author copy](https://math.hawaii.edu/~tom/mathfiles/wright-l.pdf),
undated copy inspected 2026-11-05, Section3, pp8–10, Theorem3.3,
Lemma3.5 and its full proof. Their stability means zeros in the open
left half-plane. Lemma3.5 treats the explicit Jensen coefficients
binom(n,k)(k!)^2/(2k)!, using a Chebyshev derivative polynomial and a
reciprocal-Gamma multiplier. This is neither the actual two-node
moment-weighted polynomial nor a positive-real-root conclusion.
No application of that multiplier theorem to the theta rule is made;
following its ancillary Chebyshev references is unnecessary for this
scope exclusion. Later theorems about different entire functions are
not imported.

Local duplicate/failure searches were restricted to
`drafts/literature/2026-11-05-theta-*`,
`ATTEMPTS/2026-11-05-theta-*`, `history/2026-11-05-theta-*` and
`scripts/theta-gauss`. Read the two-node-interlacing ATTEMPTS record
and the relevant canonical proof/audit passages. Only the nomination
was found for this exact root question. Preserve L795's full-support
interlacer stop, L796's Favard stop, L805's finite cubic pair stop
and the derivative-sign-only stops. Failure of a sufficient interlacing
premise neither decides this particular weighted reference nor bans a
new independently testable reference-root question. No source absence
or originality is inferred from this bounded search.

### Primary certification input

R. Becker, M. Sagraloff, V. Sharma and C. Yap,
[*A Near-Optimal Subdivision Algorithm for Complex Root Isolation
based on the Pellet Test and Newton Iteration*, arXiv:1509.06231v4](https://arxiv.org/pdf/1509.06231v4),
8 November 2016, Definition1,(3)–(4),Theorem1, pp12–13:
for F in C[x], r>0, 0<=k<=deg(F), K>=1,

    |F^(k)(m)| r^k/k! > K sum_(i!=k) |F^(i)(m)| r^i/i!

certifies exactly k roots in the disk, counting multiplicities.
No simple-root hypothesis enters this test. Read Section3.3,
Algorithms3–4, Lemma3 and Lemma2's strict-acceptance comparison,
pp15–18: a certified strict lower/upper comparison suffices; test
failure supplies no root count. The complete isolation algorithm's
arbitrary-precision oracle and termination guarantees are not imported.
Theorem1 refers its proof to Marden Section9.2 or reference61;
those proof sources were not retrieved. This standard Pellet input
is imported by precise theorem citation, not reproved. Also inspected
[DLMF1.10(iv), Rouché's theorem](https://dlmf.nist.gov/1.10#iv):
analytic functions on/inside a simple closed contour and strict
boundary domination give equal zero counts. Polynomials meet the
analytic-domain hypothesis; the strict inequality still needs a
certificate. No new theta-specific root inequality is derived here.

For the real-bracket alternative, inspected
[DLMF3.8(iii), Bisection Method](https://dlmf.nist.gov/3.8#iii)
and [1.11(ii)](https://dlmf.nist.gov/1.11#ii).
Import the named intermediate value theorem for a continuous real
polynomial with strictly opposite endpoint signs, and the fundamental
theorem of algebra counting degree-many complex zeros with
multiplicity. Root simplicity/exhaustion must be justified in the
later application, not assumed from a plotted root list. No general
real-zero or isolation theorem is reproved in this review.

### Actual input evidence and unresolved sufficiency

Read L805's full construction and independent step542 audit, and
L807's definitions and error conclusion. Using the shared JSON
inspector, inspected complete selected fields of
`scripts/theta-gauss/audit-certificate-542.json`:
`/evidence/independent_nodes`, `/evidence/independent_weights`,
`/evidence/input_hashes`, `/evidence/positive_denominators`,
`/evidence/inherited_qualifications`, `/evidence/requirements`,
`/status` and `/failures`. This was source-evidence inspection, not
an independent replay of its 106 checks. The root-specific tests in
that audit concern the cubics only. Its report is PASS with no failures.

The hash map identifies the step540 certificate as
`f007b42bb0a51a1a9b13c39c5ee3b6010c605b33c0c87d95a271754a54db9f63`
and the actual-moment source as
`2b429e4029fd7f50b30ea61b43d1be5aa22155b4c680c69440a716ff26643b2e`.
The later implementation must verify current hashes and relevant
audit provenance before using full rational intervals. L805's rounded
display boxes are not a replacement for those selected exact values.
The L778 analytic evaluator and Decimal backend contracts remain
premises; no fresh transcendental verification is claimed.

These existing enclosures make a finite certificate attempt possible.
Whether their widths yield decisive endpoint or disk inequalities is
unresolved and is part of the approved calculation, not a missing
theorem to be resolved by further browsing. No new actual moments,
Q coefficients, floating roots, signs or discriminants were computed
in this literature-only turn. Retain exact moment normalization and
the correlations only as justified by the audited construction;
interval overestimation is allowed, midpoint substitution is not.

### Bounded continuation and decision test

SPECIALIZE approves the unchanged TARGET, subject to the supervisor's
separate approval of this newly ready continuation. Apply the cited
results once to n=2,d=5; the necessary specialization is a conventional
finite certificate, not a new root-counting theorem. Future work must
verify the factorial normalization, exact coefficient definitions,
degree and nonzero leading coefficient before its root conclusion.
Do not substitute actual t_4,t_5 for quadrature moments merely because
lower moments agree. No common interlacing is needed or permitted as
an assumed premise.

Use one approximate root list only to choose rational candidate
brackets/disks. Certify with outward rational coefficient arithmetic:
either five disjoint strictly positive sign-changing brackets with
degree/multiplicity exhaustion, or the cited disk count with the
additional realness/positivity or nonreal-separation justification.
Every complex absolute-value bound must be certified, for example by
rational square comparisons. Record all transformed coefficients,
lower/upper comparisons, root regions, input hashes and failures in
a complete certificate under `scripts/theta-gauss/`; a successful
numerical solver or test of the midpoint polynomial is insufficient.
One bounded refinement of candidate regions or one algebraic
rearrangement using the same source boxes is allowed if needed; no
fresh theta precision campaign, degree sweep or repeated interlacing
calculation. Save an inconclusive certificate and stop if still undecided.

Five simple positive roots justify only subsequent independently
reviewed margin work. A certified nonreal or nonpositive root stops
the reference-hyperbolicity premise for this family; it says nothing
against actual P_5 or RH. A multiplicity obstruction also needs proof;
an interval containing zero is not an equality certificate. Alternating
margins, higher n, a degree-uniform transfer and actual mixed positivity
remain unresolved in every case.

### Search/access record and qualifications

External queries included `"Gaussian quadrature" "Jensen polynomials"`,
`"Laguerre" "convex combination" "dilations"`,
`"theta" "quadrature" "degree five"`,
`"Laguerre polynomials" "positive combinations" real zeros`,
`"Gaussian quadrature" "theta" hyperbolicity`,
`"Jensen" "Gauss" "quadrature" zeros`,
`"Laguerre polynomials" "different arguments" zeros "linear"`,
`"Jensen polynomial" "two-point" roots`,
`"Laguerre" "dilations" "real-rooted"`, and
`"theta" "Gaussian quadrature" "Laguerre" zeros`.
Root-tool searches included BPR/Sturm and Pellet/Taylor/disk-count
terminology. No exact-reference theorem was located. Snippets on
kinetic quadrature, generic multiplier lectures, a 2026 finite-strip
preprint and an external research notebook were not treated as
inspected theorem inputs. No cross-notebook mathematical input is used.

Basu's author page was inspected; its second-edition BPR download
timed out, the old author-hosted chapter link returned404, and the
accessible catalogue PDF contained only front matter. An alternate
mirror was inaccessible. No BPR theorem number or claim is imported.
This is not an essential source blocker because the inspected primary
Pellet theorem supplies the needed finite certificate. The Craven–Csordas
mirror timed out on some later requests; the author-hosted full
Lemma3.5 proof was subsequently read. No additional source access is
needed before this bounded calculation.

Full matching Mathlib coverage remains unchecked. No lemma or
mathematical script was created or modified; PROOF/DAG are unchanged.
The local advance is completed source coverage for a reproducible
finite test, not a new mathematical discovery or a root conclusion.
No mathematical exploration budget was spent or reset. No justified
creative central-gap target is ready: independent alternating margins
and a degree-uniform signed transfer are still unspecified. Preserve
that blocker rather than relabel this finite specialization creative.
