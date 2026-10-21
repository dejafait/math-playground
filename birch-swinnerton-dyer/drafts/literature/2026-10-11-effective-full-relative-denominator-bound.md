# Effective full-relative denominator — primary-source comparison

TARGET: Assess whether effective bounds for modular-parametrization degree and Manin constant give a computable bound B(E) for the reduced denominators of every full-relative Neron-normalized integral-generator value for arbitrary minimal E/Q, without assumed optimality or a supplied isogeny map.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched Manin constant/divides modular degree, effective upper modular degree bounds, arbitrary-curve modular-symbol denominators and nonunitary cusps; checked L027/L028/L043/L045, earlier exact-normalization/optimal-period assessments and ATTEMPTS/022--024; found and read the unconditional factor-six theorem, explicit optimal degree bound and full cusp-reduction proof. Queries and access qualifications appear below.
SOURCE_EVIDENCE: Cesnavicius--Neururer--Saha, author PDF dated 2022-01-28, Theorems 1.2/7.2 pp.3,45--46 with complete final proof; von Kanel, Trans. LMS 1 (2014), 85--115, published DOI full text, Section 5.2/Lemma 5.1 with complete proof and Section 4/Lemma 4.1 with complete proof; Wuthrich arXiv:1608.06423v2 (2017-03-23), Proposition 1 with complete proof pp.3--4 and Section 2.2 p.6; Cremona corrected second edition, Section 2.8 p.30, total-period definition following (2.8.9).
COMPARISON: Accessible known inputs remove the need to assume Manin constant one or identify the actual optimal model for a coarse bound: the degree theorem concerns the canonical newform quotient, the named cyclic-isogeny bound is existential, and the Manin theorem applies to every parametrization. Wuthrich's displayed Proposition 1 remains conditional; its cusp proof retains the differential scalar. The arbitrary-curve/full-relative/total-period assembly is a future specialization, not proved here.
GAP: Assemble an explicit computable reduced-denominator bound using these independent inputs, retaining the factor six, all cusp-pair endpoints, both real-lattice types and the total minimal period. No B(E), exact normalization, clearing integer or implementation is produced in this literature turn.
REASON: New inspected theorem coverage changes the general-scale route from REVIEW_REQUIRED to a known-method specialization; no original theorem or progress beyond the checked literature is claimed.
LITERATURE_REASON: The saved changed arbitrary-curve target lacked essential source coverage; earlier fixed optimal/supplied-isogeny assessments explicitly excluded this scope.
SCOPE: Arbitrary globally minimal E/Q, including additive reduction and CM, with independently certified exact conductor N and its modular newform; all torsion-free integral relative generators. No identified optimal equation, supplied isogeny map, Manin conjecture, nonzero twist value, rational-rank or Sha hypothesis.

Essential local inputs for comparison: L027's exact-normalization and
all-level denominator hypotheses; L028's independent-scale requirement;
L043's complete relative lattice and source-optimality qualifications;
L045's supplied-isogeny hypothesis; L046 and audited L047 as a fixed
downstream example. These are comparisons, not a claim that the desired
arbitrary-curve bound follows from them.

The proposed threshold is a finite, computable positive integer B(E),
obtained from the minimal equation and certified finite modular data,
such that each reduced denominator of I(g_i)/Omega(E) is at most B(E),
for every generator of a complete integral relative module. Omega is the
total minimal real Neron period. An absolute-cycle-only result or a bound
whose inputs already require the unknown normalized scale does not meet
this threshold. Distinguish a denominator bound from a common denominator
and from exact recovery of the values. No formula for B(E) is proposed.

Plausible downstream use: together with independent finite integration
enclosures, such a bound could make exact normalization recovery available
beyond the fixed optimal-source and explicit-isogeny cases. Whether those
enclosures and exact recovery can be certified remains a separate task.
Uniform coefficient nonvanishing, rational directions, Sha defects and
comparison with complex order remain unresolved even if this target works.

Continue only with a primary result whose effective inputs can be supplied
independently, including the cusp contribution and period convention.
If the best bound assumes the desired scale, unverified optimality, or an
unavailable isogeny input, record that obstruction and change mechanism;
do not repeat fixed coefficient audits. Check exact terminology, stronger
results, local duplicates and ATTEMPTS/022--024 before approval. Those
historical stops remain evidence, not global prohibitions. No cross-notebook
input, new lemma, proof or mathematical calculation is part of this proposal.

