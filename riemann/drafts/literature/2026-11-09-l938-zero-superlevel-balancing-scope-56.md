# Sign-set balancing test — source coverage completed in step57

TARGET: Assess source coverage for a zero-superlevel balancing test on the six two-block restrictions of L938's symmetrized polynomial.
CHECKED: 2026-11-09
DECISION: EXPLORE
SEARCH_EVIDENCE: Step57 searched majorization-closed sets/indicator functions, polynomial zero superlevels, exact coefficient 371319795000, and Sturm isolation with repeated roots; scoped local checks found no earlier test of these six sign sets. No inspected source settles this signed polynomial; unsuccessful searches do not establish novelty.
SOURCE_EVIDENCE: Reused step55's derivative-criterion assessment; inspected Ostrowski (1952) section I nos.5-8/Theorem I pp256-259 and section II no.12 pp262-263; Eisermann arXiv:0808.0097v4 sections3.3,3.5-3.7, Proposition5.8 pp9-12,19; Pebay-Rojas-Thompson arXiv:2208.07904v1 Theorem1.2/Lemma1.4 and relevant proof cases pp1-4. Exact citations and qualifications below.
COMPARISON: Majorization supplies the order relation and Sturm supplies complete finite root counts, including multiplicities through gcds; neither gives invariance of this particular zero superlevel. L940's negative-valued witness does not settle the changed property. Six rays can refute a global claim but cannot prove it.
GAP: The six exact root/sign tables and their inward-closure tests remain uncomputed. Ray-majorization and positive homogeneity must be justified in the application. Integral preservation, actual-theta ordering and variation transfer remain independent gaps.
REASON: Essential source coverage is adequate for the single bounded test below; no new result, root calculation, lemma or mathematical script is produced in this literature-only step. Newly ready coverage receives the supervisor's separate approval before research.
LITERATURE_REASON: Changed hypothesis from global value ordering to preservation of one closed superlevel; the prior ready assessment lacked essential exact root-count and multiple-root coverage.
SCOPE: Covers only six unchanged L940 restrictions, all q>0, the normalized fixed-sum applicability check, complete exact root/multiplicity/sign certification, and the necessary inward-closure discriminator. No new tuple grid, other polynomial, global Schur-concavity retest, full-simplex sufficiency, theta-ordering theorem or density-variation theorem is covered.
COVERED_TARGET: Test zero-superlevel preservation toward q=1 on L940's six two-block restrictions by complete exact positive-root isolation and sign tables, including multiple roots.

The paragraphs immediately below preserve the step56 proposal and its
then-missing coverage. The step57 review after them supersedes their
readiness statements; it does not change the polynomial or assert its signs.

The exact next action is the source review named above. It must compare
standard terminology for sets closed under majorization/binary mixing,
known polynomial sign-set obstructions and an appropriate exact
univariate root-count/isolation theorem. Inspect the relevant primary
hypotheses and repeated-root cases. Check local duplicates/failures
before deciding whether the proposed bounded test is worthwhile.

The proposed subsequent mathematical question, not authorized here,
is whether {Pbar>=0} is preserved when a two-block vector is moved
toward equal coordinates. The six restrictions H_m(q), 1<=m<=6,
are already defined in canonical L940 and fully saved in its certificate.
A possible finite discriminator is to isolate all their positive real
zeros and determine the sign change under movement toward q=1,
with multiple/degenerate roots explicitly handled. The review must
specify a valid necessary test; this note asserts no criterion or
root count. No new tuple sweep, changed normalization, or global
Schur-concavity retest is proposed.

L940's negative-valued witness motivates distinguishing a sign property
from monotonicity of the polynomial's values. It does not prove that
the new property survives any of the six rays or works off them.
A counterexample would stop this sign-set sufficient mechanism; absence
of a counterexample on six rays would be inconclusive in the full
simplex. Root/sign calculations have not begun.

The plausible downstream use is to identify whether balanced energy
configurations can leave the nonnegative region, an intermediate input
to a possible signed-density variation argument. Integral preservation,
actual-theta ordering strong enough for such an argument, and the
variation implication are independent assumptions, not conclusions.
L939 supplies only an eventual tail, and the main L030–L032/C032a
all-degree gap still retains endpoints, contacts, other degrees,
initialization, realization and continuation.

Essential inputs are L938's unchanged rows and normalization, L939(4)'s
labelled polynomial definition and L940's exact symmetrization and
six restrictions. The current EXPLORE assessment may supply the
already inspected general criterion but cannot be silently extended.
L915/L916/L937 and the fixed-cell stop are contrasts. No cross-notebook
input, Decimal premise, new lemma or mathematical script is part of
the next literature-only action. Mathlib coverage remains unchecked.

