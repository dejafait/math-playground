# L151 — Actual quartic-pair field and its complete dyadic conics

## Hypotheses

Use L138's odd model and actual root identification, L135's maximal
order and index [O_K:Z[alpha]]=937500, and L145's exact dyadic field and
basis maps. Thus

    K=Q(alpha), A(alpha)=alpha^4+64alpha^3+150alpha^2−32500alpha−109375=0,
    F=K tensor Q_2=Q_2(pi),
    E(pi)=pi^4−64pi^3+1272pi^2−8442pi+5850=0,
    O_F=Z_2[pi], v_F(pi)=1, v_F(2)=4.

The exact generator and odd-model root maps are

    alpha=(6731−9596pi+877pi^2−18pi^3)/71,
    theta=(3705900−3441768pi+316932pi^2−6512pi^3)/71.

Use L147/L149's full Q×K products, without rational-scalar quotient,
with masks 132102 and 3109. Their quartic components in the alpha basis
are, respectively,

    b_eta=41236+(356216/25)alpha+(397568/625)alpha^2+(4612/625)alpha^3,
    b_nu=90688+(99088/5)alpha−(1403152/625)alpha^2−(33968/625)alpha^3.

For either polynomial b let B(P) be its degree-at-most-three remainder
after substituting the displayed alpha(P) and reducing modulo E(P).
Let Theta(P) be the displayed polynomial for theta. Retain L150's conic
convention

    d_j u^2−d_i v^2+(theta_j−theta_i)w^2=0.

The rational component is irrelevant to a quartic/quartic pair, but is
retained and authenticated in the certificates. No goodness, global
conic point, pairing value or rank improvement is assumed.

## Conclusion

The ordered pairs of distinct quartic branches form one orbit with root
field M of degree twelve over Q. There is exactly one place of M above
two. Its completion is the degree-three Eisenstein extension L/F below,
with absolute ramification twelve and residue field F_2.

For both fixed classes the quartic/quartic conic has an L-point. This
exhausts the dyadic places of the remaining quartic-pair orbit, including
conjugate and reversed pairs. Together with L150, every dyadic
branch-pair conic for these classes is soluble.

This is local existence only. The remaining odd-place coverage and
outside-support proof for M, global solutions, compatible choices and
whole good-element condition remain unfinished. The result does not
decide either class good or not good, its rational Kummer status, the
mutual pairing, point control or the Beal conjecture. Arithmetic replay
is provided; the separate conceptual audit below accepts these claims.

## Proof

### Exact global root-pair field

Synthetic division gives

    A(X)=(X−alpha)h(X),
    h(X)=X^3+(alpha+64)X^2+(alpha^2+64alpha+150)X
         +alpha^3+64alpha^2+150alpha−32500.

At the maximal-order prime with alpha=0 modulo 7 the reduced cubic is
X^3+X^2+3X+1. Its values at 0,1,2,3,4,5,6 are
1,6,5,4,2,5,5. This cubic is irreducible. The place exists with residue
field F_7 because 7 does not divide 937500, A(0)=0 modulo 7, and
A'(0)=1 modulo 7. The monic h has coefficients integral at this place.
A monic factorization over K would have integral coefficients there
(its roots are integral); reduction would retain both positive degrees,
contradicting irreducibility. Thus h is irreducible over K.

Consequently M=K[X]/h is a field of degree 3 over K, degree 12 over Q,
with X representing the second distinct alpha root. This exhausts all
ordered distinct quartic pairs: there are four choices for the first
root and three for the second, and this one orbit already has size
twelve. Transport by the invertible root map in L138 gives the same
claim for the actual theta branches. No generic Galois-group assumption
is used.

### The entire remaining dyadic completion

Put pi_second=pi(1+s). Dividing E(pi+Z) by Z, using E(pi)=0 and then
substituting Z=pi*s, gives

    H(s)=s^3+u2*s^2+u1*s+u0=0,
    u0=E'(pi)/pi^3,
    u1=6−192/pi+1272/pi^2,
    u2=4−64/pi.

In F the respective valuations of u0,u1,u2 are 1,4,8. They follow by
substitution and the weighted valuation formula
v_F(sum c_j*pi^j)=min_j(4v_2(c_j)+j); the minimum is unique because the
four weights are distinct modulo four. Thus H is Eisenstein over F.
In particular L=F[s]/H is a field of degree three, s is its uniformizer,
O_L=O_F[s], v_L(pi)=3 and v_L(2)=12. These are the standard complete-DVR
consequences of an Eisenstein polynomial. Its basis pi^j*s^i, with
0<=j<=3 and 0<=i<=2, has the twelve distinct valuation weights 3j+i.

