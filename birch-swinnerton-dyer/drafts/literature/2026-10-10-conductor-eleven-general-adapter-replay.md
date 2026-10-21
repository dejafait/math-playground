# Conductor-eleven general-adapter replay — source coverage approved

TARGET: Independently certify the arithmetic of model [0,-1,1,-10,-20] and produce and completely replay its L038-relative-v1 dual-kernel certificate at conductor 11 with P={2}.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched notebook-local literature/history/ATTEMPTS for the exact model and 11a/11.a labels; inspected L029/L030/L038 contracts and adapter interfaces; searched exact-model, modularity and Tate-exit terminology, then retrieved the primary sources below.
SOURCE_EVIDENCE: Inspected LMFDB 11.a2 (Cremona 11a1) exact minimal equation, invariants, local reduction and q-expansion; Cremona corrected second edition (1997), Sections 3.1--3.2 pp.62--67 and Section 3.9 p.103; BCDT Theorem A and Introduction conditions (1)--(2); Stein online v0.1 Theorem 3.13 and its proof qualifications. Reuse audited L029/L030/L038 mathematical and executable coverage.
COMPARISON: This is a published conductor-11 non-CM curve with published a_2=-2, and the structural/kernel methods are known and locally audited. The missing object is an independent arithmetic certificate and complete new-instance replay through the general adapter, not a new elliptic theorem or BSD case.
GAP: No new-model invariant/point-count certificate or general-adapter elliptic replay exists locally; later work must establish arithmetic applicability and check the entire finite evidence rather than trust database labels, provenance strings or success summaries.
REASON: Essential theorem and method coverage is adequate for one bounded SPECIALIZE/REPRODUCTION attempt. Citations do not emit or verify the new instance's lattice, paths, bindings or rank witness; no mathematics or mathematical program was executed in this review.
LITERATURE_REASON: Changed exact elliptic input and first arithmetic use of the L038-relative-v1 adapter were outside the prior fixed replay audit.
SCOPE: Only model [0,-1,1,-10,-20], proposed N=11 and P={2}; independent arithmetic certification plus complete finite production/replay, with bounded repairs if needed. No unbounded prime search, normalized scale, q, coefficient, point certificate or universal software theorem.

The completed startup action was: Assess coverage for independent arithmetic certification and a complete L038-relative-v1 dual-kernel replay of model [0,-1,1,-10,-20] at proposed conductor 11 with P={2}.
The TARGET above is the separately assessed continuation. No part of its
arithmetic derivation or executable replay was performed in this literature turn.

## Relevance, threshold and unresolved inputs

The main gap is rank E(Q)=m(E) for arbitrary m(E)>=2. The intermediate
object is a completely certified full-relative dual integration line for
one new input to the general adapter. Its downstream use is the line
premise of L028/L036, conditional on their independent q and remaining
hypotheses. The chosen curve is a small published example, not a proposed
higher-rank BSD advance. Essential inputs are L029's column/transpose and
geometric J conventions, L030's arithmetic-source precedents and audited
parameterized checker, and L038's complete lattice/operator contract.

Continue only after independent arithmetic establishes the exact conductor,
minimality, non-CM and trace and full replay proves rank(B)=d-1 with a
nonzero rational nullvector. A larger kernel is INCONCLUSIVE; zero nullity
or failed arithmetic/binding/geometry/descent requires diagnosis or redirection.
Do not expand P in this attempt. No d or rank is presumed from a database.
Independent q, subsequent coefficient/point certificates, rational membership,
divisible Sha and arbitrary complex-order comparison remain unresolved.

## Inspected arithmetic sources and applicability obligations

