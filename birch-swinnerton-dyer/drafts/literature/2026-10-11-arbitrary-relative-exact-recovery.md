# Arbitrary-relative exact recovery — completed source comparison

TARGET: Construct a terminating exact recovery of every full-relative Neron-normalized integral-generator value for arbitrary minimal E/Q using L048 and independently certified integration and total-real-period enclosures.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched numerical modular symbols/nonunitary cusps/rigorous errors, real-period AGM bounds, bounded-denominator rational reconstruction and Sage normalization; inspected Wuthrich's analytic/transportation sections and Cremona's arbitrary-cusp Hecke closing and both real-period cases; compared L048, fixed-case assessments and ATTEMPTS/022--024.
SOURCE_EVIDENCE: Wuthrich arXiv:1608.06423v2 (2017-03-23), Sections 3.1--3.3 pp.5--7 with Lemmas 4/6 and complete proofs, Sections 5.1--5.2 pp.10--12; Cremona corrected second edition (1997), Proposition 2.2.3 with proof pp.16--17, equations (2.4.1)/(2.9.1) and arbitrary-cusp remark pp.18--19,31--32, Section 3.7 pp.97--98; DLMF 19.8.1--19.8.5; details below.
COMPARISON: Known unnormalized Hecke/transportation algorithms cover arbitrary cusps, and positive-real AGM identities cover both period cases without optimality; L048 supplies unconditional denominator information. This is a known-algorithm specialization, not a new method. Conditional Sage normalization is insufficient as a direct import.
GAP: Write and verify oriented closing/cusp matrices, certified finite-function and positive-AGM enclosures, division by a positive total minimal period, and exact reconstruction with termination including zero. No assembled recovery theorem or certificate is proved in this review.
REASON: Essential analytic coverage is now inspected; approve the unchanged target for a separate mathematical attempt, importing known identities and checking the specified specialization.
LITERATURE_REASON: The start target was REVIEW_REQUIRED and its arbitrary-cusp analytic and certified-period scope exceeded the ready denominator and fixed-instance assessments.
SCOPE: Arbitrary global minimal E/Q including CM and additive reduction; supplied exact conductor N, associated normalized newform and a complete finite integral relative generating set; zero values and nonunitary cusps included; no supplied optimal curve, isogeny, unknown normalized scale or twist nonvanishing.

## Initial proposal retained (superseded by the completed review below)

The following proposal records the state before this literature turn;
its unread-source and approval wording is historical.

Essential local input: audited L048 with its exact hypotheses and
computable bounds. A complete generating set is granted in this target;
constructing or auditing generic presentation software is outside scope.
The prior full-relative convention in L028/L038 is a comparison, and
L027 is a possible downstream use, not a recovery premise. No
cross-notebook theorem is proposed.

