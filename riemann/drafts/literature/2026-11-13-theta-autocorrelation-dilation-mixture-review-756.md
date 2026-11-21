# Theta-autocorrelation dilation mixture: completed source review757

TARGET: Assess a positive probability mixture of normalized dilations of the complete unweighted actual-theta autocorrelation as a sufficient representation for L233's A/A(0); compare known representation criteria and recorded stops, and nominate one exact moment or tail obstruction test only if independently justified.
CHECKED: 2026-11-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed bounded exact-class, Mellin scale-mixture and moment-matrix searches757; inspected primary passages and compared L233/C233c plus the September23, September27 and October31 records. Queries and limits below; no novelty inference.
SOURCE_EVIDENCE: Csordas1309.0055v2 (2014), (3.5), Theorem3.5/(3.7), Remarks3.8(a), Theorem4.5/(4.6), https://arxiv.org/html/1309.0055v2 ; Belomestny-Morozova-Panov2211.01799v2 (2024), Sections1-2,(1)-(3),Lemma2.1 and AppendixB.1, https://arxiv.org/html/2211.01799v2 ; Schmudgen2008.12698v1 (2020), Section3,Theorems3.1-3.2 and proofs, https://arxiv.org/html/2008.12698v1 .
COMPARISON: Known autocorrelation positivity covers the building block, not the proposed mixture identity. Mellin product factorization and moment-matrix necessity provide a finite necessary-condition diagnostic independent of the missing Fourier sign. No inspected theorem constructs the proposed actual-theta mixture or decides that diagnostic.
GAP: Local normalization, the exact inverse-scale moment identification, all endpoint and integrability justifications, and a certified sign for one three-value determinant remain unpaid. Full representation and actual first/higher signs remain open.
REASON: Coverage permits one ordinary moment-necessity specialization, rather than fitting mixtures or restating spectral positivity. Nominate the bounded test separately; perform no specialization or calculation in this literature-only turn.
LITERATURE_REASON: The proposed building block is the complete actual-theta autocorrelation, rather than a Gaussian; assessment753 does not cover this hypothesis or its measure and dilation endpoints.
SCOPE: Review757 covers the saved representation proposal and the necessary-condition mechanism only. The separate finite-test proposal receives next-turn approval; neither actual-theta obstruction nor construction is established.

## Preserved nomination756 (unproved question, not current instructions)

For clarity, with the same k as L019/L233, the proposed building block
is H(t)=integral_R k(s+t)k(s-t) ds. The question is whether there is
a positive Borel probability measure mu on finite b in (0,infinity)
such that A(t)/A(0)=integral H(bt)/H(0) dmu(b) for every real t.
The restriction b>0, possible endpoint limits, and any moment or
differentiation assumptions must be assessed explicitly; none is paid
by this nomination. Do not use the symbol H for any notebook heat-flow
contract here. No numerical fitting is proposed.

Plausible downstream use: a justified positive mixture of known
autocorrelations could certify the first associated Fourier sign.
Higher/mixed signs, S3/H2 and global RH assembly remain independent.
The source review should check dilation/Mellin mixture terminology,
stronger known criteria, and exact local duplicates before any proof
attempt. Reuse ready source coverage only within its actual scope.
L019/L233 and C233c are the essential local objects/contrast; no
cross-notebook input is proposed. Mathlib coverage is unchecked.

The preceding cumulative/half-wave alternative was screened solely
to select this continuation: the October31 cumulative-upper-defect
assessment and its citation-stop record already show that Proposition
3.10 and generic monotonicity do not pay the needed upper bound.
That exhausted shortcut is not nominated again. The present mixture
proposal must earn its own source coverage and bounded test; it is
not a mathematical advance or a ready creative mechanism.

## Primary comparison757

The main gap remains L030-L032/C032a actual-Xi all-degree mixed
positivity. This review concerns only a sufficient certificate for
L233's first sign, with complete k from L019. It does not reopen the
Gaussian class excluded by C233c or the generic weighted-autocorrelation
shortcut stopped in ATTEMPTS/2026-09-23-first-associated-autocorrelation-test.md.
The September27 lattice assessment and October31 Cauchy-second-derivative
assessment concern different operations. Their inspected comparison
sections contain no result deciding this dilation representation.
No cross-notebook input was read or used.

