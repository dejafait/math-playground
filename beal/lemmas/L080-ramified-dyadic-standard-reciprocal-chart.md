# L080 — Standard reciprocal dyadic chart and the coordinate-coverage gap

## Hypotheses

Use L033's E0: y²+y=x³−x²−10x−20 and L069's coordinates
X=4x, Y=8y+4, giving Y²=g(X), where

    g(X)=X³−4X²−160X−1264.

Use L078's entire fields H=Q2(pi), pi^11=2, and J=H[rho], its
maximal rings, fixed theta, and unit-square labels. Thus
v_H(2)=11, v_J(pi)=3, v_J(theta)=44, and arithmetic modulo 8 O_J
has error valuation at least 99. The strict unit-square threshold
in J is 66. Use L079's certified list of 2048 realized labels.
The independent audit below includes L078/L079.
No global-unit independence, class value, rank bound or integer
solution is assumed.

## Conclusion

The standard reciprocal chart z=1/X in pi O_H has a complete
terminal/rejected-disk certificate at depth eight. Among its 128 disks,
120 contain no curve point and eight have exact realizations and a
constant Kummer class on their feasible subsets. Their distinct labels
are exactly

    0, 1073741824, 4294967296, 5368709120,

each appearing on two realized disks. All four match L079's fixed list.
Infinity has identity class; there is no finite Weierstrass exception.
The full evidence is in `scripts/ramified-dyadic-image/reciprocal-certificate.json`.

This completes this standard reciprocal chart, not the full requested
two-chart certificate. L079 covered original x in O_H. The present chart
covers v_H(x)<−22, because X=4x. The intervening annuli

    −22 <= v_H(x) < 0

still require terminal/rejected-disk evidence. L079's abstract full-image
equality remains valid independently of this certificate gap. No global
dimension improvement or integer exclusion follows.

## Proof

### Reciprocal equation and exact square feasibility

For nonzero z=1/X, multiplying the cubic equation by z^4 gives

    (Y*z²)² = z*R(z),
    R(z)=1−4z−160z²−1264z³.