## Step57: source review and exact scope

### Main gap, target and overlap

The main unresolved claim is actual-Xi all-degree mixed positivity
L030-L032/C032a. The intermediate question is inward closure of the
nonnegative set of the **same** arithmetic S_12 average on six two-block
paths. Its plausible downstream use is a sign comparison under energy
balancing. Passing it would not establish an order for the actual theta
distribution or transfer a pointwise sign property to an integral.

Read L938's hypotheses, density statement and full 34-row table; L939's
hypotheses and equations(4)-(6); and L940's averaging formula,
restrictions(3)-(5), exact witness and verification scope. Also read
the step56 history and its canonical global-Schur stop. The relevant
local search used `zero.superlevel`, `two.block`, `H_m`, `Sturm`, and
`root isolation` in the L938 assessments/proofs and notebook histories,
then root-related assessment filenames. Earlier Pollaczek/Sturm and
ODE-separation references concern different polynomials or different
theorems; their existence does not settle this target. The step55
assessment supplies the already inspected differential criterion and
its nearby polynomial-family comparisons; that work is reused.

L940 closes global Schur-concavity, with an exact negative-valued
witness, and is not silently audited here. L915/L916/L922/L937 and
the fixed-energy-cell stop remain contrasts, not inputs proving the
new sign property. No repeated Schur grid or refinement of the stopped
cell experiment is proposed. No cross-notebook source was read.

### Primary majorization input