## Review result and exact remaining specialization

The original proposal above is preserved. The completed source comparison
approves a later assembly using known bounds, rather than another fixed
coefficient audit. It does not assert that the desired B(E) has already
been derived. The [continuation assessment](2026-10-11-arbitrary-curve-denominator-specialization.md)
records that exact mathematical target for separate next-turn approval.

The main gap is unchanged: rank equality for arbitrary complex order at
least two. The useful intermediate threshold is a finite computable bound
on every reduced relative-generator denominator. Its downstream use is
independent rational isolation of normalization values. Existence and
verification of those integration enclosures, exact recovery, coefficient
nonvanishing, rational directions, Sha removal and complex-order comparison
remain independent tasks. In particular, a very large effective bound need
not yield a practical implementation.

## Primary statements actually inspected

**Differential scalar.** [Cesnavicius--Neururer--Saha, *The Manin constant
and the modular degree*](https://maths.qmul.ac.uk/~asaha/research/manin-paper.pdf#page=45),
PDF dated 28 January 2022, Theorems 1.2/7.2, pp.3,45--46, treats every
surjection X_Gamma -> E at E's exact conductor, for
Gamma_1(N) contained in Gamma contained in Gamma_0(N). With the minimal
Neron differential, phi^*omega_E=c_phi omega_f and c_phi is a nonzero
integer. Unconditionally c_phi divides 6 deg(phi). The extra valuation
is at most one, only at 2 with v_2(N)>=3 and no divisor prime 3 modulo
4, or at 3 with v_3(N)>=3 and no divisor prime 2 modulo 3. Thus the
factor-six version covers all conductors; the sharper version must not
be imported unrestrictedly. The complete proof's final branch uses
6 omega_f on the Jacobian when rational singularities are not granted.
Optimality of E is not a hypothesis. This is a named theorem import,
with no reproof. It alone gives no numerical degree bound.

**Effective degree and bounded existential isogeny.** [Von Kanel,
*Integral points on moduli schemes of elliptic curves*, Trans. London
Math. Soc. 1 (2014), 85--115](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/tlms/tlu003),
published Section 5.2, Lemma 5.1(i), gives
log(m_f)<=N(log N)^2/2 for a normalized weight-two newform of exact
level N with rational integer coefficients. Here m_f is the degree of
X_0(N)->E_f, with E_f=J_0(N)/I_f J_0(N); it is not the degree of an
arbitrary target map. The complete proof was read, including congruence
divisibility, the nonsingular Fourier minor, algebraic-integer/Galois
argument, Hadamard bound and explicit final estimates. No unknown Manin
constant enters this degree bound. Section 4, proof of Lemma 4.1,
explicitly imports Mazur--Kenku's cyclic-isogeny classification (Kenku,
JNT 15 (1982), 199--202, Theorem 1): a minimal-degree Q-isogeny between
Q-isogenous elliptic curves is cyclic and has degree at most 163. Its
complete short proof was read. This is existential input for future
composition, not a produced isogeny map or identification of E as optimal.

