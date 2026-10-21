# Rational dyadic two-descent image — completed source comparison

TARGET: Determine whether the rational two-adic Kummer condition cuts the local norm-square unit space for L069's E0, using its entire cubic algebra.
CHECKED: 2026-10-14
DECISION: IMPORT
SEARCH_EVIDENCE: Reused the coarse-rank and bare-unit assessments; checked L069, L046, ATTEMPTS/032 and the recovery comparison; searched dyadic two-descent, good-reduction unit images, full local-image algorithms and the exact local-index theorem; inspected BPT and Bruin–Stoll primary passages.
SOURCE_EVIDENCE: Barrera Salazar–Pacetti–Tornaría arXiv:2001.02263v3 (17 September 2020), Section 1 p.3, Lemmas 1.3 and 1.5/Remark 1.4 p.4, Definition 1.6/Theorem 1.8 pp.5–6 including the good-reduction proof case, and Theorem 1.11 p.7 including its first-claim proof; Bruin–Stoll 14 March 2008 manuscript Section 2/Remark 2.1 p.3 and Section 4 Lemma 4.4 and LocalImage correctness discussion pp.7–10.
COMPARISON: Theorem 1.11 already gives full Kummer-image inclusion in the norm-square maximal-unit space and its index under Definition 1.6; the unramified dyadic good-reduction clause is the relevant application to check. This comparison needs a cited theorem application, not a new class enumeration or precision computation.
GAP: Local model, good-reduction and notation matching remain for the next mathematical application; global-unit localization, global class coverage, rank below twelve and point/integer lifting remain open. The theorem does not identify an explicit class list or show that a global unit is removed.
REASON: Replace missing dyadic computational coverage by a stronger known local-index theorem; preserve the exact saved target and avoid reproof of covered mathematics.
SCOPE: The saved rational-place comparison only, with the entire cubic etale algebra and maximal integer ring; IMPORT permits only KNOWN_IMPORTED work. No global rank bound, explicit class list, other place or global-unit localization is preapproved.
LITERATURE_REASON: REVIEW_REQUIRED at invocation; essential dyadic theorem coverage was unread, while existing global assessments remained reusable.

## Target, relevance and duplicate checks

The main gap remains primitive integer emptiness, including ordered
(3,4,11). The intermediate target is M intersect H versus M. A strict
cut could provide a necessary local linear condition in a later certified
global descent space; equality would park this place's unit-pruning test.
Neither outcome alone removes a class from L069's global unit kernel.

The supplied definitions remain unchanged: E0 is
y²+y=x³−x²−10x−20, g=X³−4X²−160X−1264 and A=Q2[X]/(g),
retaining every factor. O_A is the product of their maximal integer
rings. M is the image of norm-square classes from O_A*/O_A*² in A*/A*²;
H is the full Kummer image of E0(Q2)/2E0(Q2). H is not assumed to
lie in M. Irreducibility over the global K does not assert local
irreducibility over Q2.

Read L069's proof/audit, L033's field/model passages, L046's rational
factor/good-reduction passages, ATTEMPTS/032 and the recovery comparison
in drafts/2026-10-14-bare-unit-rank-critical-audit.md. Reused the coarse
and bare-unit assessments. Targeted searches also checked ATTEMPTS/014
(five-isogeny local equality) and ATTEMPTS/030 (fixed fifth-power class
at finite primes). Neither decides this two-descent comparison. The
unfiltered stop is preserved. No cross-notebook input is used.

## Covering primary theorem

