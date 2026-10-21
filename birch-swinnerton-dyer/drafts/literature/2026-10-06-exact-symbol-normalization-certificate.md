# Exact symbol normalization and uniform denominator certificate: source assessment

TARGET: Assess whether a finite integral modular-symbol presentation and one certified nonzero quadratic-twist central value can certify L027's real-Neron symbol normalization and an all-level denominator bound without BSD or finite Sha.
CHECKED: 2026-10-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched exact modular-symbol normalization, quadratic-twist period comparison, finite Manin presentations and rigorous numerical modular symbols; checked the local precision assessment and ATTEMPTS/022 for duplication. Queries and inspected primary passages are recorded below.
SOURCE_EVIDENCE: Read Stein's online General Modular Symbols, Proposition 1.24 and Theorem 1.25 with generation/relations proofs; Cremona second edition Sections 2.3, 2.6--2.7 and 2.11; Pal arXiv:1012.0094v2, Proposition 2.5, Corollary 2.6, Lemma 3.1 and Theorem 3.2's positive-twist proof; Wuthrich arXiv:1608.06423v2, Proposition 1 with proof and Section 2.2; Stein--Wuthrich Sections 3 and 3.7, pp. 1762 and 1768--1769.
COMPARISON: Exact twist calibration and integral finite generation are known source mechanisms. They cover a conditional certificate with an independently certified normalized twist value; they do not certify an arbitrary software scale or produce that value under L027's hypotheses alone.
GAP: No actual eigensymbol, independently certified normalized nonzero twist value, uniform numerical C or coefficient is supplied. The remaining approved difference is finite certificate bookkeeping with explicit conventions and inputs, not a new calibration theorem or a universal production algorithm.
REASON: Primary coverage now permits a restricted conditional specialization; the general numerical path retains extra Manin/isogeny certification obligations. Separate the exact single-value input from its still-unperformed production, and do not repeat the conditional enclosure audit.
LITERATURE_REASON: The target changes from auditing a bound with exact normalization and C granted to producing their certificates; essential exact normalization and lattice coverage was explicitly excluded before.
SCOPE: Non-CM E/Q at good ordinary p>=5, global minimal model, primitive trivial branch, total real Neron period and kappa(gamma)=1+p; allow L(E,1)=0. The specialization grants a correctly identified one-dimensional real plus functional on the full relative symbol module and an independently certified rational nonzero L(E^ell,1)/Omega(E^ell), with prime ell=1 modulo 4 coprime to p times the minimal discriminant. No BSD, finite Sha or rounded period ratio is granted.

The request/test and recovery comparison below preserve the starting proposal.
The completed source determination follows them; earlier statements that no
review had been performed refer to that proposal stage.

## Target and discriminating test

Main gap: rank E(Q)=m(E) for m(E)>=2. This narrower input target could
make L027 executable on certified data; it does not guarantee its b
excludes zero. Essential local inputs are L027, L004 and foundations/05;
L026 remains only a downstream use with all its additional hypotheses.

The review must identify a primary theorem or rigorous algorithm that
recovers the exact scale of a rational plus eigensymbol, controls the
total-real-period convention and twist period factors, and turns a
finite integral presentation into a proved bound at every rational
argument used by L027. Specify any required optimal-curve, Manin
constant, isogeny or twist-discriminant restrictions; do not silently
add them to L027. A certified twist central value is a proposed input,
not an already available number, and its exact period normalization
must not presuppose the scale being recovered.

Continue to a narrowly stated specialization only if the inspected
inputs remove this circularity and certify both scale and uniform C.
If they yield only floating-point calibration, sampled denominators
or assume the desired normalization, record that obstruction and stop
that mechanism. A missing exact-scale input may be isolated, but it
must remain explicit. This review is not authorized to implement or
prove a proposed calibration method during its literature-only step.

## Recovery comparison

Three mechanisms were compared for the next direction. Exact symbol
calibration addresses a missing supplied input independently of the
already verified tail proof and is selected. A rational exterior-square
import retains finite-Sha or domain gaps in the 2026-10-04 arithmetic
rank-two assessment; no new source lead presently reopens it. Generic
common-field splitting retains the strict-degree obstruction in
ATTEMPTS/020 and the 2026-10-05 period-index comparison. Repeating
either earlier mechanism without a new arithmetic input is rejected.

