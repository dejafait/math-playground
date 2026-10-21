# Primitive seven-adic two-descent image — source comparison completed

TARGET: Determine the exact primitive whole-fiber two-descent image at seven for L033's 54a1 algebra.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed exact-image, standard local-Kummer and stronger good-prime searches; compared L033/L034/L069/L084/L088, the ready thirteen-adic construction/audit assessments and ATTEMPTS/039–040. No inspected theorem determines the correlated seven-adic image; exact queries and qualifications are recorded below.
SOURCE_EVIDENCE: Inspected BPT arXiv:2001.02263v3 Section 1 pp.3–6, especially Definition 1.6, Theorem 1.8 field/split/quadratic cases and Corollary 1.9 proof; Bruin–Stoll 14 March 2008 Section 4 Lemmas 4.3–4.4 and local algorithm proof cases; FNS 10 June 2019 Section 7.2 pp.25–29, including the complete general Lemma 7.5 statement/proof and the specifically dyadic Lemma 7.6; Stacks 04GK statement and complete proof. Reused the precise lifting and norm coverage cited below.
COMPARISON: Good-prime equality describes unrestricted norm-square unit classes, not points transported from one common primitive scalar through the entire fiber. L088 gives a global D/F norm constraint to retain, but its thirteen-adic application is field-specific. No inspected result asserts automatic seven-adic restricted membership or redundancy on T.
GAP: Source coverage permits the specialization, while the entire seven-adic algebra, common primitive domain, all identifications, exact classes, branch/tail coverage and realizations remain uncomputed. Subgroup structure and independence on T remain unresolved.
REASON: Admit one subsequent REPRODUCTION attempt on the unchanged target using the inspected local methods; this literature turn proves no new seven-adic result and creates no lemma or mathematical script. Equality or proved norm redundancy retires the additional-filter mechanism; unresolved coverage must be saved rather than called an exact image.
SCOPE: Exactly TARGET with L033/L034's entire modular fiber, L069's fixed theta and all seven-adic components; no global class backend, rank bound, probe enlargement or integer exclusion.
LITERATURE_REASON: The supplied gate requires comparison at the new prime seven; existing ready general methods are reused, while the unrestricted-versus-correlated image and possible good-prime redundancy needed explicit assessment.

## Purpose and bounded admission test

The main gap remains positive primitive integer emptiness in the 54a1
branch and the other residual signatures. An exact local primitive
two-descent image at seven could supply a necessary constraint to compare
with L084's T. Its relevance depends on whether ordinary supported-class
conditions and L088's square D/F norm already force membership. A proper
subset of an unrestricted image alone would not prove independence on T,
improve a dimension bound, or exclude an integer solution.

This was an uncovered proposal at the L089 audit. The separate source
comparison below now covers its general methods, without doing the
calculation. Known unrestricted-image equality must be used as the
baseline, rather than counted as an additional global condition. No new
mathematical conclusion about seven is derived in this source review.

The inspected finite local-image, factor-lifting and branch-parametrization
methods allow one attempt to establish a complete finite test. Its
termination and precision must be justified in this specialization;
source coverage alone supplies no computed bound. An assessed theorem
proving automatic redundancy would retire this candidate; an unresolved
branch or ineffective reduction parks the incomplete calculation rather
than reopening the eleven-adic envelope or class-backend scans.
Any future exact-image attempt must retain all component identifications,
exceptional points, shared primitive power witnesses, and scalar branch
disks. Success requires equality with the complete image, not sampled
residue classes. Whether that image is a subgroup is also unresolved.

Essential proposed inputs are L033/L034 (entire field and modular map),
L069 (fixed cubic and two-descent generator), L074/L084 (supported domain
and T), and audited L088 (universal cubic norm). L065 is only a contrast:
its finite-prime membership concerns the five-isogeny map. L073/L082/L087
provide assessed-method leads, not seven-adic facts. No cross-notebook
input is proposed. No complete D S-unit basis, localized class kernel,
global realization of a local tuple, or rational/integer lifting is
assumed. Full and supporting Mathlib coverage for this target is not
checked. ATTEMPTS/033–040 retain their original evidence and stops.

## Exact scope and primary-source comparison — 2026-10-18

