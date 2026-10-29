# Actual-family average pole cost — completed source comparison

TARGET: Assess whether averaging prime divisibility on L089's fixed coefficient lattice can yield survivors whose interval-relevant pole cost satisfies L116's residual budget.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step476 searched multivariate polynomial divisibility, finite-field zero bounds, geometric sieves and elliptic-curve local/global densities; inspected the primary inputs below and reused the occurrence/prime-selection assessments. Targeted checks of L089,L101,L116, ATTEMPTS/035–036 and the October-25 assessments found no existing joint weighted estimate. No novelty is inferred.
SOURCE_EVIDENCE: Moshkovitz, ECCC TR10-096 revision 1 (8 July 2010), sections 1–3, pp.1–2, complete statement/proof and Lemma 3.1; Cremona–Sadek, arXiv:2003.08454v3 (18 October 2021), Proposition 3.1 and entire proof p.11, Proposition 3.4 and proof p.14, Proposition 3.5 and proof p.15; Zywina, MaximalGalois author version, Lemma 5.9 and entire proof p.8, with fixed-level coverage reused from step338. Direct links and scope distinctions below.
COMPARISON: Known finite-field zero bounds, explicit prelimit residue-block counts and a coefficient-box height upper bound support a bounded first-moment specialization. Fixed-modulus density limits alone do not justify moving primes. Neither inspected source gives the same-member weighted estimate, reduced-height lower slice or overlap with L089 survivors; these remain proof obligations.
GAP: Coverage is ready for the narrowly specified later attempt, not for its conclusion: verify moving-modulus errors on the actual lattice, handle fixed exceptional primes, remove low reduced-height members and fixed parameter exceptions with sufficiently small loss, then compare the weighted bad set with L089's retained count and L116's actual budget.
REASON: Essential primary inputs have been inspected and the fixed-modulus versus moving-modulus distinction made explicit. Only this known-method specialization is supported; no averaged estimate or survivor has been proved. The newly written mathematical continuation receives a separate supervisor approval next turn.
LITERATURE_REASON: At turn start, arithmetic averaging and joint actual-family selection introduced essential uncovered hypotheses beyond the ready scalar-height and finite-prime-set mechanisms; this turn inspected their source inputs and isolated the remaining specializations.
SCOPE: One fixed L089 congruence family and bounding domains, unchanged d=6, delta=3317760, literal F=G_o, original P1+ interval and all-place P2/P3. No field, interval, or source-authentication change; no average over unrestricted curves may be substituted without justification.

## Invocation-start proposal (preserved; coverage completed below)

Main gap remains original finite B>=A. A useful intermediate estimate
would show that enough actual survivors have small added cost
T=sum_(p in (S intersect (sqrt(H),U]) minus A) log p to satisfy
L116's residual budget. Its downstream use would be a same-member
prime satisfying L098's extra integrality premise. No complete repair
or main-target route is asserted.

The next review should search the exact arithmetic-average statement,
standard polynomial-divisibility sieve terminology, stronger available
uniform counting results and obstructions. Reuse L089's occurrence
assessment where applicable; inspect only its precise primary inputs
needed for the joint-count comparison. A count before imposing the
full-image survivor conditions does not suffice unless the exceptional
sets are controlled together. Distinguish numerator/denominator
cancellation in rational j from divisibility of the displayed polynomial.

Continue only with a theorem-level comparison giving an independently
testable uniform estimate on the relevant moving prime range and a
justified overlap with the retained survivors. Park or change this
proposal if an essential uniformity, height relation or simultaneous
selection premise is unavailable. Do not attempt a new average-value
lemma or mathematical script during the coverage turn.

Essential inputs: L089,L090,L098,L100,L101,L116. New unresolved
assumptions are actual-family denominator/height distribution and
uniform divisibility estimates after retaining the image conditions.
All initial-data/III/P7, directed (*), generation/full repair,
factor-four excess, action/factorization/pilot, authentication/def=,
essentiality and finite B>=A gaps remain. Mathlib coverage is unchecked.

## Completed comparison — 2026-10-25, step476

The main gap remains original finite B>=A. This is one source review of
the saved TARGET, with no new lemma, arithmetic estimate or mathematical
script. A later successful estimate could supply L098's additional
selected-prime integrality premise. It would leave the independent IUT
applicability and essentiality gaps unresolved.

### Primary inputs actually read

