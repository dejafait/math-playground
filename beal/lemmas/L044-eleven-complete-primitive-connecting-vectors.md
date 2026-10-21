# L044 — Complete primitive whole-fiber connecting vectors at eleven

## Hypotheses

Use L033's curve, normalized dual connecting map and L034's complete modular map:

    E0: y^2+y=x^3-x^2-10x-20,
    f=(x-4)y-4x^2+30x-55,
    j=(a(x)+b(x)y)/(x-16)^11,
    F(x,s)=h(x)^3+J(x)s-(x-16)^11 s^2,  J=2a-b.

The polynomials are exactly L034's audited source coefficients. Use L041's
entire algebra A11=Q11 × Q11 × L, L=Q11[r]/(r^10+55), with places ordered
as there and normalized orders (1,1,10) relative to v11. Consider all
isomorphisms B_s -> A11 of the **entire** modular fiber at a scalar
s in Q11 minus {0,1728}. Require common nonzero a0,b0,c0 in Z11 with
minimum coordinate valuation zero and

    a0^3+b0^4=c0^11,  s=1728 a0^3/c0^11.

The vector is (ord_w(delta(P_w)) mod 5)_w, including good-divisor evaluation.
Retain every rational-factor permutation and ramified embedding. There is
no positivity, global class basis, GRH, other-place restriction or precision
cutoff.

## Conclusion

The complete primitive whole-fiber vector image is exactly

    {(0,2,0), (2,0,0)} in (Z/5Z)^3.

Every compatible primitive scalar is integral with residue 4 or 10 modulo
eleven. In particular s and 1728-s are units. Both vectors are realized by
L042's exact whole fiber at its one shared primitive-compatible scalar.
The two integral branch disks contribute no vectors: in the primitive
domain the disk at zero has v11(s)>=3 and the disk at 1728 has
v11(s-1728)>=4, and neither admits even a rational fiber point.

Thus 23 of L041's 25 inherited norm candidates are excluded from this
restricted image, compared with 125 unrestricted vectors. For a global
primitive solution in L033's 54a1 branch this also forces 11 not dividing
A B C. This is a local necessary restriction, **not** global branch
emptiness, an integer solution, or a Beal resolution. The independent
critical audit below confirms this local result without a correction.

## Proof

### Source imports and specialization