For A7=K tensor_Q Q7, the target concerns the tuple of two-descent
classes induced by EVERY Q7-algebra isomorphism B_s -> A7, with B_s
the actual projective fiber of L034's map. Fix L069's generator theta
and evaluate [4x-theta], with standard root-point and origin values.
Require nonzero a,b,c in Z7, min(v7(a),v7(b),v7(c))=0,
a^3+b^4=c^11 and s=1728a^3/c^11. The same triple and scalar must
work on all components. No seven-adic splitting, image cardinality,
subgroup property or power surjectivity is assumed here.

**Barrera Salazar–Pacetti–Tornaria**, *On 2-Selmer groups and quadratic
twists of elliptic curves*, [arXiv:2001.02263v3, 17 September 2020](https://arxiv.org/pdf/2001.02263v3),
Section 1 pp.3–6. For a finite extension L/Q_p and an integral monic
square-free cubic, Definition 1.6 permits a cubic field, maximal
polynomial order, odd residue characteristic with odd nonsingular
reduction index, or unramified dyadic base with good reduction.
Theorem 1.8 gives norm-square unit containment; Corollary 1.9 gives
equality when p is odd. Lemmas 1.3 and 1.5 supply its cardinality
argument. Read the field, split and quadratic-factor proof cases;
they concern the maximal integer rings of the entire cubic algebra.
L069 supplies disc(g)=-256*11^5 and L033 supplies the integral
good-reduction model away from eleven. These are the existing inputs
for checking the odd-prime hypotheses at each actual seven-adic place.
The theorem's ordinary condition is the unit/norm condition already
built into W_S outside two and eleven, subject to this applicability
check. It imposes no shared scalar or whole-fiber realization requirement.
No global narrow-class hypothesis from Section 2 is needed for this
local theorem. Do not reprove the theorem or count its baseline as
new pruning.

**Bruin–Stoll**, *Two-cover descent on hyperelliptic curves*, Math.
Comp. **78** (2009), 2347–2370,
[14 March 2008 author manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/twocoverdescent.pdf),
Remark 2.1, Section 4 pp.6–10 and Section 9 p.15. Reuse the previously
inspected odd-degree convention: full algebra modulo squares, root
evaluation (a-theta)+h(theta) when f=(X-a)h, and identity at monic
infinity. Reinspected Lemmas 4.3–4.4 and the recursion, linear-root,
existence, reciprocal and infinity cases. Lemma 4.3 requires odd
residue characteristic, integral coefficients, unit leading coefficient
and discriminant valuation at most one. Equality also requires unit
discriminant and sqrt(q)+1/sqrt(q)>=2(2^(2g)(g-1)+1). This is still
an unrestricted image statement. Lemma 4.4 assumes irreducible h,
integral x0, e>=0 and
v(h(x0+epsilon*pi^e)-h(x0))>v(h(x0)); constancy follows on
x0+pi^(e+v(4))O. The source algorithm terminates for unrestricted
points. It does not prove termination for an arbitrary additional
whole-fiber/common-witness predicate. The proposed specialization
must certify that predicate separately on every retained disk.

**Freitas–Naskrecki–Stoll**, *The generalized Fermat equation with
exponents 2, 3, n*, Compositio Math. **156** (2020), 77–113,
[10 June 2019 final author manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
Section 7.2, printed pp.25–29. Read the entire twelve-subgroup
transport, the explicit modular map, Table 5, (7.4), and Lemma 7.5
with its full proof. That general complete-field lemma supplies
ramified branch power series only under its explicit coefficient,
nonzero linear-term and convergence inequalities. These must be
verified locally; it is not an automatic effective disk bound.
Lemma 7.6 and its covering proof concern Q2, specified dyadic domains
and absence of local two-torsion, so they cannot be imported at seven.
The source places its global Selmer computations under GRH; neither
those dimensions nor the complete conditional classification is used.

**Stacks Project**, [Lemma 10.153.7, tag 04GK](https://stacks.math.columbia.edu/tag/04GK),
statement and complete proof read 2026-10-18: reduction is an
equivalence for finite etale algebras over a henselian local ring,
including morphisms. It controls all identifications after an entire
finite-etale integral fiber has been established. It cannot be applied
to a repeated branch reduction or merely to a convenient necessary
polynomial. L066's thirteen-adic map certificate is not a seven-adic
certificate; local integral charts and separability require verification.

Reuse the ready [thirteen-adic membership assessment](2026-10-13-thirteen-adic-canonical-class-membership.md),
primary-input ranges: Clark ANT II, 161-page author notes, Theorem
1.79 p.58 (strict Hensel), Theorems 2.38/2.41 pp.80–82; Milne ANT
v3.08, 19 July 2020, Theorem 7.33/Remark 7.36 pp.121–123,
Corollary 7.42/Remark 7.43 p.124, Propositions 7.50/7.60
pp.127–128,131–132; Zabradi's 29 June 2022 notes, Lemma 2.3,
Theorem 2.4 and Corollary 2.5 p.4. These give factor lifting,
local-field identification and root tests. Repeated factors need
refinement, not an assumed maximal-prime decomposition. At seven,
unit root lifting still requires an actual residue root. Keep one
shared c; do not assume cube or fourth-power surjectivity.

For a later norm comparison reuse the ready
[global-norm assessment](2026-10-17-thirteen-global-norm-filter.md):
Stein, May 2004, Corollary 5.2.3 p.28; Milne ANT v3.08,
Proposition 4.1 pp.68–69 and Proposition 8.2/Corollary 8.4 p.136;
Milne CFT v4.03, III Proposition 1.2/Lemmas 1.3–1.5 p.98;
Conrad, *Finite fields*, Theorem 4.6 pp.9–10. Audited L088 already
provides the square D/F norm on T, including supported nonunit lifts.
Its localization is a product over all extending places. No individual
component can be declared square without the actual factor and norm
maps. The thirteen-adic proof uses its particular unramified field;
its conclusion does not assert redundancy at every prime.

## Search record, overlap and bounded mathematical continuation

Actual queries were `"X0(11)" "local" "2-descent"`,
`"54a1" "7" Freitas Naskrecki Stoll`,
`"two-cover descent" "good reduction" "local" image`,
`"On 2-Selmer groups and quadratic twists" Corollary 1.9`,
`"primitive" "whole-fiber" "seven" descent`, `"54a1" "7-adic"`,
`"X0(11)" "good reduction" "7" descent`,
`"two-descent" "rational" "j-invariant" local image`,
`"elliptic curve" "local image" "rational j" descent`,
`"X0(11)" "Selmer" "7"`, and
`"2-descent" "good reduction" "unramified" local image`.
The primary matches supporting this review are the sources above.
Results on plane quartics, level raising, other torsion modular curves
and the 2025 exponent-25 computation do not supply an inspected match
for this fixed target. Their search snippets are not theorem evidence;
they are unread leads outside the essential coverage, not source
blockers. Failed exact-phrase searches establish no novelty.

Local comparison used L033/L034's model/fiber ranges, L069's cubic,
L084's definition of T, L088's hypotheses/conclusion, the ready
[thirteen-image construction](2026-10-17-primitive-thirteen-two-descent-image.md)
and [audit](2026-10-17-primitive-thirteen-image-audit.md) assessments,
and ATTEMPTS/039–040. L088 stops thirteen-adic independence by a
proved norm argument. L089 stops a sufficient eleven-adic envelope
certificate, without deciding actual global containment. Neither is
an image theorem at seven. L065's finite-prime five-isogeny survivor
uses a different map and remains untouched. No cross-notebook input
is read or proposed; no existing stop is reversed.

The next attempt is still exactly TARGET. First establish A7 in its
entirety and the corresponding cubic factors, preserving theta.
Use the known unrestricted good-prime image as comparison. Determine
the common primitive scalar domain by valuation and residue root
tests. Reduce the whole-fiber predicate to finitely many regular
disks and explicitly controlled neighborhoods of 0,1728,infinity;
prove any tail exclusion or periodicity uniformly in the unit parts.
Retain removable x=16 charts, two-torsion and all identifications.
Verify the required integral map/fiber hypotheses rather than
transferring L066 from thirteen. Each claimed class needs an exact
entire-fiber realization with one shared primitive triple. Every
rejected disk needs a complete obstruction. Full records belong on
disk; previews or sample residue tables cannot certify equality.

Continue to a separately assessed comparison on T only if a complete
proper image is obtained and no already established norm argument
settles redundancy. Equality with the unrestricted image, or proved
automatic membership from the existing constraints, retires this
additional filter. If even one branch, tail or realization remains
uncontrolled, report partial evidence and the precise obstruction;
do not expand into global basis searches or repeat the eleven-adic
envelope. A proper local set may fail to be a subgroup and may still
be redundant on T. Both dimension bounds, the localized class kernel,
global realizations and integer lifting remain separate gaps.

This review performs no seven-adic factorization, residue enumeration,
new lemma derivation or mathematical script change. It authorizes a
later specialization of known methods, not a verified image or a
new result beyond the sources checked. Full and supporting Mathlib
coverage for the exact target is not checked.