Exact substitution gives E(pi_second)=0 and
v_L(pi_second−pi)=v_L(pi*s)=4, so these are distinct branches. L145's
inverse generator maps transport them to distinct alpha roots and hence
to an embedding of the actual pair field M. The resulting completion
has degree 4*3=12 over Q_2, equal to [M:Q]. The sum of local degrees is
[M:Q], so there is no additional dyadic place. This also proves that the
residual cubic has no root in F; a second branch cannot be tested inside
F itself. The saved complete 25-disk root exclusion is an independent
consistency check, not a substitute for this Eisenstein argument.

### Complete square criterion in L

Apply the Local Square Theorem and strict Hensel lemma in the actual
field L: e=v_L(2)=12, so every unit in 1+s^25 O_L is a square. This is
the same named input used in L145/L150: Pete L. Clark, *Algebraic Number
Theory II: Valuations, Local Fields and Adeles*, inspected 161-page
author-hosted version, Proposition 2.20 p.72 and Theorem 2.24 with proof
p.73, [primary notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf).
The prior SPECIALIZE assessment covers this finite conic arithmetic;
no new general square criterion or pairing formula is asserted.

There are exactly 4096 unit residues modulo s^13, namely

    R(t)=1+sum_(k=0)^11 bit_k(t)*s^(k+1), 0<=t<4096.

For integral units x,y with v_L(x−y)>=13,

    v_L(x^2−y^2)>=min(2*13,12+13)=25.

Thus these 4096 residues exhaust every possible unit-square residue
modulo s^25. Conversely a unit with the same residue as R(t)^2 is a
square by the Local Square Theorem, or strict Hensel at R(t).

The full square table is in the certificate. In the flattened basis
pi^j*s^i, congruence modulo s^25 is coefficientwise congruence modulo
eight for the weight-zero coefficient and modulo four for the other
eleven coefficients: 12v_2(c)+3j+i>=25 gives exactly these thresholds.
The certificate encodes those 25 bits in flattened coordinate order.
All 4096 unit-root residues give precisely 2048 distinct fingerprints.
The independent replay reconstructs them using the maximal-order basis
and a modular multiplication tensor, rather than the producer's exact
pi-basis squaring. No partial image or preview is used as a square test.

For arbitrary nonzero h, first require n=v_L(h) even, then test the unit
h*s^(−n) against this complete image. A successful witness r has
v_L(r^2−h)>2v_L(2r). When n is negative this statement is applied after
scaling r and h to a unit root and unit right side; all Hensel inputs are
then integral. Odd valuation or a missing fingerprint certifies only
that particular element nonsquare, not conic insolubility.

### The two conics

In L set

    b_i=B(pi), b_j=B(pi_second),
    theta_i=Theta(pi), theta_j=Theta(pi_second),
    a=b_i*b_j, c=(theta_i−theta_j)*b_j.

These quaternion entries differ from b_i/b_j and
(theta_i−theta_j)/b_j by the square factor b_j^2. Equivalently, the
invertible substitution U=b_j*u, V=v gives the exact conic
U^2−a V^2=c w^2. Neither b_j nor the root difference vanishes.
For k_a=floor(v_L(a)/2), k_c=floor(v_L(c)/2), put

    a0=a*s^(−2k_a), c0=c*s^(−2k_c).

The change U=s^k_c*U0, V=s^(k_c−k_a)*V0 gives
U0^2−a0*V0^2=c0*w^2. These are explicit invertible changes over L.
The producer and replay reconstruct the full products from all selected
columns and check every coordinate of these identities.

For eta_class, a0 has valuation zero and fingerprint 23318615.
The exact proposal R(2041) satisfies

    v_L(R(2041)^2−a0)=29>24=2v_L(2R(2041)).

Hensel supplies a square root of a0 in L, giving a projective point with
w=0. Since this is a nondegenerate conic over the infinite field L, it
also has an affine point with w=1: projection from a point parametrizes
infinitely many points, while w=0 meets the conic in at most two points.

For nu use V0=s^(-1)(1+s), the 68th candidate in the saved fixed order,
and put h=a0*V0^2+c0. Its valuation is −2 and normalized fingerprint is
5342209. The proposal r=s^(-1)R(1168) satisfies

    v_L(r^2−h)=23>22=2v_L(2r).