The monic-cubic Kummer class [X−theta] equals [z(1−theta*z)],
since their ratio is z^(-2), a square. This is the reciprocal evaluation
in Bruin–Stoll, *Two-cover descent on hyperelliptic curves*, Math. Comp.
78 (2009), 2347–2370,
[DOI](https://doi.org/10.1090/S0025-5718-09-02255-8),
[14 March 2008 author manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/twocoverdescent.pdf),
Section 4, LocalImage and SquareClasses, pp.8–10. The odd-degree map has
no scalar quotient (Remark 2.1). The general algorithm and square
neighborhood theorem are imported from the ready assessment, not reproved.
The coordinate and disk specializations below certify this instance.

For z in pi O_H, put k=v_H(z)>=1, treating z=0 separately. Since
v_H(4)=22, v_H(160)=55 and v_H(1264)=44,

    v_H(R(z)−1) >= min(22+k,55+2k,44+3k) >= 23 > 22.

Consequently R(z) is a unit square in H. Precisely, the imported strict
Hensel inequality for T²−R(z) at 1 is v_H(1−R(z))>2v_H(2).
This is the square-neighborhood fact used in Bruin–Stoll Lemma 4.4,
pp.7–8, already specialized in L078. Thus z*R(z) is square exactly when
z is square. For every actual square z=a²!=0 in pi O_H, an exact point is

    X=a^(-2),     Y=a^(-3)*sqrt(R(a²)).

Here sqrt(R(a²)) is the Hensel root at 1, specified by its convergent
limit, rather than a finite approximation. Substitution verifies the
entire cubic equation. The inverse coordinate changes give an actual
E0(H) point. Its Kummer class is [1−theta*a²], since a^(-2) is square.

### Every terminal or rejected disk

The residue field of H is F2 and O_H=Z2[pi]. Therefore the 128 distinct
centers

    z0=sum_(i=1)^7 b_i*pi^i,    b_i in {0,1},

give all disks z0+pi^8 O_H in pi O_H. To identify those containing a
square, any root a must lie in pi O_H. Write a=a0+d, with
a0=b1*pi+b2*pi²+b3*pi³ and d in pi^4 O_H. Then

    a²−a0²=2*a0*d+d² belongs to pi^8 O_H,

because the two summands have valuations at least 16 and 8. In a0²,
the cross terms have valuation at least 11+1+2=14. Its residue is
therefore b1*pi²+b2*pi⁴+b3*pi⁶. The eight choices give distinct
residues, precisely those whose odd-position digits 1,3,5,7 vanish.
Every other disk is rejected: no square and hence no curve point can
lie there. This proves necessity exhaustively, without a precision
sample standing for a square test.

Conversely use the exact a0 above for each nonzero allowed mask. For
the zero mask use a=pi⁴, so z=pi^8!=0 lies in that disk. Each choice
is nonzero and gives the exact point just constructed. Thus all eight
remaining disks are realized. Some z in such a disk can be nonsquares;
the terminal certificate asserts realization and class constancy on
the feasible subset, not that every z in that disk is a point.

For any two feasible z,z' in one depth-eight disk, 1−theta*z and
1−theta*z' are units of J, and

    v_J(theta*(z−z')) >= 44+3*8=68 > 66.

Their ratio is in 1+rho^68 O_J, hence a square by L078's strict Hensel
test. The square factors z,z' can be removed from their respective
Kummer evaluations. This proves constancy on the entire feasible
subset. The modulus error 99 also exceeds 66, so the exact ring
arithmetic determines the required classes. No division loses precision
in the computed unit 1−theta*a².

### Exceptional values and full evidence replay

At z=0 the reciprocal point is infinity O, whose Kummer class is
identity. The zero disk also contains the nonzero realization pi^8,
whose unit 1−theta*pi^8 differs from 1 by valuation 68, confirming the
same class. There are no further reciprocal exceptional values:
R(z) is a unit, while z!=0 is invertible in H. Globally on this curve
there is no finite H-rational Weierstrass point, because L078 identifies
the entire cubic algebra with a degree-three field. In particular no
finite root of g is being discarded. The denominator changes 4 and 8
are nonzero field scalars, not claimed integral units.

Run

    python3 scripts/ramified-dyadic-image/check_reciprocal_disks.py
    python3 scripts/ramified-dyadic-image/verify_reciprocal_certificate.py

The construction stores all 128 disks, all 120 odd-digit obstructions,
the eight exact root formulas and their squared residues, Hensel bounds,
full L078 normal forms, affine representative matches, complete
collisions and exceptions. Its 13 checks pass with no failures. The
complete histogram is {0:2,1073741824:2,4294967296:2,5368709120:2}.
The replay compares every disk against all eight possible square-root
residues; checks every nonzero realization and R square bound; rebuilds
each fixed class representative and its full square-factor/residual
identity; and checks all labels against L079 and the complete histogram.
Its 8 checks pass with no failures, recorded in
`scripts/ramified-dyadic-image/reciprocal-verification.json`. All stored
records are replayed, not merely previewed. This verifies the certificate
within L078's arithmetic; it is not an independent audit of that input.

Finally v_H(X)=22+v_H(x), so z in pi O_H is equivalent to
v_H(x)<−22. L079's original integral-x chart and this chart leave exactly
the stated middle annuli without the requested disk evidence. Neither
the four-class reciprocal computation nor L079's abstract cardinality
argument is substituted for that missing work. This is local
specialization of known methods, with no claim of progress beyond the
sources checked and no new independent global direction.

### Independent critical audit — 2026-10-16

The independent audit confirms this chart, retaining its historical
coverage qualification. The exact equation is (Y*z²)²=z*R(z).
For every nonzero z in pi O_H, R(z)−1 has H-valuation at least 23>22,
so feasibility is precisely that z be square. Modulo pi^8 the possible
squares are exactly the eight even-digit residues: the omitted cross
terms have valuation at least fourteen and changing the root by pi^4
changes its square by valuation at least eight. Every permitted residue
has its displayed nonzero realization; arbitrary points in that residue
disk are not asserted feasible.

The independent verifier of L078 recomputes all eight possible square
residues and compares each of the 128 disks with them. It verifies all
120 rejection witnesses, all eight nonzero realizations, their R square
bounds, class reconstructions, affine representative matches and complete
four-label histogram. The unit variation has J-valuation at least 68>66;
infinity and the nonzero realization in its disk both have label zero.
No finite Weierstrass exception exists in the entire irreducible cubic.
All these checks pass in the separate complete audit certificate.

The coordinate conversion is essential: z=1/(4x) in pi O_H means
v_H(x)<−22. This audit does not erase the earlier gap or reinterpret
x as X. L081's separately verified parameter branch supplies the missing
annuli. No correction of this chart's decisions or labels is required.

## Mathlib

Full matching standard reciprocal-chart certificate over this ramified
field and its explicit fixed labels: **not checked**. Supporting local
field, Hensel, Kummer-map and square-class declarations: **not checked**.
Unknown availability is not evidence of absence.