The next turn must search the exact statement and known rigorous
numerical-modular-symbol algorithms, then inspect primary hypotheses
and relevant cases before approving mathematics. Wuthrich,
*Numerical modular symbols for elliptic curves*,
[arXiv:1608.06423v2](https://arxiv.org/pdf/1608.06423v2),
is a specific lead: the already inspected Proposition 1 proof supplies
cusp information only; the integration algorithms and their sufficiency
for this exact target remain unread leads. Do not import its conditional
displayed normalization formula as an unconditional enclosure algorithm.
Use the recorded fixed-case sources for comparison only after identifying
the exact additional generality needed. Mathlib coverage is not checked.

Continue if independently computable analytic bounds provide certified
enclosures of arbitrarily small width for every required normalized
value, including all endpoint and real-period cases, so L048 can support
exact recovery. Stop or narrow the proposed mechanism if it requires
the unknown scale, unproved optimality, inaccessible essential cusp
expansions, or merely floating-point convergence. This file asserts no
convergence or reconstruction theorem and approves no new mathematics.

Downstream use is production of exact normalized inputs for L027 beyond
the fixed cases. Neither this target nor L048 promises practical runtime,
coefficient nonvanishing, independent rational points, removal of Sha
defects or comparison with complex order. The main rank-equality gap
remains unresolved. ATTEMPTS/022--024 prohibit repeating conditional
audits as production, not this distinct test of actual enclosure inputs.

## Completed review — 2026-10-11, BSD-162

The main gap is still arbitrary rank equality for analytic order at least
two. The one intermediate target is TARGET above, potentially furnishing
L027's normalized inputs beyond the fixed cases. This is source comparison
only: no recovery lemma, numerical value or mathematical script is created.

### Inspected primary inputs

**Unnormalized integration.** [Wuthrich v2](https://arxiv.org/pdf/1608.06423v2)
has title-page date 20 March 2017 and version date 23 March 2017.
Read primitive (2), Section 3, and relevant Section 5 cases.
Lemma 4 assumes Im(tau)=y>0, epsilon>0 and integer
T> -log(2*pi*y*epsilon)/(2*pi*y); its error is below epsilon.
The complete proof bounds the tail by
exp(-2*pi*T*y)/(exp(2*pi*y)-1). Lemma 6 assumes 0<epsilon'<1,
T evaluated terms and correctly computed q; its Horner condition is
2^(-b)<epsilon'/(2*T*(T+epsilon')). Neither encloses the period.
Section 5.1, (11), treats Gamma_0(N)-equivalent endpoints by
lambda(tau)-lambda(gamma*tau), constructing gamma by Bezout and
a solvable congruence. Section 5.2 closes nonunitary a/m with a good
prime ell=1 mod gcd(gcd(m,N),N/gcd(m,N)); the scalar's absolute
value is #E(F_ell)>0. These analytic operations do not use optimality
or Manin constant one. The p.3 rounding paragraph uses a clearing
integer; Proposition 1's conditional bound is not imported.
L048 supplies independent clearing.