[Dana Moshkovitz, *An Alternative Proof of the Schwartz-Zippel Lemma*](https://eccc.weizmann.ac.il/report/2010/096/revision/1/download),
ECCC TR10-096 revision 1, 8 July 2010, pp.1–2, states the named
finite-field zero bound: a nonzero total-degree-d polynomial in m
variables over a finite field F has at most d|F|^(m-1) zeros. Read
sections 1–3 completely, including the d<|F| proof case and Lemma 3.1;
for d>=|F| the asserted upper bound is trivial. Import the named lemma,
not a new proof. Application must check nonzero reduction and degree
after fixing the lattice residues. The degree-zero case is separate.

[J. E. Cremona and M. Sadek, *Local and global densities for Weierstrass models of elliptic curves*](https://arxiv.org/pdf/2003.08454v3),
version 3, 18 October 2021, Proposition 3.1 and full proof, printed
p.11, treat any subset Sigma of (Z/MZ)^d with positive box weights.
Density is |Sigma|/M^d. Crucially, the proof retains explicit upper and
lower counts using floor(X^k_i/M), before taking a limit; its concluding
O-constant may depend on M and Sigma. A moving-modulus application must
use those prelimit counts and justify translations and the fixed lattice.
Proposition 3.4 and proof, p.14, require an admissible family and
measure-zero boundaries; Proposition 3.5 and proof, p.15, concern
simultaneous congruences for two coprime polynomials. They supply no
direct theorem for the present single-polynomial weighted moving window.
Those product-density results are comparisons only, not imported inputs.

[David Zywina, *Elliptic curves with maximal Galois action on their torsion points*](https://pi.math.cornell.edu/~zywina/papers/MaximalGalois.pdf),
15-page author version associated with Bull. London Math. Soc. 42 (2010),
811–826: Lemma 5.9 and its full proof, printed p.8, give h(j(E))
bounded by a constant times log R for integral short coefficients in a
fixed norm box over a fixed number field. The proof uses projective
height, so reduction of the quotient causes no difficulty for this
upper bound. It supplies no lower height bound. Reuse step338's
Proposition 5.7/composite-level assessment for the full-image exceptions;
the present scope changes neither level nor base field. The new reading
was needed for coefficient-to-height control, not to refresh ready
surjectivity coverage. No uniformity in the fixed lattice index is claimed.

### What remains to specialize, without deriving it here

Use L089's unchanged rectangle R/2<=A<=R, |B|<=R, B odd, inside its
fixed affine lattice, and its existing quadratic survivor count. The
proposed majorant is the sum of log p over primes up to a uniform
box envelope for U(H) that divide 4A^3+27B^2. This is a proposal for
a later proof, not an estimate or an identification with actual poles.
The proof must justify pole containment despite numerator cancellation.
Overcounting divisibility may give an upper bound; equating the two sets
without checking valuations is invalid.

The proposed test keeps all lattice constants fixed before R grows.
It must exhibit the congruence classes defining this lattice and parity,
bound their residue-block errors uniformly over the required prime range,
and treat primes dividing the fixed congruence modulus or polynomial
coefficients separately. No black-box uniformity in the asymptotic
density theorem is authorized. A proof using a common modulus that is
the product of all moving primes needs its own error control; single
prime counts and a first moment are the covered mechanism.

L101 identifies H with the logarithm of the reduced denominator of j;
coefficient size alone cannot be substituted for this value. A proposed
lower slice H>=(log R)/8 must be proved to discard sufficiently few
pairs. The existing per-j fiber cap in L089 and elementary enumeration
of reduced rational numbers provide an independently testable way to
address cancellation. No growing-height counting bound is asserted here.
The same count must control every fixed exceptional Legendre parameter
before selection. Do not presume a generic denominator lower bound.

Finally a first-moment/Markov bound must be compared with L089's actual
retained lower count, after subtracting its two full-image exceptional
sets. No independence theorem or conditional distribution on survivors
is needed if a valid ambient exceptional-set subtraction suffices; its
inequality is still unproved. Compare with the minimum of L116's M(H)
on the justified height range, rather than an unrelated coefficient
height. Continue only with uniform errors and a strictly positive
same-member count satisfying T<=M(H). Otherwise record the exact failed
inequality and park or change this arithmetic mechanism. No actual
counterexample follows from failure of a sufficient count.

### Search record, duplicate check and limits

Queries included `multivariable polynomial lattice points congruence
divisibility prime average number prime factors elliptic curves
discriminant sieve`, `Ekedahl sieve polynomial values fixed congruence
conditions small primes uniform lattice count`, `average bad reduction
primes elliptic curves discriminant polynomial short Weierstrass lattice`,
`multivariate Schwartz Zippel polynomial finite field bound`,
`Bhargava geometric sieve theorem 3.3 codimension k rB M log M pdf`,
and `Schwartz 1980 fast probabilistic algorithms verification polynomial
identities lemma 1 pdf`. Read the exact primary passages above. The
original Schwartz PDF endpoint returned 404; the complete alternative
primary proof was accessible, so this is not an essential source blocker.
Bhargava's original sieve theorem, the small-box polynomial-curve paper,
and the Atkin/Elkies average paper are uninspected leads, not inputs.
No matching constrained joint theorem was established by this search;
this does not establish novelty.

Reused occurrence coverage is in
`2026-10-19-auxiliary-full-mod120-occurrence.md` and
`2026-10-20-corollary-2-2-compact-family-occurrence.md` in this directory;
selection coverage is in `2026-10-25-selected-prime-pole-exclusion-budget.md`.
L089's existing finite-fiber argument, L101's exact height and L116's
conditional budget were read. ATTEMPTS/036 stops the scalar cap only;
ATTEMPTS/035 keeps repeated authentication retrieval parked. No duplicate
joint weighted estimate was found in the targeted records. No cross-
notebook result is used, and no source-authentication qualification is
removed. Mathlib full matching and supporting coverage are unchecked.

The concrete next attempt and its limits are recorded in
`2026-10-25-average-lattice-first-moment-specialization.md`. This review
does not approve mathematics performed during the present turn.