Daniel Barrera Salazar, Ariel Pacetti and Gonzalo Tornaría (BPT),
*On 2-Selmer groups and quadratic twists of elliptic curves*,
[arXiv:2001.02263v3](https://arxiv.org/pdf/2001.02263v3),
17 September 2020; the version was checked on the
[arXiv record](https://arxiv.org/abs/2001.02263).
Published in Math. Res. Lett. **28** (2021), 1633–1659,
[DOI](https://doi.org/10.4310/MRL.2021.v28.n6.a1).
All page/theorem numbers here refer to the inspected arXiv version.

Section 1 takes a base of characteristic different from two and a monic square-free
cubic defining y²=F(x). Its Kummer target is the square-norm subgroup
of the ENTIRE A*/A*², without quotienting by scalar classes. Remark 1.4
uses the product of maximal integer rings, not the polynomial order.
The source's local base symbol K must not be confused with our global K.

Definition 1.6 requires an integral monic square-free cubic and at least
one of four alternative conditions: a cubic field algebra; maximal
polynomial order; odd component index at odd residue characteristic;
or an unramified dyadic base with good reduction of the curve. The
last clause does not require good reduction of the displayed
completed-square cubic model or maximality of its polynomial order.

Theorem 1.11, FIRST assertion: over a finite extension F_v/Q2
satisfying Definition 1.6, the Kummer image is contained in the
norm-square subgroup of O_A*/O_A*² with index 2^[F_v:Q2].
Its first-claim proof uses Theorem 1.8 (inclusion), Lemma 1.3
(image order [O_v:2O_v]·|E(F_v)[2]|), and Lemma 1.5
(unit norm-kernel order [O_v:2O_v]²·|E(F_v)[2]|).
The latter proof counts every local factor and uses the scalar norm
splitting from Remark 1.4. These are source statements, not new
cardinality calculations for our E0.

Read Theorem 1.8's complete good-reduction case, pp.5–6: supersingular
reduction over an unramified dyadic base gives the cubic-field case
via Brumer–Kramer Proposition 3.4; the ordinary case cites their
Proposition 3.6 with the same unramified-base restriction. Also read
the full first-claim proof of Theorem 1.11. Its separate U4 assertion
is unnecessary here and is not imported. Global Hypotheses 2.1,
including odd narrow class number, are outside this local theorem.

The next application must match L069's origin-preserving model change
and nonzero cubic discriminant and L033/L046's good reduction on the
original integral model to these hypotheses. It must use the full
abstract Kummer map, defined at every group point, rather than evaluate
X−theta at a zero or pole. The theorem includes exceptional points.
It supplies both inclusion and index; cardinality without inclusion
would not suffice. No custom proof, maximal-order basis, local
factorization, torsion enumeration or p-adic sampling is needed for
this application. This review does not yet establish a specialized
local result for E0.

## Full-image and precision comparison

Nils Bruin and Michael Stoll, *Two-cover descent on hyperelliptic
curves*, [author manuscript dated 14 March 2008](https://mathe2.uni-bayreuth.de/stoll/papers/twocoverdescent.pdf),
Math. Comp. **78** (2009), 2347–2370. Section 2/Remark 2.1 treats odd
degree without dividing by scalar classes, the infinity point and
exceptional Weierstrass evaluations. Section 4 includes residue
characteristic two. Lemma 4.4 and its proof give a sufficient disk
precision condition; SquareClasses/LocalImage and their correctness
discussion retain root neighborhoods and the reciprocal nonintegral-x
chart. The termination/realization discussion on pp.8–10 was read.
This is a primary algorithmic lead for explicit images, not an image
computed here. It is unnecessary for the narrower comparison now
covered by BPT, and no implementation is authorized by this IMPORT.

Simon's recorded global cubic Kummer coverage is reused. Schaefer–Stoll's
odd-prime prescription and L046's five-isogeny result cannot replace
this dyadic two-descent theorem. Mathlib full matching and supporting
coverage: not checked. No novelty follows from the search.

## Search record, limits and continuation

Queries included `elliptic curve good reduction 2 local Kummer image
units cubic algebra Brumer Kramer`, `2-descent good reduction units
dyadic`, `Schaefer Stoll local image 2 descent pdf`, `Theorem 1.11
2-Selmer index`, and correction/erratum searches for the BPT paper.
No correction was located in this bounded search; that does not prove
none exists. The later hyperelliptic paper arXiv:2308.08663 is an
unread lead, not an input.

The BPT publisher PDF returned 403. Its accessible primary arXiv
statement/proof cases suffice for this theorem import. The author-hosted
2selmer.pdf was opened, but theorem numbering was not independently
resolved, so no version-equivalence claim is made. The Brumer–Kramer
DOI was inaccessible and the Euclid PDF endpoint returned a wrapper.
Those original referenced proofs were not read or independently audited;
the cited input is the fully stated primary BPT theorem. These retrieval
limits do not block its use by precise citation.

Continue with the exact saved target as KNOWN_IMPORTED. Accept a local
cut only after matching the integral model, unramified good reduction
and full-algebra definitions of M/H. Failed hypotheses require a
specific coverage correction; do not infer inclusion from sizes.
Equality parks this place. Properness alone leaves global-unit
localization, global class coverage, other places, actual rank,
index/coset bounds, other classes and integer lifting unresolved.
No GRH or global-to-local surjectivity is assumed. No new lemma,
mathematical script or source-dependent specialization was produced
this literature-only turn. PROOF and DAG remain unchanged.
