# L061 — Exact five-adic whole-fiber connecting classes

## Hypotheses

Use L033's curve E0: y²+y=x³−x²−10x−20, its dual connecting map
delta, and f=(x−4)y−4x²+30x−55. Use L034's complete modular map
j=(a+by)/d, d=(x−16)^11, J=2a−b and

    h=x^4−52820x^3+1333262x²+4971236x+9789217,
    F_s=h³+sJ−s²d.

The full source coefficients of a,b,d,h,J are retained in
`scripts/five-adic-exact-list/certificate.json`, `source_polynomials`;
they agree with the previously audited L034 coefficients.
Use exactly L035's whole-fiber image I_fiber and primitive image I_pow,
allowing every entire-fiber isomorphism and good-divisor evaluations.
Fix L038's entire algebra A=Q5 × U, U unramified of degree eleven.
There is no global point, class/unit basis, GRH, rank or Sha premise.

Identify U=Q5(t) using the monic polynomial

    H(t)=t^11+3t^10+4t^9+t^8+3t^7+2t^6+4t^5
           +4t^4+2t²+t+3.

Write R for its full integer ring, k=R/5R, q=5^11. Coefficient vectors
below are ascending in the basis 1,t,...,t^10. The coefficient lift of
w in k has coefficients 0,...,4 in R. The word class always refers to
the fifth-power class of a nonzero field element.

## Conclusion

A scalar s has an entire fiber B_s isomorphic to A if and only if

    s in 2+5 Z5.

In particular the other disk allowed by L060, 4+5 Z5, is incompatible.
The exact common image I_pow=I_fiber has **55** elements. The following
table and formula give every element explicitly. Let w_s be the element
of k represented by the indicated vector, and let beta_s be the integer
in the second column.

| s | beta_s | w_s, ascending coefficients |
|---|---:|---|
| 2 | 38 | (4,3,0,2,4,4,2,4,0,1,0) |
| 7 | 123 | (1,4,1,4,2,4,2,0,0,0,1) |
| 12 | 108 | (3,0,2,1,0,4,2,1,0,4,2) |
| 17 | 118 | (0,1,3,3,3,4,2,2,0,3,3) |
| 22 | 28 | (2,2,4,0,1,4,2,3,0,2,4) |

For each row take i=0,...,10 and form the pair of fifth-power classes

    ( class(beta_s), class(1−5 coefficient_lift(w_s^(5^i))) ).       (1)

These 55 pairs are distinct and constitute the whole image. The choice
of unramified algebra identification changes coordinates, not coverage:
all eleven embeddings are retained. Every pair has an exact whole-fiber
realization; this is not a list of merely necessary candidates.

This supplies a local membership test for future global class
intersection. It neither evaluates the global class image nor excludes
the 54a1 integer branch or any further Beal signature. The independent
critical audit below confirms this local result without correction.

## Proof

### Imported methods and the fixed integral model