ATTEMPTS/022 preserves the limit of repeated enclosure verification;
ATTEMPTS/021's finite-defect obstruction is also unchanged. The older
blocked Nekovar/Jones sources remain parked, not retried. There is no
new access blocker in the completed L027 audit. No new theorem, novelty
claim, mathematical derivation or approval of this uncovered target is
made. Mathlib coverage for this production target: not checked.

## Completed source determination, 2026-10-06

The answer is conditional on what “certified central value” means. Require
an exact rational q with an independent proof that
q=L(E^ell,1)/Omega(E^ell) != 0, where Omega integrates the absolute
minimal Neron differential over the entire real locus. A nonzero raw
L-value or an unproved floating-point period quotient does not meet
this input requirement. Certification using the unknown E-symbol scale
would be circular. No such q is supplied in this notebook.

### Finite presentation input

[Stein, *Modular Forms, a Computational Approach*, online General Modular
Symbols](https://www.wstein.org/books/modform/modform/modular_symbols.html),
Definition 1.23, Proposition 1.24 and Theorem 1.25, covers a finite-index
subgroup G of SL_2(Z) and integer weight k>=2. The torsion-free symbol
module is generated integrally by the finitely many Manin symbols from
right cosets and monomials. Its presentation uses the two-term,
three-term and central-element relations, followed by killing torsion.
The continued-fraction proof introduces no denominators. Import these
statements at G=Gamma_0(N), k=2; do not reprove the presentation.
The relevant proof and Remark 1.26 were read: independently quotienting
only residual generators can lose relations. This input concerns the
full relative module, not just cycles. Values on arbitrary cusp paths
must be represented there. Remark 1.43 also warns that Stein's star
involution and Cremona's convention differ by a sign.

### Exact twist calibration input

[Cremona, *Algorithms for Modular Elliptic Curves*, second edition,
corrected online Chapter 2](https://johncremona.github.io/book/fulltext/chapter2.pdf),
Section 2.3, p. 18, gives integral continued-fraction conversion;
Sections 2.6--2.7, pp. 25--26, describe the dual eigenvector, determined
up to scalar. Section 2.11, pp. 38--39, proves, for an odd prime ell
not dividing N and its quadratic character chi, that the cycle
gamma_ell=sum chi(k){0,k/ell} has period
P(ell,f)=sqrt(ell*) L(f tensor chi,1), with ell*=chi(-1)ell.
For ell=1 modulo 4 it lies in the real homology. The Gauss-sum
derivation and equation (2.11.4) were read, not just the numerical
algorithm. The latter determines modular-form periods; identifying
those with the particular curve's Neron periods remains essential.
Its prime-search discussion has a square-conductor qualification, so
it is not imported as an existence guarantee for our selected twist.

### Exact period input and restricted applicability

[Pal, *Periods of quadratic twists of elliptic curves*,
arXiv:1012.0094v2 (21 January 2011)](https://arxiv.org/pdf/1012.0094v2),
Proposition 2.5 and Corollary 2.6, pp. 5--6; Lemma 3.1 and Theorem
3.2, pp. 7--8, use a global minimal E and square-free d. For d>0,
Omega(E^d)=u_tilde Omega(E)/sqrt(d). The factor is obtained from
the transformation to a minimal twist; it need not be a power of two.
Corollary 2.6 states u_tilde=1 when d is coprime to the minimal
discriminant and d=1 modulo 4. The corresponding odd-prime and
2-adic cases of Proposition 2.5 and the full positive-real integral
comparison were inspected. Thus the proposed prime restriction has
primary coverage. Negative twists and unrestricted bad-prime factors
are outside the continuation. These period identities do not assume
BSD or finite Sha. The published paper is Proc. Amer. Math. Soc. 140
(2012), 1513--1525; theorem numbering here refers to the inspected v2.

### Normalization match and existing calibration mechanism

[Stein--Wuthrich, *Algorithms for the arithmetic of elliptic curves
using Iwasawa theory*, Math. Comp. 82 (2013),
Section 3, p. 1762 and Section 3.7, pp. 1768--1769](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=6)
defines the plus symbol as the real part of 2pi i integral_(infinity)^r f
divided by the total real Neron period, with [0]^+=L(E,1)/Omega(E).
Section 3.7 explicitly explains nonzero quadratic-twist calibration
when the untwisted central value vanishes, including recovery of a
rational scalar. This is a known mechanism. Its broad period-factor
statement is not used in place of Pal's exact minimal-model formula.
The specialization must match orientations and the real integration
functional, rather than trust a software “plus” label. No new twist
identity or coefficient enclosure is derived in this review.

### Limits of the numerical route

[Wuthrich, *Numerical modular symbols for elliptic curves*,
arXiv:1608.06423v2 (23 March 2017)](https://arxiv.org/pdf/1608.06423v2),
Section 2, Proposition 1 and its proof, pp. 3--4, assumes Manin
constant c0=1 for the X_0-optimal curve. With delta^2 the largest
square dividing N, primes ell>2 coprime to N and ell=1 modulo delta
give t0=gcd #E(F_ell). Put q^+=Omega_E^+/Omega_E0^+ and t^+ the
numerator of t0 q^+. The stated all-cusp lattice is
[r]^+ in c_infinity(E0)/(2t^+) Z. Its proof uses cuspidal torsion,
unramified torsion reduction and both real-lattice shapes. These are
least-positive-period symbols, unlike L027's total-period convention.
Section 2.2, p. 6, exposes the Manin and optimal-curve identification
obligations. Merely expecting a later rounding failure is not a
certificate. Section 3.1, Lemma 4 with proof, supplies rigorous
Fourier-tail bounds, but does not discharge those arithmetic inputs.
No unqualified software certification is imported.

## Decision, useful difference and continuation test

SPECIALIZE permits a conditional finite certificate assembly using the
inspected presentation, twist identity and exact period comparison.
No theorem reproof is needed. The remaining mathematical work is to
express calibration in the exact relative-functional convention and
carry its scalar through every generator to a proved all-argument C.
That bookkeeping is deferred to a research turn; this assessment does
not claim the resulting formula or a lemma already proved.

The finite lattice requirement is stronger than sampled symbols: a
certificate must include the complete generating presentation and the
functional's relation checks. A basis of absolute cycles alone leaves
relative paths and possible cusp denominators uncovered. The matching
one-dimensional real functional is a granted independently checkable
input, not a claim that any rational vector with a few matching Hecke
eigenvalues suffices.

Continue only if the future argument identifies the exact scale from
the independently certified q and proves its C on all relative paths.
Stop or isolate the failed implication if a sign, factor of two,
unaccounted coordinate denominator, incomplete eigenline identification
or circular value certificate remains. q-production and a_2
nonvanishing remain separate unperformed tasks. L026 additionally
retains its arithmetic/residual-family conditions, rational Kummer
membership and complex-order comparison. No new rational-rank input
or BSD candidate results from this source review.

## Search and access record

Queries included `Cremona modular symbols normalization quadratic twist
exact periods Manin constant`; `Wuthrich modular symbols normalization
quadratic twist rigorous scaling periods`; `Pal periods quadratic twists
elliptic curves period formula lemma real Neron`; `Christian Wuthrich
numerical modular symbols rigorous denominators 2018 theorem Manin
constant`; `site.wstein.org modular forms modular symbols Manin trick
integral presentation theorem`; and `Periods of quadratic twists Pal
arxiv theorem 3.2`. Search snippets and secondary mirrors only located
sources; the primary passages above supplied the comparison.

Shell DNS, PDF screenshots and ar5iv retrieval failed. The relevant PDF
text and HTML remained accessible through web retrieval, so this is
not SOURCE_BLOCKED. Sage source cautions are reused from the earlier
assessment; no fresh full-source reread was needed. References to
Murty--Murty, Merel and later Manin-constant results are unread leads
for any broader production target, not imported assertions here.
Mathlib: the full production certificate and supporting symbol-lattice
coverage were not checked; unknown availability is not absence.