1. [LMFDB 11.a2, Cremona 11a1](https://www.lmfdb.org/EllipticCurve/Q/11/a/2),
   accessed 2026-10-10, page footer Release 1.2.1/SageMath 10.5.
   Read the exact minimal equation, invariants, local data and modular
   q-expansion, not its numerical BSD formula. This published model matches
   the proposed coefficients exactly. It records conductor 11, minimal
   discriminant -161051=-11^5, nonintegral j=-122023936/161051,
   no CM, local type I_5 at 11 with conductor exponent one, and a_2=-2.
   These are source values, not locally reproduced calculations. Rounded
   periods, analytic Sha, numerical special values and rank columns are
   not certification inputs. The page's modular form label is 11.2.a.a;
   no label identification is needed for the independent modularity route.

2. [Cremona, corrected second edition, Chapter 3](https://johncremona.github.io/book/fulltext/chapter3.pdf),
   printed pp.62--67 and 103. Read invariant formulas and equation (3.1.3),
   the discriminant transformation, minimal-model discussion, conductor
   cases on p.65 and Tate pseudocode lines 1--22, including the good and
   multiplicative exits. Read the complete rational CM list on p.103.
   These cover integral nonsingular models and rational CM classification.
   Later certification must compute invariants, factor Delta, check local
   valuations against possible discriminant decreases by multiples of 12,
   and check c4 at every bad prime before importing the conductor exits.
   It must establish that j excludes the integral CM list. No additive
   Tate branch is proposed; failure of these tests changes coverage.

3. [Breuil--Conrad--Diamond--Taylor, JAMS 14 (2001), 843--939,
   Theorem A and Introduction](https://virtualmath1.stanford.edu/~conrad/papers/tswfinal.pdf).
   Inspected the authors' January-2001 manuscript, Theorem A and the
   equivalent L-function statements (1)--(2), PDF pp.1--3. Every E/Q is
   modular with the weight-two conductor-level association used in L030.
   There is no analytic-rank or ordinary-prime restriction. Reuse the
   normalized rational newform interpretation already assessed in L030;
   do not reprove modularity. Once exact conductor is certified, good-prime
   coefficients come from point counts. At 2 the later attempt must check
   good reduction and enumerate all affine pairs and the infinity point;
   the published coefficient is only an independent comparison value.

No new arithmetic specialization is derived here. The next research turn
must put its complete hypotheses, proof, qualifications and Mathlib status
in a canonical lemma file before the arithmetic becomes a local input.
Mathlib full matching/supporting coverage was not checked in this review;
unknown availability is not absence.

## Reused structural coverage, duplicates and failures

Reused ready assessments for parameterized dual-kernel source review and
critical audit, and general-relative implementation and critical audit,
all dated 2026-10-10. Inspected L029 hypotheses, L030 arithmetic and general
adapter/audit passages, and L038 hypotheses, construction/imports, descent
and audited empty-shape cases. Narrow program reads confirm the general
builder accepts supplied level/P and the adapter invokes the complete
structural checker before linear replay. Arithmetic syntax/Hasse tests
and provenance strings do not prove elliptic applicability; preserve
SUPPLIED_CONDITIONAL in the generic executable even after a separate
canonical arithmetic proof supplies its assumptions.

Reopened [Stein online v0.1, weight-two Theorem 3.13](https://wstein.org/books/modform/modform/weight_two.html),
including all two/three-term relations and removal of all torsion. Its
printed version is Stein (2007), pp.42--44; L038 retains Section 3.4.1
for Hecke paths and online reflection equations (11)--(12)/Remark 1.43.
The online proof proves surjectivity and well-definedness but explicitly
omits injectivity, citing Manin (1972), Section 1.7. Import the stated
full theorem as previously assessed; do not claim its partial proof is
complete or the unread original was inspected. Example 3.12 at N=11 is
only a path example and does not certify this entire instance.

The local exact-model/label search found only the pending continuation
and history/117, with no completed duplicate. Existing fixed L030 replay
and structural N=1/N=15 runs are different executed objects. ATTEMPTS/023
and 024 stop repeated conditional calibration audits as input production;
this new finite production test does not reopen uniform q or its parked
source blocker. L030's repaired stale subordinate-report failure remains
relevant: retain fresh input-bound complete subordinate and outer reports.

## Approved finite evidence contract

Retain outputs in a fresh instance directory, preserving all prior work.
Check every coset/lift, source relation, unimodular transform and inverse,
saturated relation, quotient coordinate and every integral generator.
Replay every oriented endpoint chain and Gamma_0 segment for J and the
complete good-prime T_2 sum, full saturated descent and all generator
matrix reconstruction identities. Bind model/N/P/traces, structural bytes,
adapter version and subordinate reports; supplied paths/hashes alone are
not mathematical verification. Reconstruct B from column matrices using
L029's transposes; verify complete reversible rational elimination, a
nonzero nullvector, an independent nonzero (d-1)-minor and all generator
functional values. Record actual and required bounds, failures and full
certificate/report paths without relying on previews. A single successful
finite replay supplies no universal software soundness or runtime bound.

Queries included exact-model LMFDB terms, BCDT Theorem A and Tate
multiplicative c4/conductor terminology. Search snippets, secondary
encyclopedia pages and unrelated number-field hits were not used as
proof. No new primary source access blocker appeared. No novelty follows
from the scoped search, and no beyond-source mathematics is claimed.