We reuse the dual descent and normalization from L033, imported from
Schaefer–Stoll, *How to do a p-descent on an elliptic curve*, Trans. AMS
356 (2004), 1209–1231, [DOI](https://doi.org/10.1090/S0002-9947-03-03366-X),
[June 13, 2001 manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf),
Section 5, pp.8–10, and Section 9, pp.21–24. This identifies delta with
ordinary f-evaluation off T,O and good-divisor evaluation at them. The
complete modular map is L034's audited specialization of Freitas–Naskręcki–Stoll,
*The generalized Fermat equation with exponents 2, 3, n*, Compositio Math.
156 (2020), 77–113, [June 10, 2019 manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
Section 7.2, equation (7.4), p.27. Its degree is twelve, its branch
values are 0,1728,infinity, its poles are O and 3T, and its removable
point 2T has value −121. No Q2 square-class result is applied at five.

The polynomial H is exactly L039's irreducible degree-eleven residue
factor, lifted with the same integer coefficients. Its irreducibility
over F5 was proved there by H dividing X^(5^11)−X and
gcd(H,X^5−X)=1; the present verification repeats these tests. Its
reduction is separable. The integral root field therefore has degree
eleven and residue degree eleven, hence ramification index one.
The classification of unramified extensions identifies it with U.
These uses import Milne, *Algebraic Number Theory*,
[v3.08, July 19, 2020](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
Theorem 7.33 and Remark 7.36, pp.121–122; Corollary 7.42 and
Remark 7.43, p.124; Proposition 7.50, pp.127–128.

Moreover Z5[t] is the full integer ring R. Separability of H modulo
five gives unit power-basis discriminant. Apply Milne Proposition 2.43,
p.40, to the PID Z5: the integral closure is contained in the inverse
discriminant times the power-basis lattice, which here equals that
lattice. Thus R/125R is faithfully (Z/125Z)[t]/(H). No polynomial-order
approximation to the maximal integer ring is used.

Strong Hensel lifting is imported from Clark, *Algebraic Number Theory II*,
[161-page notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
Theorem 1.79, p.58, version retrieved 2026-10-12, revision date
unidentified. In particular 1+125R and 1+125Z5 consist of fifth powers:
for Z^5−u at 1, v(error)>=3>2v(derivative)=2. Coordinate lifting below
uses unit derivatives. The finite unit specialization below is needed
to decide this explicit list; no general Hensel or descent reproof is
being claimed. Clark Theorem 2.36, p.79, covers general higher-unit
indices, but an index alone does not provide these labels or collisions.

### Complete fibers in both scalar disks

L060 already excludes every scalar outside the two integral disks
2+5Z5 and 4+5Z5. Direct residue factorization gives

    Fbar_2 = X Hbar,
    Fbar_4 = X(X−1) P Q,
    P = X^5+2X^4+3X^3+4X²+X+1,
    Q = X^5+2X^4+2X^3+4X²+3X+4.

The four factors in the second line are irreducible and pairwise
coprime over F5. The two quintics satisfy X^(5^5)=X modulo the
quintic and have gcd one with X^5−X, which is the complete prime-degree
irreducibility test. All exact factors and Frobenius remainders are
in the certificate; `verify.py` independently recomputes both tests
over F5. Both Fbar_r are squarefree and coprime to bbar. L060 already
proves those last conditions, and both scripts check them again.

For every scalar in either disk, monic coprime Hensel lifting therefore
preserves the complete factor degrees and irreducible separable
reductions. First justify that these are the actual fiber factors,
rather than merely factors of a necessary polynomial. At each root x
of F_s, b(x) is a unit and reconstruct

    y=(sd(x)−a(x))/b(x).

The exact polynomial identity

    (sd−a)²+b(sd−a)−b²g = −d F_s,
    g=X³−X²−10X−20,

gives the curve equation. If x≠16 the source map gives j=s. At x=16
the arithmetic identities give

    F_s(16)=J(16)(s+121),  J(16)≠0,
    a(16)=−61b(16),       b(16)≠0.

Thus this root occurs only at s=−121, and reconstructs precisely
(16,−61)=2T, whose regular modular value is indeed −121. The other
point (16,60)=3T is a pole. Neither O nor a pole supplies an extra finite
fiber point. Every F_s has twelve distinct geometric roots, giving
twelve distinct reconstructed points of the actual fiber. Since j is
degree twelve and these disks avoid its branch values, they exhaust the
whole étale fiber. Conversely the source polynomial relation holds at
all finite fiber points by regularity; no coordinate chart was discarded.
Consequently B_s=Q5[X]/(F_s) throughout both disks, including s=−121.

The degree and residue degree argument already used for H shows that
each lifted irreducible factor of degree d gives U_d. Hence

    B_s = Q5 × U_11                 when s=2 modulo five,
    B_s = Q5 × Q5 × U_5 × U_5       when s=4 modulo five.

The first is A; the second cannot be A since an algebra isomorphism
preserves primitive idempotents and factor dimensions. This proves the
exact scalar domain. In particular s=j(T)=−24729001 and s=j(2T)=−121
both lie in the excluded residue-four disk. They were tested, not
silently removed. No zero f-value is assigned a fifth-power class.

### Faithful unit labels and collision decisions

For a unit u in R define the residue-field label

    Lambda(u) = (u^(q−1)−1)/5 modulo 5R.                           (2)

The numerator is divisible by five since k has q elements. This label
depends only on u modulo 25R, and multiplication makes it additive.
If u=v^5 then v^(q−1)=1 modulo 5R, whose fifth power is one modulo
25R; thus Lambda(u)=0. Conversely suppose Lambda(u)=0. Choose a
unit t0 lifting the unique fifth root of ubar in k, namely ubar^(5^10).
Put z=u/t0^5. It is one modulo five. Also z^(q−1)=1 modulo 25:
the numerator has this property by assumption, and the denominator
t0^(5(q−1)) has it by the preceding fifth-power argument. Write
z=1+5c modulo 25. Expansion gives

    z^(q−1)=1+5(q−1)c modulo 25.

Since q−1 is a unit modulo five, c=0, so z=1 modulo 25. Write
z=1+25w modulo 125. Then

    (t0(1+5w))^5 = u modulo 125.

All omitted binomial terms are divisible by 125. This unit root
modulo 125 lifts to an exact fifth root by strong Hensel, with the
strict inequality 3>2. Therefore Lambda(u)=0 if and only if u is
a fifth power. Two units have equal labels if and only if their
ratio is a fifth power. Also Lambda(1−5 coefficient_lift(w))=w,
because q−1=−1 modulo five. Thus (2) is an isomorphism from the
unit fifth-power quotient onto the additive field k, and the explicit
representatives in (1) are faithful. This derivation specializes the
assessed unit method; it does not rely on a guessed smaller precision.

The implementation uses exactly this proof: reject a nonzero ratio
label; otherwise choose t0 by inverse Frobenius, compute w modulo
five and store the root t0(1+5w) modulo 125. For every collision it
verifies the full equality of fifth powers in R/125R. For every pair
of distinct classes it stores a nonzero coordinate difference of the
labels, a complete rejection witness. Equality of raw f-values or
different scalar residues is never substituted for class comparison.

### Complete enumeration and exact realizations

There are 25 scalar residues s=2,7,...,122 modulo 125. In the fixed k,
Hbar has eleven distinct roots, exactly tbar^(5^i), i=0,...,10.
For each scalar residue and each root, simple coordinate lifting
uniquely determines x modulo 125R; b is a unit, so reconstruction
uniquely determines y there. The values f are units: on the degree-eleven
factor xbar is not in F5 and in particular is not zero; L033's identity
f(P)f(−P)=−(x−5)^5 makes both factors units.

For an arbitrary exact s with that residue, the unique exact Hensel
coordinate roots reduce to these same x,y,f modulo 125. This covers
every actual fiber class and every embedding, by the full factor
description. Conversely use the ordinary integer s for any enumerated
row. The preceding whole-fiber argument supplies an exact isomorphism
B_s -> A, and the root with the specified residue is an exact U point.
It is one of the eleven embeddings of the complete degree-eleven
factor. Thus every row represents an exact entire-fiber realization,
with the same scalar on its rational and U factors. This is both
directions of coverage, not a numerical stabilization argument.

For a fixed scalar, multiply the eleven unit f-values modulo 125R.
Their exact lifts range over every embedding, so this product is
N_(U/Q5)(f_U) modulo 125. Its coefficients other than the constant
coefficient vanish. Write the constant residue as n_s. L035's complete
norm identity determines the rational component uniquely as

    class(alpha_0)=class(121/N_(U/Q5)(f_U)).

Thus beta=121/n_s modulo 125 represents it. Norms are units, so the
choice of unit lift does not change the class. This recovers the full
product class rather than merely its U projection. The exceptional
good-divisor norm convention from L035 remains valid, although no
exceptional T fiber survives the factor test here.

The full 275-row computation partitions the rows into 55 classes,
each with five members. Precisely, the class of a row is unchanged
under s -> s+25 with the same residue embedding, and no other
collision occurs. The first 55 rows, s=2,7,12,17,22 with all eleven
embeddings, are a complete list of representatives. The certificate
records every membership, 275 U and rational fifth-root witnesses,
all 1,485 unordered pairs of distinct-class rejection witnesses and
55 additional roots comparing the chosen f-values with the explicit
representatives 1−5 coefficient_lift(Lambda(f)).

For the embedding with residue x=tbar the five labels and rational
representatives are exactly the table. Galois equivariance of f and
(2) sends each label to its successive fifth-power Frobenius conjugates
in k and leaves the rational class fixed. The verification checks all
eleven elements in each orbit against the full row list. Hence (1)
is the displayed explicit list, with 55 distinct classes and exact
realizations. L040 identifies I_pow with I_fiber without changing the
point, scalar or embedding; that already audited equality transfers
the same list to I_pow.

### Certificate verification and scope

Run `python3 scripts/five-adic-exact-list/compute.py`, then
`python3 scripts/five-adic-exact-list/verify.py`.
The construction has 26 passing summary checks and no failures;
the separate arithmetic replay has 23 and no failures. The replay
imports no construction code. It verifies all source coefficients,
complete factors and their irreducibility/coprimality, every one of
the 275 coordinate/f/label records, every norm, every collision root,
all 1,485 noncollision witnesses, all explicit representatives and
all five Frobenius orbits. The actual/required realization pair count
is 275/275; the other 275 formerly possible pairs are uniformly ruled
out by the full residue-four factors. Exact size 55 is below L060's
upper bound 600. Complete factors, irreducibility evidence, labels,
memberships and verification results were inspected, with all larger
row and witness arrays replayed in full.

The full certificates are `scripts/five-adic-exact-list/certificate.json`
and `scripts/five-adic-exact-list/verification.json`. They provide
arithmetic evidence; the uniform whole-fiber, integral-ring, unit-kernel
and exact-realization arguments above are essential to interpreting it.
The initial attempted degree-eleven splitting at residue four failed
because that factor hypothesis was false; its corrected complete
factorization is retained. No partial list was labeled exact.

This is REPRODUCTION of assessed general methods through explicit
local arithmetic, not a claim of mathematical originality. The independent
critical audit below checks the uniform arguments and the complete
certificate interface. Global class/unit values, simultaneous
other-place compatibility, global points, integer lifts, other modular
twists and infinitely many signatures remain unresolved. I_fiber is
never assumed to be a subgroup.

### Independent critical audit, 2026-10-12

The prior SPECIALIZE assessment for this exact target is reused. No
mathematical correction is needed. This audit confirms the local membership
theorem; it supplies no stronger restriction, global intersection, integer
exclusion or originality beyond the sources checked.

**Entire fibers and integral model.** The separate implementation
`python3 scripts/five-adic-exact-list/audit.py` imports neither construction
nor replay code. It compares every source coefficient with the previously
audited L034 transcription, checks b,d,h,J,g and the integer elimination
identity, and reconstructs both F reductions from those coefficients.
Factor products are thus compared with the actual source polynomial,
not merely another stored candidate. The complete degrees are 1+11 and
1+1+5+5. Each degree-5 or degree-11 factor passes the prime-degree Frobenius
test; all factors are separable and pairwise coprime, and both complete
reductions are coprime to b.

For every exact scalar in either disk, F_s is monic integral. The cited
coprime lifting theorem over the complete DVR Z5 gives all factors.
Irreducible reduction forces irreducibility of each monic lift and residue
degree at least its degree; the complete-field degree formula forces
equality and ramification index one. Perfect finite residue fields satisfy
Milne Proposition 7.50's hypotheses. Each degree-eleven factor therefore
has precisely eleven embeddings into the fixed U, corresponding to its
residue roots. Different factor dimensions prevent exchanging the rational
and degree-eleven components in an isomorphism with A.

Reverse reconstruction works over the splitting field: b is a unit at
every integral root and the elimination identity gives the curve equation.
Away from x=16 the map equation gives j=s. At x=16 the audit checks
J(16)=11^22, h(16)^3=121J(16), a(16)=61b(16), and b(16) a 5-adic unit.
Thus this root occurs only at s=-121 and reconstructs y=-61, the removable
2T chart with that regular map value. The conjugate point is the pole 3T;
together with O these are the complete poles by L034. The twelve distinct
roots give twelve distinct points, exhausting the degree-twelve finite
locally free fiber. Both disks avoid 0,1728,infinity. L060 already excludes
every other scalar, including all negative valuations, uniformly.
Both j(T) and j(2T) reduce to four and are retained in the incompatible
product algebra; no zero f-value is assigned a class.

For the fixed H the audit checks gcd(H,H')=1 modulo five and irreducibility.
The power basis has unit discriminant, so Milne Proposition 2.43 over Z5
puts the full integral closure inside that same lattice. Every coefficient
operation modulo 125 therefore takes place in the maximal integer ring R.
The valuation normalization is v(5)=1 in both U and Q5.

**Faithful classes, precision and realization.** Multiplication of units
adds the labels in (2), because the cross term is divisible by 25. A fifth
power has label zero. Conversely inverse Frobenius in k, with exponent
5^10, supplies a residue fifth root of any unit. After division by its
coefficient lift's fifth power, the quotient z is one modulo five. Label
zero and the unit q-1 force z=1 modulo 25. Write z=1+25w modulo 125.
Multiplying the preliminary root by 1+5w corrects its fifth power: the
linear term is 25w and every higher binomial term is divisible by 125.
For the exact unit equation, strong Hensel has error valuation at least
three and derivative valuation one, so its strict inequality is 3>2;
an already exact root is immediate. This proves the whole kernel, rather
than necessity or a cardinality comparison. Since q-1=-1 modulo five,
the label of 1-5 lift(w) is w, with the displayed sign. The same strong
Hensel check turns every stored rational collision root into an exact
Q5 root.

All 275 records satisfy F_s=0, the curve equation and the modular numerator
equation modulo 125, with unit coordinate derivatives, b-values and
f-values. Each specified residue root has a unique exact lift for any
exact scalar in its residue class modulo 125; that lift and its f-value
reduce to the recorded coordinates. This covers every scalar and all
eleven embeddings. Conversely, choosing the ordinary integer s in a row
supplies its exact lift and the unique rational factor of the same whole
fiber. The complete factor decomposition gives an entire isomorphism
B_s -> A realizing that row. Neither different scalars on different
factors nor finite precision alone are used to infer realization.

The product over all eleven lifted embeddings is the U/Q5 norm; every
product is checked modulo 125. L035 determines the rational class uniquely
from the U class, because the rational factor's norm is the identity map.
Additionally, the audit lifts the rational root for all 25 scalars by
complete base-five digit enumeration, reconstructs y and f, and checks
both the full L034 norm formula modulo 125 and a fifth-root witness for
f/beta. These independent tests have unit f-values and unit roots.

Every one of the 275 collision witnesses is checked in both factors;
every one of the 1485 unordered noncollision pairs has its nonzero label
difference verified. All 55 explicit representatives have the correct
label and fifth-root comparison, and all memberships and entries of the
prior verification list agree. The five displayed seeds give disjoint
orbits of length eleven, with the stated rational representatives.
Frobenius here is the residue action: its unique lift to an automorphism
of U preserves f and (2). No assertion that t -> t^5 is an automorphism
in the characteristic-zero polynomial model is needed. L040 transfers
the list to I_pow with the point, scalar and isomorphism unchanged.

All 28 audit checks pass, with no failures. The complete certificate is
`scripts/five-adic-exact-list/audit-certificate.json`; it retains input
hashes, exact chart values, full finite-field tests, every coordinate
residual, all norm and direct rational checks, every collision and
noncollision comparison, and all five orbits. Both previous certificates
were loaded in full and their load-bearing arrays replayed; a passing
summary is not substituted for that verification. Actual/required pair
coverage is 275/275, noncollision coverage 1485/1485, and explicit
representative coverage 55/55. Exact size 55 is verified, not merely
bounded by 600. The global and integer gaps remain open.

## Mathlib

Full exact 55-class result and matching explicit computation: **not
checked**. Supporting unramified-extension, integral-basis, Hensel,
finite-field, norm and elliptic connecting-map coverage: **not checked**.
Unknown coverage is not evidence of absence. Named general inputs are
imported by the precise citations above.