Equivalently v_L((s*r)^2−s^2*h)=25>24, with integral unit root and
right side. Hensel supplies U0 with U0^2=h and hence an affine conic
point. Every coefficient, full residual vector, valuation and root
proposal is checked exactly in the replay. The failed preceding
candidates are nonsquares for those V0 only. They were never used as
negative conic evidence.

These two successes prove solubility over the single dyadic completion
of M. All global conjugate pairs are embeddings of this same conic
over M; all their dyadic specializations are isomorphic to the one just
tested because M has one dyadic place. Reversing the pair also exchanges
u,v and negates the equation. This proves the conclusion without
assuming a generic quartic Galois group, global solubility, or goodness.

### Certificates, bounds and remaining boundary

Run `python3 scripts/pair-genus-two/shukla_quartic_pair_conics.py`, then
`python3 scripts/pair-genus-two/verify_shukla_quartic_pair_conics.py`.
Full evidence is in
`scripts/pair-genus-two/shukla-quartic-pair-conics-certificate.json`;
the independent replay writes
`scripts/pair-genus-two/shukla-quartic-pair-conics-verification.json`.
Its 52357 direct and 4010 helper checks pass with no failures.
The exact global specialization exhausts seven residues; the additional
root-tree consistency check uses 25/8192 disks and depth 5/32.
The unit-square table exhausts 4096/4096 unit-root residues at the
required precision 25. The eta square succeeds directly; nu uses 68/160
conic candidates. Producer/replay rational sizes are 1673/1440 bits
against 8192. No exhaustion is interpreted as an obstruction.

The proof imports standard factorization/local-field/Hensel tools and
specializes them to the fixed instance; it claims no new general
mathematics beyond the sources checked. Untested odd completions,
outside-support coverage for M, global field points and compatible
solutions remain necessary before either class is certified good.

### Separate conceptual audit — 2026-10-29

The approved conceptual audit accepts the degree-twelve field and
complete dyadic conclusions. Its rerun of the full independent replay
passes 52357 direct and 4010 helper checks, with no failures. It checks
the complete global deflation, all seven specialization residues, the
relative cubic, the exact second root, every one of the 4096 unit-root
rows, all 2048 image witnesses and the complete successful residuals.
Required square precision is 25 and actual precision is 25. The two
conics require zero and 68 new candidates within the saved cap of 160;
no candidate search was enlarged or regenerated by this audit.

At seven, A'(0)=1 modulo seven and seven does not divide the order
index, so the degree-one place used in the monic cubic specialization
exists. Integrality of monic factors in its DVR makes the irreducible
reduction argument valid. The 4*3 embeddings of M are exactly all
ordered distinct quartic pairs. Under L145's inverse generator maps,
the two distinct E-roots in the tower give the two distinct A-roots;
the local image contains F and s=pi_second/pi−1, hence is all of L.
The relative Eisenstein valuations 1,4,8 imply local degree twelve.
Equality with the global degree proves that this is the sole dyadic
place, rather than merely a tested embedding of one unknown factor.

The twelve basis weights 3j+i are distinct modulo twelve. Thus the
coefficientwise fingerprint modulus really represents congruence
modulo s^25. All unit residues modulo s^13 are enumerated; squaring
is constant on those disks modulo s^25. The strict square witnesses
give 29>24 for eta_class and, after multiplying the nu square equation
by s^2, 25>24 with integral unit input. This checks the negative
valuation scaling explicitly. The invertible changes U=b_j*u and
the square normalizations preserve the actual conic and its point
existence. The point at infinity used for eta_class is sufficient for
affine existence by the smooth infinite-field argument, not an
assertion that its saved approximate square root is an affine point.

Every M-embedding into an algebraic closure of Q_2 corresponds to this
one place; transporting a point along an isomorphism of completions
preserves its equation. Reversal also preserves solubility by exchanging
variables. Neither observation assumes that reversal of an arbitrarily
chosen point must equal its Galois conjugate. Compatible global choices
are a separate existential interface, treated in L152. This reference
records the later assembly, not an input to the present local proof.

## Mathlib

Full matching coverage for this root-pair field, its dyadic conics or
Shukla's good-element condition has not been checked. The cited complete
DVR, Eisenstein and Hensel inputs are mathematical imports; their
presence or absence as a matching Mathlib theorem is not asserted.