**All cusps and torsion reduction.** [Wuthrich, *Numerical modular symbols
for elliptic curves*, arXiv:1608.06423v2](https://arxiv.org/pdf/1608.06423v2#page=3),
23 March 2017, Proposition 1 and proof pp.3--4, sets delta^2 to the
largest square dividing N. All cusp images are torsion over Q(zeta_delta).
At a good prime ell>2 with ell=1 modulo delta, the residue field is F_ell;
unramified torsion reduction is injective, including ell-primary torsion,
by the cited Silverman, *Arithmetic of Elliptic Curves*, second edition,
VII.3.4. Hence a finite gcd of the point counts annihilates the cusp
images. The proof retains c_0 and handles rectangular/nonrectangular
period lattices. Its displayed denominator result assumes c_0=1 and
uses q^+; neither is an unconditional theorem for this target. Section
2.2 p.6 explicitly retains these implementation limitations. Future work
must apply the underlying pullback/cusp argument to the target curve
and retain its integer c_phi, rather than assume the displayed formula.
The degree and differential bounds address this identified difference;
it is not derived here. Primes in the required progression can be
enumerated using the standard Dirichlet theorem; no cutoff is promised.

**Total real period.** [Cremona, *Algorithms for Modular Elliptic Curves*,
corrected second edition (1997), Section 2.8 p.30, following (2.8.9)](https://johncremona.github.io/book/fulltext/chapter2.pdf#page=24)
states that the total period is twice the least positive real part of
a full period for either real-lattice type. This passage was read. It
does not require the target's lattice to equal the newform period image.
Its convention, already retained in L043, must be used on the minimal
target E; using only the least positive purely real period loses a
component factor.

These primary statements cover the proposed mechanism. Modularity and
integral Manin generation are standard inputs already used locally;
L028/L038 supply the presentation convention. There is no reason to
reprove the classification, degree theorem, Manin theorem or
Manin--Drinfeld theorem. Only their explicitly identified specialization
to all relative target values is authorized for later work.

## Searches, overlap, access and qualifications

Queries included `Manin constant divides degree modular parametrization
Cesnavicius arbitrary elliptic curve`; `modular symbols denominators
arbitrary elliptic curve effective bound cusps modular degree Manin
constant`; `effective upper bound modular degree elliptic curve arbitrary
conductor explicit Watkins upper`; `modular degree upper bound elliptic
curve N 2 effective bound Manin constant`; `Manin constant bound Edixhoven
effective`; `von Kanel integral points moduli elliptic curves Lemma 5.1
modular degree pdf`; and `Kenku 1982 Theorem 1 163 isomorphism classes`.
They found the sources above. No novelty is inferred from these searches.

The earlier exact-normalization assessment left later Manin-constant
results unread; the fixed optimal-period assessment retained semistability
and an identified optimal model; L045 retained a supplied prime-degree
map. The present universal factor-six/explicit-degree coverage is a
materially different input, not a duplicate proof of L028/L043/L045.
ATTEMPTS/022--024 stop repeated conditional audits as production. Their
evidence and the uniform-twist source blocker are preserved; this review
uses neither uniform twist nonvanishing nor another fixed schedule.

The Nottingham preview of Wuthrich failed; the versioned arXiv primary
PDF succeeded. The first Oxford full-text request failed; Wiley's
published primary full text succeeded. Von Kanel's author research page
identifies the published part of arXiv:1310.7263v2. That PDF was checked
only for version/theorem locations: Lemma 5.1 is pp.27--29 and its
Lemma 4.1 is broader than the published lemma, with the elliptic bound
in its (ii). Published numbering controls the citations above.

Direct retrieval of Kenku's original ScienceDirect article and PDF
(DOI 10.1016/0022-314X(82)90025-7) returned 403. Its original proof was
not read. The classification is imported as a standard named theorem
through the inspected explicit statement and complete bounded-isogeny
argument in von Kanel, not through a search excerpt. No dependent
reproof of Kenku is proposed. Watkins's lower-bound paper and conditional
symmetric-square degree algorithms are not adequate upper-bound inputs;
only their search descriptions were inspected. Stronger asymptotic
degree bounds and Belabas--Bernardi--Perrin-Riou's computational work
remain unread leads, unnecessary for this coarse effective target.

Mathlib: full matching arbitrary-curve effective-denominator theorem and
support for the new degree/Manin/classification inputs were not checked.
No absence claim follows. This literature turn modifies no lemmas or
mathematical scripts, runs no calculation and adds no DAG node. The
source coverage is local progress within known mathematics, not a BSD
resolution or discovery beyond the sources.

## Continuation and abandonment test

The later proof must provide an actual finite computable B(E) from
independent conductor/finite arithmetic, without an optimal-model label,
unknown normalized scale or supplied isogeny. It must cover nonunitary
cusps, both endpoints of every integral relative path, zero values and
the total minimal real period. It must distinguish the size bound on
reduced denominators from a proved common clearing integer: an upper
bound on c_phi is not automatically a multiple of c_phi. Stop the
proposed assembly if it needs an exact unknown differential scalar,
unproved optimality, an unavailable map or only absolute-cycle data.
An obstruction would require another mechanism; repeating L047 is not
the continuation. The full proof and any resulting lemma belong to a
separately approved research turn.