The complete modular map and elimination identity are imported through
L034 from Freitas–Naskręcki–Stoll, *The generalized Fermat equation with
exponents 2, 3, n*, Compositio Math. **156** (2020), 77–113,
[final author manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
internally June 10, 2019, Section 7.2, printed pp.25–27, equation (7.4).
L033 imports the normalized connecting-map/good-divisor interface from
Schaefer–Stoll, *How to do a p-descent on an elliptic curve*, Trans. AMS
**356** (2004), 1209–1231,
[June 13, 2001 long manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf),
Sections 5 and 9. L041 imports the elementary Hensel inputs and proves
the simultaneous scalar domain; L042 supplies exact whole-fiber
realizations and every valuation in the generic integral slice; L043
excludes all primitive negative scalars.

These source assessments are reused unchanged. No general theorem is
reproved. The remaining specialization is a uniform coefficient
obstruction on two primitive branch disks, established below by the
valuation rule that a zero sum cannot have a unique term of lowest
valuation. It needs neither an extra Newton-polygon citation nor a
finite-precision root-count assumption. This is REPRODUCTION of assessed
methods, with no claim of novelty beyond the sources checked.

Write v for the extension of v11 with v(11)=1. Zero coefficients have
valuation infinity in the tables below.

### A coefficient criterion, proved directly

Suppose Q(Z)=sum_(i=0)^n c_i Z^i is monic, v(c_0)=n h,
and v(c_i)>=(n-i)h for all i, with h>0. Its roots are nonzero.
If a root z had e=v(z)<h, then for i<n

    v(c_i z^i)-v(z^n)>=(n-i)(h-e)>0.

The leading term would be uniquely lowest, impossible. If e>h, then
for every i>0

    v(c_i z^i)-v(c_0)>=i(e-h)>0,

and the constant term would be uniquely lowest, again impossible.
Therefore every algebraic root has valuation h. In particular, if h is
not an integer, Q has no root in Q11. Internal coefficients lying on the
bound do not affect these strict comparisons. This criterion is proved
here solely for the explicit coefficient specialization that follows.

### Primitive disk at zero

By L041, integral primitive scalars satisfy v(s) in 3 N0 and
v(1728-s) in 4 N0. If s is zero modulo eleven, then v(s)>=3.
Put V=(x+105)/121, so x=16+121(V-1), and define integral polynomials

    H(V)=h(-105+121V)/11^8
        =352-1144V+1232V^2-440V^3+V^4,
    Jstar(V)=J(-105+121V)/11^22,
    Dstar(V)=(V-1)^11.

Exact substitution gives the **monic** degree-twelve polynomial

    Q_s(V)=F(-105+121V,s)/11^24
          =H(V)^3+(s/121)Jstar(V)-(s^2/121)Dstar(V).

The complete coefficient valuation table is:

| i | v([V^i]H^3) | v([V^i]Jstar) | v([V^i]Dstar) |
| --- | --- | --- | --- |
| 0 | 3 | 3 | 0 |
| 1 | 3 | 2 | 1 |
| 2 | 3 | 3 | 1 |
| 3 | 3 | 2 | 1 |
| 4 | 2 | 2 | 1 |
| 5 | 2 | 3 | 1 |
| 6 | 2 | 2 | 1 |
| 7 | 2 | 1 | 1 |
| 8 | 1 | 1 | 1 |
| 9 | 1 | 1 | 1 |
| 10 | 1 | 1 | 1 |
| 11 | 1 | 0 | 0 |
| 12 | 0 | infinity | infinity |

Since v(s/121)>=1 and v(s^2/121)>=4, every perturbation coefficient
has valuation strictly greater than 3-i/4; inspect each of the thirteen
rows, including the constant. The base coefficients have valuation at
least 3-i/4. Thus Q_s is integral with leading coefficient one,
v(Q_s(0))=3 exactly, and all coefficient bounds

    v([V^i]Q_s)>=3-i/4=(12-i)/4.

The constant's leading residue is H(0)^3/11^3=10 modulo eleven,
so it cannot vanish or acquire higher valuation through cancellation.
The criterion gives v(V)=1/4 for **every** algebraic root, for all s
with v(s)>=3, irrespective of its unit part. There is no rational root.
This is stronger than an exclusion of only the positive-multiple-of-three
scalar subset, but asserts nothing about v(s)=1 or 2.

### Primitive disk at 1728

If an integral primitive scalar is 1 modulo eleven, 1728 is also 1
modulo eleven and L041 forces v(s-1728)>=4. Write u=s-1728 and W=x-16.
Define

    P(W)=F(16+W,1728),
    Q(W)=J(16+W)-3456W^11.

There is the exact identity

    F(16+W,s)=P(W)+u Q(W)-u^2 W^11.

The complete coefficient valuations of P and Q are:

| i | v([W^i]P) | v([W^i]Q) |
| --- | --- | --- |
| 0 | 22 | 22 |
| 1 | 21 | 21 |
| 2 | 19 | 19 |
| 3 | 17 | 17 |
| 4 | 15 | 15 |
| 5 | 13 | 13 |
| 6 | 11 | 11 |
| 7 | 10 | 10 |
| 8 | 8 | 8 |
| 9 | 6 | 6 |
| 10 | 4 | 4 |
| 11 | 2 | 0 |
| 12 | 0 | infinity |

All base coefficients have valuation at least 22-11i/6. Every u Q
coefficient is strictly above this bound, because v(u)>=4; the only
coefficient of -u^2 W^11 has valuation at least eight, also strictly
above 11/6. The leading coefficient stays one. The constant has
valuation exactly 22, with P(0)/11^22=1 modulo eleven, and cannot
cancel with u Q(0), whose valuation is at least 26. The criterion with
n=12 and h=11/6 gives v(W)=11/6 for every algebraic root. No rational
root exists, uniformly for all v(s-1728)>=4 and every unit part.

### Fiber necessity and all exceptional charts

The preceding polynomial-root exclusions really exclude rational
points of the entire finite modular fiber. Its points are affine,
because O has scalar infinity. If x=16, the curve gives exactly
2T=(16,-61) and 3T=(16,60). L034 proves their complete-map values
-121 and infinity, respectively. The former has v(s)=2 and fails
L041's primitive domain; the latter is not a finite scalar. Thus no
primitive-compatible point has x=16.

At any remaining point with j=s, one has sd-a=by. Substitution into
L034's elimination identity

    (sd-a)^2+b(sd-a)-b^2(x^3-x^2-10x-20)=-d F(x,s)

makes its left side zero. Since d=(x-16)^11 is nonzero, F(x,s)=0.
This necessity never divides by b and remains valid even if b=0.
Consequently a rational fiber point in either disk would give the
impossible rational root just excluded. A whole-fiber isomorphism
with A11 necessarily gives a rational fiber point by either rational
projection A11 -> Q11. Thus no such isomorphism exists. The argument
covers both rational-factor permutations and every ramified embedding
without selecting or discarding any of them.

The connecting-map exception T has scalar -24729001, whose valuation
is one. It is outside L041's primitive domain, so no zero ordinary
evaluation f(T) is assigned a class or omitted from an admissible
fiber. Likewise 4T has scalar -32768 with v(s-1728)=1 and is outside
the domain. These values follow from L034 and are checked exactly in
the certificate. Exceptional good-divisor definitions remain those of
L033; this proof excludes their scalars by the common primitive
witness condition, rather than deleting their charts.

### Exhaustion, realization and downstream scope

L041 partitions all primitive scalars into the integral domain just
used and the negative domain v(s)=-11k, k>=1. L043 excludes the latter
uniformly. The two branch disks exclude all integral scalars with
residue 0 or 1. All other integral scalars lie in L042's generic slice,
whose complete proof forces residues 4 or 10 and gives only the two
stated vectors. L042 realizes both at its exact scalar from x=500,
using the rational-factor permutation and the proved degree-ten field
comparison. Its algebra reconstruction proves entire-fiber generation,
and L041 supplies common primitive witnesses without changing that
fiber or its scalar. Thus necessity and realization both hold: the
image has exactly two elements, not merely at least two or at most two.

The sum of either vector is two modulo five, consistent with L041's
norm plane. There are 25 elements in that plane, so this result
excludes its other 23 elements. These are additional restrictions
beyond the norm baseline and can filter global K(S,5) classes after
their place valuations are known. Their nonempty local image does
not give a global class or an integer solution.

For the global consequence, L033 transports any branch solution to
the entire fiber; base change gives the assumed compatibility. L043
already forces 11 not dividing C. The proved units s and 1728-s then
give 3v11(A)=v11(s)=0 and 4v11(B)=v11(1728-s)=0, so 11 divides neither
A nor B. The five twist emptiness claims, global unit/class data and
infinitely many remaining signatures are still independent gaps.

### Exact evidence and qualifications

Run `python3 scripts/primitive-eleven-vectors/check_integral_branches.py`.
The full [certificate](../scripts/primitive-eleven-vectors/integral-branch-certificate.json)
records every exact coefficient in both identities, all thirteen
coefficient rows per disk, the uniform perturbation bounds, the exact
endpoints and exceptional-chart evaluations. All 15 checks pass; both
full bound tables, all component coefficients, exceptional values and
check results were inspected. Actual forced valuations are 1/4 and
11/6; rational roots require integer valuations. No failed check or
unproved finite precision threshold is suppressed. The mathematical
proof above, with L042's inherited realization and L043's inherited
negative-scalar exclusion, supplies completeness beyond the arithmetic
checks. The independent critical audit below is now complete; no complete
Beal candidate is claimed.

### Independent critical audit, 2026-10-10

No mathematical correction was found. This audits the stated local theorem,
not any global class intersection. Run
`python3 scripts/primitive-eleven-vectors/audit_complete_image.py`.
It imports no original calculation code, uses rational Horner composition
to recompute the complete coefficient arrays from L034's previously
audited source transcription, and compares the exact results with the
existing certificates. All 37 checks pass. The complete
[audit certificate](../scripts/primitive-eleven-vectors/complete-image-audit-certificate.json)
retains the recomputed coefficients, all branch bounds, all nine generic
and ten negative unit cases, the field and realization data and failures.
Both full branch tables, every affine negative bound and infinity exponent,
the full generic residue table and all endpoint/exceptional data were
inspected. Shared input is the source coefficient list, not an independent
retranscription of FNS; the prior L033/L034 source audits are reused.

The scalar partition has no missing unit-power condition. For an integral
primitive scalar L041 gives valuations in 3 N0 and 4 N0. Conversely its
choice of a unit u with residue q0^-1 makes q0 u^11 congruent to one, so
a fourth root lifts with derivative 4. The cube map on F11^* is bijective
and each nonzero residue root lifts with unit derivative. Using these two
roots with the same c=11^gamma u proves sufficiency, including the negative
case; it never invokes an eleventh root. The defining field's two simple
residue roots have derivatives 6 and 5. Its remaining degree-ten block is
Eisenstein with constant/11 residue 5. Correcting its uniformizer by a
tenth root of a unit congruent to one proves the exact model r^10=-55.
Thus the ordered factor dimensions 1,1,10 and residue degrees 1,1,1 used
by the local argument are justified, not inferred from repeated residues.

In the zero disk all perturbations are strictly above 3-i/4, with constant
valuation exactly 3 and normalized constant residue 10. In the other disk
they are strictly above 22-11i/6, with constant valuation exactly 22 and
residue 1. These statements include i=0,11,12 and every unit part of the
scalar. The minimum-valuation proof gives exactly 1/4 and 11/6 for each
shifted root in an algebraic closure. A rational root would have integral
valuation, an impossibility. The argument only needs the necessary
polynomial relation, which follows without dividing by b. Rational
projection of a whole-fiber isomorphism produces the required rational
point. At x=16 the complete map gives -121 or infinity; T and 4T give
-24729001 and -32768. Their finite exceptional valuations are 2,1 and
v(-32768-1728)=1, respectively, outside the primitive domain. O lies over
infinity. Thus no ordinary zero evaluation is being assigned a class.

The inherited negative proof also holds for every k>=1, not just the
minimum k. Scaling at infinity yields X^11(X-1), whose unique nonzero
residue root lifts rationally; division leaves reduction X^11 and excludes
another algebraic root at that scale. The valuation comparison forces
every other root to have v(x-16)=k+2. All nonconstant perturbation slopes
in k are nonnegative and their derivative bounds are positive after
division by eleven. Hence Rbar=sigma-sigma^2 Z^11 and
(R'/11)bar=-sigma^2 Z^10 uniformly. If the required second rational root
exists, translating it gives a monic degree-ten Eisenstein factor with
constant/11 residue 1. Any isomorphism with L would send its uniformizer
w to a uniformizer of L; w/r is a unit with residue in F11^*, so its tenth
power reduces to one. This forces constant/11 residue 5 instead, a
contradiction. If the rational root does not exist, compatibility already
fails. Reconstruction is legitimate since b is nonzero at all twelve
roots and x=16 is absent; no factor or ramified embedding is discarded.

For the generic slice, all eleven cluster roots have v(x-16)=2 and
residue z0=1/(sbar-1) after scaling. The complete derivative table gives
constant/11 residues 9,4,5,4,1,3,9,3,5 for scalar residues 2 through 10.
Thus only 4 and 10 match L. The smooth root has f a unit; every cluster
point has v11(f)=2 because f/121 reduces to 1+z0, which is nonzero.
Normalized orders are therefore 0,2,20, giving the two vectors modulo
five under the rational permutations. Field isomorphisms preserve these
orders. The x=500 construction lifts V^2+V-8520 at V=2 with derivative 5;
its scalar residue is (3+2)/4=4. Removing its rational cluster root and
the rational smooth root leaves a degree-ten Eisenstein factor with
constant/11 residue 5. The unit tenth-root correction identifies that
factor with L. At every root b is nonzero and reconstruction is unique;
the scalar is away from the branch values, so these twelve distinct
points exhaust the degree-twelve fiber. This proves entire-algebra
generation and both permutations at one scalar. L041 supplies primitive
witnesses at that same scalar, not at a newly chosen nearby fiber.

The unrestricted baseline and exceptional norm interface were also checked
at proof level: L041's point over L has ord_L(f)=1, while the rational
T class has order -1 modulo five, so independent factors give all 125
vectors. In the norm formula residue degrees, all one, weight the orders;
the weight at L is not ten. Good-divisor evaluations are locally constant
since 5 is a unit at eleven. At the exceptional unramified fiber, local
inverse lifting and a nonzero twelve-monomial determinant preserve the
entire algebra under a sufficiently small common-scalar deformation.
This validates the inherited 25-element norm baseline without requiring
the deformation to preserve primitive witnesses. For L044 itself all
exceptional scalars already fail its primitive condition.

The audit therefore confirms necessity and realization on the entire
primitive domain. It establishes no new restriction beyond this lemma,
no certified global arithmetic and no progress beyond the assessed source
methods. Mathlib coverage remains not checked.

## Mathlib

Full matching primitive whole-fiber vector theorem and its explicit
branch-disk exclusions: **not checked**. Supporting valuation,
polynomial, fiber-algebra, local-descent and Hensel declarations:
**not checked**. Unknown coverage is not absence. The result is local
progress under the existing SPECIALIZE assessment, with no claim of
progress beyond the assessed source methods or a Beal resolution.