**Oriented closing.** [Cremona, Chapter 2](https://johncremona.github.io/book/fulltext/chapter2.pdf),
corrected second edition (1997), Proposition 2.2.3 pp.16--17 was read
with all implications and the constructive congruence proof. Reduced
cusp fractions are inputs; a Gamma_0(N) matrix is constructed.
Section 2.4 pp.18--19 gives the full good-prime operator (2.4.1) and
integration adjointness. Section 2.9, (2.9.1), pp.31--32 gives closing
for {alpha,infinity}; its final remark covers arbitrary alpha when the
good prime is 1 mod N. The preceding central-vanishing discussion
motivates an application; the operator identity has no vanishing premise.
This stronger prime condition is an available alternative to the faster
cusp-dependent condition. Section 2.6, (2.6.1)--(2.6.2), p.25 supplies
good/bad coefficient recurrences; exact conductor/newform association
remains granted. Section 2.8 p.30 after (2.8.9) gives total period
twice the positive real generator in the rectangular case, once otherwise.
No optimal-period equality is imported.

**Independent target periods.** [Cremona, Chapter 3](https://johncremona.github.io/book/fulltext/chapter3.pdf),
Section 3.7 pp.97--98 starts from the given Weierstrass equation and
roots of x^3+(b2/4)x^2+(b4/2)x+b6/4. For e3>e2>e1 real,
(3.7.1) gives lambda1=pi/AGM(sqrt(e3-e1),sqrt(e3-e2)), using
positive roots. For one real e3 and conjugate e1,e2, it gives
lambda1=pi/AGM(|z|,s), z=sqrt(e3-e1)=s+it, s>0. Both
paragraphs and the preceding full-lattice discussion were read.
Nonzero discriminant separates these cases. The algorithm uses
floating-point roots, so it is not itself an enclosure certificate.
Apply the identities to the target minimal differential; root isolation,
branches and outward errors remain to be supplied. CM and additive
reduction are not excluded.

[DLMF 19.8(i)](https://dlmf.nist.gov/19.8.i), 19.8.1--19.8.5,
supplies the positive-input AGM iteration, common limit and integral
identities; positivity hypotheses and convergence statement were read.
It does not prescribe a precision schedule. Sturm's real-root isolation
theorem and elementary Taylor remainder bounds are standard named
inputs for algebraic and finite transcendental enclosures. The later
proof must state their applications and prove enclosure shrinking,
including accumulated errors; decimal convergence is insufficient.

### Qualifications and the approved specialization

The extracted Wuthrich p.9 convention is lambda(r)-lambda(r') for
paths r' to r, while p.12 prints a_ell-ell-1 with paths pointing
toward r. This suggests a sign inconsistency; it is a source-comparison
finding, not a proved correction. The Nottingham author PDF has the
same extracted display. Do not silently copy it or infer the sign from
extraction. Check orientation from Cremona (2.4.1)/(2.9.1) and the
primitive definition in the mathematical turn. A limited rederivation
is justified by the suspect display and local oriented convention;
the imported transport identity does not need reproof.

Approve finite assembly and error bookkeeping for the unchanged scope:
both endpoints, integral combinations, zeros, independent positive
total target period, and exact recovery using L048's clearing K(E).
B(E) is only a size bound. The test should exhibit an enclosure of
the scaled value containing exactly one integer and prove refinement
terminates. Source rounding is already known; its period error and
unrestricted denominator must be included explicitly. No new algorithm
or improved complexity is claimed.

Transportation uses the infinity Fourier primitive at interior points;
new cusp expansions are not an input. Dirichlet's theorem permits
good-prime enumeration in 1 mod N, as a standard named import.
The matrix congruence need not be optimized, and (11) permits a fixed
interior point without the hyperbolic/parabolic optimization. Finishing
behavior and applicability must still be written in the research turn.

### Search, duplication and access record

Read L048's full hypotheses/conclusion and named-input scope, and
ATTEMPTS/022--024 in full; reused its denominator assessment and the
fixed-case one-root and optimal-cycle comparisons. No earlier local
arbitrary-relative recovery theorem was identified in those targeted
paths. Fixed certificates do not supply a universal assembly. Preserve
the conditional-audit stops and independent twist-source blocker.

Queries: `Wuthrich numerical modular symbols elliptic curves non unitary
cusps rigorous error 1608.06423`; `elliptic curve real periods AGM
rigorous error bounds Cremona algorithms 2.8`; `rational reconstruction
bounded denominator interval modular symbols certified`; `site.sagemath.org
modular symbols numerical Manin constant rigorous rounding errors`.
The arXiv page lists v2 as latest; no v3 is listed. Search located the
published Math. Comp. reference, but that version was not inspected.

[Sage module documentation](https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/mod_sym_num.html),
algorithm and note, was read: it retains Manin constant one outside
the tables and divides by the least positive real period. A call is
not an unconditional substitute for the proposed proof/convention.

Optional FLINT/Arb AGM/ball-arithmetic pages failed to open despite
indexed excerpts; those excerpts are not inspected theorem coverage.
The generic complex-integration page was accessible, but treats finite
bounded paths and admits failure, not arbitrary cusp convergence.
No software guarantee is imported. Essential Wuthrich/Cremona/DLMF
coverage remains accessible. Shell PDF download failed at DNS; browser
PDF reads succeeded. Full matching Mathlib coverage was not checked.

The current [Clay page](https://www.claymath.org/millennium/birch-and-swinnerton-dyer-conjecture/)
still links [Wiles's official description](https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf).
Read printed p.2: the conjecture asserts rank equals central complex
order for every E/Q; Remark 1 separately states the refinement. No
target or foundational argument changes in this review.

### Continuation and abandonment test

SPECIALIZE covers the unchanged TARGET/SCOPE only. The next step is a
separate proof attempt using L048 and the inspected analytic identities.
Continue only if independently certified enclosures shrink at every
supplied generator and exact scaled-integer isolation terminates,
including zeros and both period cases. Abandon or narrow if unknown
scale, unverified optimality, unavailable cusp expansions or uncertified
convergence becomes essential. No recovery theorem has been proved here.

Even successful recovery leaves exact arithmetic and complete generating
paths granted, generic executable correctness unproved, and L027's
nonzero coefficient and remaining premises unproduced. Rational
directions, Sha defects and complex-order comparison still prevent a
BSD candidate. Original Kenku and Manin presentation-injectivity proofs
remain qualified named imports in L048. No cross-notebook input is used.
