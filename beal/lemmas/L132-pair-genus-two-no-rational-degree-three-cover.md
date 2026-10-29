# L132 — No rational degree-three genus-one cover of the actual pair curve

## Hypotheses

Let B be L110's audited smooth proper geometrically integral genus-two
curve over Q, with its exact model

    W²=f(T)=11(T²−4)Q4(T),
    Q4(T)=7+52T−6T²−64T³−25T⁴.

The full proper curve is intended, including its rational point (2,0)
and infinity chart V²=−275 at h=0. A genus-one target means a smooth
proper geometrically integral curve over Q. Maps are nonconstant
Q-morphisms, without any origin or ramification restriction.

## Conclusion

There is no degree-three Q-morphism from B to any genus-one curve.
The branch divisor of B -> P¹ has no Q-rational effective sub-divisor
of degree three; this violates a necessary condition for such a map,
including special ramification. This closes this cover-degree shortcut
only, with no rank, rational-point or Beal-resolution conclusion.

## Proof

### Imported cover theory and its applicability

Import N. Bruin and K. Doerksen, *The arithmetic of genus two curves
with (4,4)-split Jacobians*, Canad. J. Math. **63** (2011), 992–1024,
DOI [10.4153/CJM-2011-039-3](https://doi.org/10.4153/CJM-2011-039-3),
**Section 2, pp.995–997**, Definition 2.3, the ensuing optimal-cover
and complementary-cover construction, and **Lemma 2.6 with its proof**.
This construction concerns optimal separable degree n covers, not merely
n=4. In the odd-degree situation it supplies a complementary map over
the base field of the same degree, with zero cross push-pull composites.
The general Jacobian/complement theorem is imported, not reproved here.

Suppose phi:B -> D had degree three. L110's P=(2,0) gives phi(P) in
D(Q); choose it as origin, making D elliptic. Characteristic zero
ensures separability. The map is optimal: factoring through an isogeny
of degree greater than one would, by primality of three and degree
multiplicativity, leave a degree-one map from B to a genus-one curve.
A degree-one map of smooth proper curves is an isomorphism, contradicting
their genera. The cited construction therefore supplies the degree-three
complement over Q. L110 even provides a rational Weierstrass point, so
the odd-degree rational-divisor premise presents no obstruction. Lemma
2.6 supplies the cross-composite vanishing required below.

Import R. Bröker, E. W. Howe, K. E. Lauter and P. Stevenhagen,
*Genus-2 curves and Jacobians with a given number of points*,
LMS J. Comput. Math. **18** (2015), 170–197,
DOI [10.1112/S1461157014000461](https://doi.org/10.1112/S1461157014000461),
**Appendix A, pp.193–196**, equation (A.1), Lemma A.1 and especially
**Proposition A.2 and both cases of its proof**. In characteristic
different from two and three, completeness for this complementary pair
gives, over the base field, a genus-two model

    t y²=(x³+3ax+2b)(2dx³+3cx²+1),
    12ac+16bd=1,     (a³+b²)(c³+d²)t != 0.

The proof includes two simple ramification points and a single triple
ramification point; Appendix A.3 retains b=0 or d=0. We use completeness,
not just the explicit maps in Lemma A.1. No Qbar-isomorphism replaces
the asserted Q-isomorphism, and the twist parameter t is retained.

Homogenizing both factors gives rational cubic forms

    G1=X³+3aXZ²+2bZ³,
    G2=2dX³+3cX²Z+Z³.

Their zero divisors are disjoint reduced rational branch divisors of
degree three: the cited smooth model's branch sextic is their product.
For clarity, infinity is retained even when the affine degree drops.
If d=0, the constraint gives 12ac=1, so G2 has a simple zero at infinity
and G1(1,0)=1. If d!=0 neither factor vanishes at infinity. Thus the
degree-five special case still supplies two triples. Smoothness supplies
separability and disjointness; no generic-ramification restriction is
being silently added.

A Q-isomorphism of these genus-two curves induces a PGL2(Q) isomorphism
of their hyperelliptic branch lines. Import the isomorphism representation
in R. Lercier, C. Ritzenthaler and J. Sijsling, *Fast computation of
isomorphisms of hyperelliptic curves and explicit Galois descent*,
The Open Book Series **1** (2013), 463–486,
DOI [10.2140/obs.2013.1.463](https://doi.org/10.2140/obs.2013.1.463),
**Sections 2A–2B, pp.465–468, and Section 2E1, p.474**. Transport of
G1,G2 by the rational invertible linear substitution factors B's binary
branch form into rational cubics, up to nonzero rational scalar. Hence
phi necessarily gives a rational branch triple. Only necessity is used.

### Exact irreducibility certificate

The whole sextic has ascending integer coefficients

    f=[−308,−2288,341,3388,1034,−704,−275].

At the prime 19 its degree-preserving reductions are

    fbar=[15,11,18,6,8,18,10],
    Qbar=[7,14,13,12,13].

Both leading coefficients are nonzero. The replay supplies the full
squarefreeness identity in F19[T]

    u fbar + v fbar' = 1,
    u=[17,16,4,2,1],     v=[8,11,7,18,5,3],

with all lists in ascending order. Thus the entire sextic, not just its
quartic factor, has squarefree reduction.

Every monic linear T+a (19 choices) and every monic quadratic T²+bT+a
(361 choices), 0<=a,b<19, was tested. All 380 exact remainders of Qbar
are nonzero. Full divisor/remainder rows are at
`primes[6].divisor_trials` in
`scripts/pair-genus-two/degree-three-branch-certificate.json`.
This exhausts the needed finite domain: a reducible degree-four
polynomial over a field has an irreducible factor of degree at most
two, since otherwise two factors already have total degree at least
six. Thus Qbar is irreducible over F19.

Q4 is primitive over Z (7 and 52 are coprime), and −25 is nonzero modulo
19. Gauss's lemma and the degree-preserving irreducibility-by-reduction
criterion imply irreducibility over Q: a nonconstant rational
factorization would give a primitive integer factorization with factor
degrees retained modulo 19, contrary to the certified irreducibility.

### Exhaustion of rational branch triples, including infinity

Set F(X,Z)=Z⁶f(X/Z). Its distinct rational irreducible factor degrees
are 1,1,4: X−2Z, X+2Z and the homogenization of Q4. The scalar 11 does
not affect zeros. F(1,0)=−275!=0, so infinity is not a branch point.
L110's two geometric points over infinity are unramified, and do not
add branch points to this list.

A rational reduced sub-divisor is Galois stable, hence a union of the
irreducible branch orbits. Their sizes 1,1,4 allow only degrees
0,1,2,4,5,6, never three. Equivalently, a homogeneous cubic factor of F
cannot contain Z; dehomogenizing it would give a degree-three rational
factor of a polynomial with irreducible factor degrees 1,1,4, contrary
to unique factorization. This contradicts the necessary condition above
and excludes every asserted Q-map, without a sufficient-cover criterion.

### Reproduction, accounting and limitations

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-25-pair-genus-two-degree-three-subcover.md`.
General cover theory is imported; its exact-model obstruction is a local
specialization, with no general novelty or certified-originality claim.

Producer: `python3 scripts/pair-genus-two/degree_three_branch.py`.
It refuses to overwrite an existing ledger, preserving cumulative caps.
It visited 3,5,7,11,13,17,19 and stopped at the first certified prime.
Replay: `python3 scripts/pair-genus-two/verify_degree_three_branch.py`.
It imports accounting only, and uses Horner residues independently of
producer polynomial division. It checks all complete selected-prime
rows, the input expansion, derivative and squarefreeness identity.
All 1175 checks pass, with no failures, in
`scripts/pair-genus-two/degree-three-branch-verification.json`.
Earlier unsuccessful primes are unnecessary to the conclusion and are
not replayed; their partial trials remain in the producer certificate.

Whole-step charges, including preparation, producer and replay, are in
`scripts/pair-genus-two/degree-three-branch-ledger.json`: 8 prime visits
against cap 25; 773 divisor trials against 250000; 14543 work units
against 1000000; maximum observed polynomial degree 10 against 12;
integer input/output bits 12 against 4096. There is no cap stop.
Polynomial operations, candidate/scalar checks and processed rows are
charged; library-internal elementary operations are not claimed counted.
A certificate preview is not the verification: the independent replay
recomputes the complete relevant evidence.

This obstruction is over Q and does not exclude geometric covers or
higher-degree covers. It gives no quotient upper rank or point control.
All marked lifting, degree-nine recovery, L095 integer-system and
other-signature gaps remain independent unresolved obligations.

## Mathlib

The full matching result and supporting cover/descent and finite-field
theorems have not been checked in Mathlib. No absence claim or Lean
verification is made. This is an informal specialization with complete
exact certificates and an independently implemented arithmetic replay.
