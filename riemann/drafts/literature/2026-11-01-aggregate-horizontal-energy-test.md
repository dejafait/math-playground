# Aggregate horizontal-multiplicity energy — bounded test coverage

TARGET: Attempt aggregate domination of equal-real-part multiplicity by the full sinc-squared energy, using two unequal-depth conjugate packets as the bounded falsification test.
CHECKED: 2026-11-01
DECISION: EXPLORE
SEARCH_EVIDENCE: The finite-frequency source review searched horizontal multiplicity with kernel square, Lamzouri, energy and equal real parts, and compared the local charged-pair assessment and L613 stop; no matching domination theorem or recorded counterexample was identified. Search failure does not establish novelty.
SOURCE_EVIDENCE: Lamzouri arXiv:2609.02882v1 Proposition 2.1/(2.4) and its proof through (2.21); BGST arXiv:2501.14545v3 Theorem 3/(1.5), (4.1), Lemmas 3–5; GLSS arXiv:2503.15449v4 (6.2) and Theorems 1–2. Full comparison and inspected ranges are in 2026-11-01-finite-frequency-horizontal-multiplicity.md.
COMPARISON: The known norm identity and simple-real deficit inequality control the complete algebraic energy without termwise signs. They do not state domination of the equal-real-part second moment. BGST supplies such count extraction with a thin box; GLSS supplies a conditional PCC route. The proposed finite inequality is a stronger aggregate claim requiring an independent test.
GAP: Prove or refute M(Z)<=E(Z) under finite conjugation symmetry, beginning with the two-packet family specified below. Even success on that family leaves the general inequality, actual-zeta weight removal and quantitative charge conversion unresolved.
REASON: An aggregate norm/count comparison is a distinct mechanism from signed-term deletion, an infinite-frequency limit or L613's fixed contrast. Existing source coverage suffices for this finite test; no source is assumed to prove the missing inequality and no mathematical result was derived during preparation.
SCOPE: Finite complete multiset energy only, fixed sinc kernel and stated two-packet falsification family; no thin box, minimal spacing, test variation, support enlargement, Xi realization, zero-free theorem, or actual-zeta main-term assumption. Full and supporting Mathlib coverage is not checked.

## Exact proposed claim and source specialization

Let Z be a nonempty finite multiset in C invariant under conjugation,
with conjugates having equal multiplicities. All ordered pair sums below
retain the product of multiplicities. Define

    K(z)=sin(pi z)/(pi z), K(0)=1,
    E(Z)=sum_(z,s in Z) K(z-s)^2,
    M(Z)=sum_(z,s in Z; Re z=Re s) 1.

The proposed inequality M(Z)<=E(Z) is UNPROVED. No termwise sign
condition is imposed. Algebraic squares must not be replaced by modulus
squares. Equal real parts in these coordinates correspond to equal
zeta ordinates after the usual rotation; this is motivation only, not
an application to actual zeros.

The reference input is Youness Lamzouri, *A new proof that more than
2/3 of the zeros of the Riemann zeta function are simple and on the
critical line*, [arXiv:2609.02882v1](https://arxiv.org/html/2609.02882v1),
Proposition 2.1/(2.4), norm identity (2.10), and proof through (2.21).
Choose eta=1 on [-1/2,1/2] and zero elsewhere, taking the proposition's
lambda=1. This is real-even L2, has support contained in (-1,1) and
int eta^2=1. Its displayed Fourier convention (2.3) gives the fixed
sinc kernel above; BGST v3 (4.1) records its squared Fejer kernel.
Thus the known proposition applies to this energy, including repeated
real points and conjugate pairs. It gives E(Z)>=2|Z|-s_real(Z),
not the proposed M(Z) comparison. Only this direct specialization is
authorized as a known input; reproving the norm identity is unnecessary.

BGST, *Pair Correlation of Zeros of the Riemann Zeta Function I*,
[arXiv:2501.14545v3](https://arxiv.org/html/2501.14545v3),
Theorem 3/(1.5) explains the potential count use: a sufficiently small
horizontal second moment gives simple-critical proportions. Its
Lemmas 4–5 require the thin box, which is not an assumption of this
finite test. GLSS,
[arXiv:2503.15449v4](https://arxiv.org/html/2503.15449v4),
Section 6/(6.2) retains a nonzero-gap count integral; its Theorems 1–2
require PCC or HMH. None is imported to fill the proposed inequality.

## Bounded falsification test and stopping rule

Use the two packets

    {-a/2+iu, -a/2-iu}, {a/2+iv, a/2-iv},
    0<a<=4, 0<=u,v<=2,

with each label of the first packet repeated m times and each label
of the second repeated n times, m,n in {1,2}. At u=0 or v=0 the
two coincident labels remain, with their combined multiplicity. Permit
arbitrarily small positive a; do not assume distinct-real-part spacing.
The family deliberately permits unequal depths. No expansion, sign,
optimization or numerical evaluation of E-M has been carried out here.

One rigorous example E(Z)<M(Z) abandons this universal domination claim;
record its full multiplicities and exact or certified strict inequality.
Such a counterexample would obstruct this mechanism, not RH or the
known simple-critical result. A proof on this complete bounded family
is only an intermediate result: it can motivate general aggregate
analysis, but it does not prove domination for all Z. A numerical grid
with no failure is not a proof. If the step supplies neither a proof
nor a rigorous negative, preserve partial reasoning and reassess rather
than repeating the same search unchanged.

This is the preparatory bounded test for a new norm/count mechanism,
not a claim of creative success. If domination survives and can later
be proved generally, it could provide horizontal-moment control from
the already evaluated fixed energy. That still would not prove a
microscopic o(T) charged union, control all exceptional centers, or
establish the remaining initial/all-degree Xi signs. Those independent
gaps must remain explicit. The sharp count threshold C<2 comes from
the inspected BGST theorem; no achieved constant is reported.

## Duplicate and failure comparison

L612 proves only compatibility with its two count conditions; L613
compares two finite configurations against a fixed-test error. Neither
tests M(Z)<=E(Z) for one arbitrary conjugation-invariant set. The prior
charged-pair review already covered Lamzouri's simple-real inequality
and fixed-test application; that coverage is reused, not called new.
The present review adds the explicit horizontal-moment distinction.
No inaccessible stability statement, reciprocal cutoff route, or
cross-notebook result is needed. The full-complex signed remainder is
not discarded. Bounded search found no adequate match, but possible
coverage outside the inspected sources remains unresolved.

This is a newly prepared continuation. Its separate next-turn source
approval must precede mathematics; preparation does not count as having
proved, tested, or independently approved the missing claim.