**Autocorrelation source.** George Csordas, *Fourier transforms of positive
definite kernels and the Riemann xi-Function*, arXiv:1309.0055v2,
21 February2014, [primary text](https://arxiv.org/html/1309.0055v2),
(3.5), Theorem3.5/(3.7), Remarks3.8(a), Theorem4.5/(4.6)
(printed pp6-8,11). For an L2 function, (3.5) gives positivity of
its unweighted autocorrelation. Theorem3.5 assumes an admissible,
strictly log-concave kernel; its proof separates 0<s<t and s>t.
Theorem4.5 supplies theta admissibility. Remarks3.8 distinguishes
n=0 from the harder weighted n=1. These statements and proof cases
were inspected; earlier shape/tail coverage752-756 is reused.
Admissibility supplies decay, not a spectrum sign. No theorem here
asserts that n=1 is a positive dilation mixture of n=0.

**Scale-mixture source.** Denis Belomestny, Ekaterina Morozova and
Vladimir Panov, *Statistical Inference for Scale Mixture Models via
Mellin Transform Approach*, arXiv:2211.01799v2,22 January2024,
[primary text](https://arxiv.org/html/2211.01799v2), Sections1-2,
(1)-(3), Lemma2.1 and AppendixB.1. The model assumes independent
almost surely positive factors. Its Mellin-Stieltjes product identity
holds where the transforms exist. Division requires a nonzero
base transform. Lemma2.1 handles inversion on either side of real
part1 with the specified integrability strip and endpoint correction;
AppendixB.1 reduces it to bilateral Laplace inversion. Those passages
were read, not the statistical error theorems. The source allows discrete
mixing laws. It does not ensure that an arbitrary quotient represents
a positive law. Our point-normalized functions are not probability
densities; conversion, scale weights and inverse-scale powers must be
justified locally. Complex inversion/nonvanishing is unnecessary for
the proposed finite positive-real moment test. No statistical theorem
or numerical recovery result is imported.

**Moment source.** Konrad Schmudgen, *Ten Lectures on the Moment
Problem*, arXiv:2008.12698v1,28 August2020,
[primary text](https://arxiv.org/html/2008.12698v1), Section3,
(8),(14),(16), Theorems3.1-3.2 and proofs. For a real sequence,
Theorem3.2 equates representation by a positive Radon measure on
[0,infinity), with finite moments of every order, to positivity of
both its unshifted and shifted Hankel matrices. Theorem3.1's proof
identifies the quadratic form with the polynomial-square functional;
Theorem3.2 uses the half-line polynomial decomposition instead.
The relevant necessity is moment-matrix positivity, requiring only
the finitely many moments used. An all-order converse cannot turn
three numbers into a function representation. The support includes
zero; excluding a zero atom and controlling mass at infinity are
additional obligations for any converse. No converse is needed here.

Christian Berg and Ryszard Szwarc, *A determinant characterization of
moment sequences with finitely many mass-points*,
[arXiv:1405.7267v1](https://arxiv.org/html/1405.7267),28 May2014,
Introduction,(1),Theorem1.1,Remark1.2 and Section2's polynomial-square
identity were also inspected. They warn that nonnegative leading
Hankel determinants alone do not imply positive semidefiniteness.
Their finite-support theorem is not an existence theorem for this
mixture and is not imported. The author-hosted PDF timed out;
the accessible arXiv manuscript resolved that lead. An unrelated
arXiv page returned during an access probe was not used. The
Schmudgen2017 book Theorem3.12 search hit was not inspected as a
primary passage; the author's2020 theorem above supplies coverage.
No essential source remains blocked. Other search hits were not
promoted to evidence. Full matching/supporting Mathlib coverage remains
unchecked; absence is not claimed.

## Bounded continuation and stopping threshold

Nominate exactly the test in
[proposal757](2026-11-13-theta-autocorrelation-mellin-minor-test-757.md).
For the proposed complete normalized functions, define their positive-real
Mellin-integral ratios q1,q2,q3 as in that proposal. The single planned
threshold is the shifted moment determinant D=q1*q3-q2^2 against zero.
These are proposed quantities, not computed values or a proved local
inequality. A mathematical turn must first justify the inverse-scale
moment interpretation, positivity/finiteness of the normalizations,
Tonelli and the treatment of every finite b>0, including arbitrary
mass approaching either endpoint. No differentiation of a mixture is
needed. It must then enclose the complete integrals with explicit
errors; finite theta truncations or approximate fitting are insufficient.

A certified D<0 would abandon only this sufficient mixture class.
A certified D>=0 would merely pass this one necessary test; it would
not construct a measure or prove any Fourier sign. An interval crossing
zero leaves the test unresolved. Do not silently continue to an
unreviewed higher-order survey. C233c's Gaussian tail argument cannot
be reused as an exclusion for a building block with its own fast tail.
No new comparison of the actual H and A tails was derived here.

Queries included `scale mixtures Mellin transform characterization
moment sequence scale mixtures density theorem`; `Stieltjes moment
problem Hankel matrices positive semidefinite theorem measure positive
half line`; `"Riemann" "autocorrelation" "scale mixture"`;
`"associated kernel" "scale mixture"`; `"theta" "autocorrelation"
"Mellin" associated kernel`; `"Csordas" "dilations" kernel`;
`"scale mixtures" "Mellin" "characterization" positive definite`;
and exact-title/author followups for the inspected sources. No matching
actual-theta representation theorem was found in this bounded search;
this is not a novelty claim or a survey of all subsequent first-sign
results. The exact sufficient class, not a zero-free region, was assessed.

Outcome757: EXPLORATION. Essential source preparation is complete and
one independently testable necessary-condition target is nominated.
No new lemma, actual-theta inequality, exclusion, spectrum sign or RH
advance was established. Mathematical exploration usage is zero.
The proposed test is ordinary specialization, not a creative central
mechanism. A construction or direct actual-sign mechanism remains
missing; that blocks a justified creative nomination on this route.