Alexandre Ostrowski, *Sur quelques applications des fonctions convexes
et concaves au sens de I. Schur*, J. Math. Pures Appl. (9) **31**
(1952), 253-292, [original article](https://www.numdam.org/item/JMPA_1952_9_31__253_0.pdf),
section I nos.5-8/Theorem I, pp256-259, and section II no.12,
pp262-263, were inspected. Theorem I identifies decreasing partial-sum
majorization, with equal total sum, with a nonnegative matrix having
each row and column sum one. Its necessity and binary-mixing/induction
proof cases are available. No.12 defines order-preserving functions
before imposing the later differential criterion's smoothness.

For this review, define a majorization down-set explicitly: x in A and
y majorized by x imply y in A, within the same fixed-sum domain.
This is the proposed property of A={Pbar>=0}; it is not an imported
theorem about Pbar. Its indicator is an order-preserving observable
in the corresponding direction. The smooth differential criterion
cannot be applied to a discontinuous indicator. In particular,
nonpositive derivatives only at regular boundary points would need
additional treatment at singular zeros and are not approved as a
substitute for the finite root/sign test.

### Primary root-count and multiplicity inputs

Michael Eisermann, *The Fundamental Theorem of Algebra made effective:
an elementary real-algebraic proof via Sturm chains*,
[arXiv:0808.0097v4](https://arxiv.org/pdf/0808.0097v4), header version
26 March 2012 (PDF compilation date 23 October 2018). Inspected
Proposition3.7/Corollary3.8, Theorem3.11/Proposition3.12,
Definitions3.13-3.14, Theorem3.15/Corollary3.16/Remark3.17,
pp9-12; and Proposition5.8 with proof, p19. Over a real closed field,
the normalized Euclidean-chain index counts distinct real roots;
boundary roots count one half. No square-free hypothesis is imposed.
Remark3.17 gives multiplicity recovery by successive gcds with
derivatives. The proof uses local logarithmic derivatives, cancellation
at interior chain nodes and normalization by the last nonzero remainder.
Proposition5.8 puts every root of monic x^d+c_1 x^(d-1)+...+c_d
strictly inside radius 1+max|c_i|.

For a rational-coefficient calculation, the ordered ambient field is
R (or the real algebraic numbers), **not Q as a real closed field**.
Rational Euclidean arithmetic computes the same chain exactly.
Root counts and multiplicity recovery are known inputs, not new
theorems. A square-free quotient and its own derivative may be used;
do not confuse that sequence with dividing the original (f,f') pair
by their gcd. The selected convention must be recorded consistently.

Philippe Pebay, J. Maurice Rojas and David C. Thompson, *Sturm's Theorem
with Endpoints*, [arXiv:2208.07904v1](https://arxiv.org/pdf/2208.07904v1),
16 August 2022 (PDF dated 18 August), Theorem1.2, Lemma1.4,
Examples1.1/1.3 and proof pp1-4 were inspected. For nonzero f in R[x]
and a<=b, their zero-deleting variation difference counts distinct
roots in (a,b] when neither endpoint is a multiple root. Interior
multiple roots are allowed. At a multiple-root endpoint all sequence
values vanish and that formula cannot simply be used. The proof's
subdivision, simple-root, common-factor and no-root cases were read.
Use this as an independent endpoint qualification; the finite test can
avoid endpoint ambiguity with nonroot rational isolators and explicit
treatment of rational roots. No new endpoint theorem is needed.

### Search record and uninspected leads

Queries included `majorization Schur convex sets indicator functions
convex hull permutations theorem`, `Schur-convex set majorization`,
`majorization superlevel sets polynomial`, `polynomial Schur sets`,
`polynomial superlevel majorization`, `371319795000 polynomial
majorization`, and Sturm/multiple-root/exact-isolation queries.
The exact-coefficient and sign-set searches supplied no inspected
matching theorem for the signed 34-row polynomial. Klemes's structured
positive index-set families remain outside the established scope.
This bounded search does not certify novelty or impossibility.

The search surfaced *Majorization and Gaussian correlation*,
[publisher lead](https://www.sciencedirect.com/science/article/abs/pii/S0167715299000644),
whose snippet uses the term Schur set for an indicator-monotone set.
The page returned 403; no theorem or Gaussian correlation conclusion
is imported from it. Explicit down-set terminology and Ostrowski's
inspected order theorem suffice for the finite necessary test; this
optional inaccessible lead is not an essential source blocker.
FLINT documentation and formal Sturm references appeared as leads;
no implementation correctness or Mathlib theorem is inferred from
them. No full matching Mathlib coverage was checked.

## Bounded mathematical continuation, not performed in this review

The exact covered action is:

> Test zero-superlevel preservation toward q=1 on L940's six two-block restrictions by complete exact positive-root isolation and sign tables, including multiple roots.

Use H_m as defined in L940(3), m=1,...,6, and
t_m(q)=(q repeated m times,1 repeated 12-m times)/(mq+12-m).
Keep every coefficient, factorial, labelled slot and M_0^12 factor.
For each side of q=1 the discriminator is whether there exist q_0,q_1>0
with q_1 between q_0 and 1, H_m(q_0)>=0 and H_m(q_1)<0.
This specifies the proposed necessary test, not a result about any H_m.

The research application must first justify from Ostrowski's theorem
that the normalized movement being tested is toward a majorized
vector, and from L940's homogeneity that its sign is the sign of H_m.
It must also justify why the six m values represent both block sizes
when q ranges over all positive numbers. These are elementary
applicability obligations, left to the mathematical turn; no new
specialization is proved and approved here.

One bounded computation should reconstruct the six rational
polynomials from the original rows and compare the saved L940
coefficients, then certify **all** positive real roots and signs.
Use exact signed remainders, a proved outer root bound, rational
nonroot isolators, total-count agreement, and successive gcd checks
for multiplicity. Retain complete coefficients, division identities,
variation counts, bounds, sample values and failure lists on disk.
Compare each row polynomial at q=1 with the recorded balanced value
from L939; this is an input check, not a new asymptotic calculation.

Determine signs on every complementary interval, including the first
positive interval and the unbounded last interval; split at q=1 and
handle any rational root there explicitly. Roots themselves belong
to the closed nonnegative set. Even-multiplicity roots cannot be
discarded merely because they do not reverse the sign: test whether
moving inward from a zero enters a negative interval. A failed test
may require an algebraic root as q_0; do not demand an unavailable
rational starting point for an isolated zero. A root defined by a
rational polynomial and a complete isolating interval is admissible
exact evidence. Distinguish domain endpoints q=0/infinity from
included positive finite roots. Treat zero/constant-polynomial cases
explicitly if encountered; never feed zero to a nonzero-polynomial
theorem. No roots, counts or sign tables have been computed here.

An exact inward exit from {H_m>=0} abandons the proposed global
sign-set sufficient mechanism. A complete six-path pass establishes
only those restricted properties; it cannot be promoted to a full
simplex theorem. Stop after this six-polynomial test, without adding
a grid or other rays under this assessment. A pass requires a new
independently assessable mechanism before any further global claim.

The density context uses L019/L058/L874/L917 through L938; the finite
test uses L938's rows, L939(4)-(6) and L940's definitions and saved
coefficients, with reconstruction rather than blind reliance on an
unaudited certificate. Integral preservation under symmetrization,
actual-theta ordering, finite-energy variation, endpoint signs,
contacts, other degrees, initialization, realization and global
continuation remain unpaid. This literature turn adds no lemma,
script, numerical premise, DAG edge, proof-assembly change or RH claim.
